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
