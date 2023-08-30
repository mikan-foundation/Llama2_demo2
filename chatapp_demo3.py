from tkinter import *
from tkinter import font
from llama_cpp import Llama
from threading import Thread

class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.llm = Llama(model_path="model path")

    def init_window(self):
        self.master.title("LLM Chat")
        self.pack(fill=BOTH, expand=1)
        chat_font = font.Font(size=14)
        self.chat_text = Text(self, font=chat_font)
        self.chat_text.pack(side=TOP, fill=BOTH, expand=True)
        self.chat_text.config(state=DISABLED)
        self.chat_text.tag_configure("user", background="lightblue")
        self.chat_text.tag_configure("llm", background="lightgreen")
        self.status_label = Label(self, text="")
        self.status_label.pack(side=LEFT, fill=X)
        self.text_entry = Entry(self, bd=5)
        self.text_entry.pack(side=LEFT, fill=BOTH, expand=True)
        self.text_entry.bind('<Return>', lambda event: self.send_message())
        button_font = font.Font(size=10, weight="bold")
        self.send_button = Button(self, text="Send", command=self.send_message, bg="lightblue", fg="darkblue", font=button_font, relief="ridge", bd=3)
        self.send_button.pack(side=RIGHT)

    def add_message(self, user, message):
        self.chat_text.config(state=NORMAL)
        tag = "user" if user == "User" else "llm"
        self.chat_text.insert(END, "{}: {}\n".format(user, message), tag)
        self.chat_text.config(state=DISABLED)

    def update_status(self, status):
        self.status_label.config(text=status)

    def generate_response(self):
        chat_history = self.chat_text.get("1.0", END)
        chat_history = chat_history + "\n Response:\n"
        self.update_status("Generating response...")
        response = self.llm(chat_history, max_tokens=500, temperature=0.1, stop=["Instruction:", "Input:", "Response:"], echo=False)
        response_text = response['choices'][0]['text']
        response_text = response_text.replace(' Response:', '').strip()
        self.add_message("LLM", response_text)
        self.text_entry.delete(0, 'end')
        self.update_status("Response generated.")

    def send_message(self):
        user_message = self.text_entry.get()
        self.add_message("User", user_message)
        self.text_entry.delete(0, 'end')
        Thread(target=self.generate_response).start()

root = Tk()
root.geometry("800x600")
app = ChatInterface(root)
root.mainloop()