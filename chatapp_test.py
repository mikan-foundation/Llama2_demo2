from tkinter import *
from llama_cpp import Llama

def generate_dummy_response(prompt):
    llm = Llama(model_path="C:/Users/hirot/Python/VSC/AoS/Llama2/llama-2-7b-chat.ggmlv3.q8_0.bin")
    response = llm(prompt,max_tokens=500,temperature=0.1,stop=["Instruction:", "Input:", "Response:"],echo=True)
    response = response['choices'][0]['text']
    response_text = response.replace(' Response:', '').strip()  # ' Response:' を除去
    return response_text

def on_button_click():
    prompt = """What is the height of Mount Fuji?"""
    response = generate_dummy_response(prompt)
    text_box.insert(END, "Llama2: {}\n".format(response))

root = Tk()
root.title("生成テスト")
root.geometry("800x600")
text_box = Text(root)
text_box.pack(side=TOP, fill=BOTH, expand=True)
button = Button(root, text="生成開始", command=on_button_click)
button.pack(side=TOP, fill=X)

root.mainloop()
