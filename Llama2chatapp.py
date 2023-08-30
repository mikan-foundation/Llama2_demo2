from tkinter import *
from tkinter import font
from llama_cpp import Llama
from threading import Thread

# ChatInterface クラスを定義
class ChatInterface(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)  # Frame クラスの初期化
        self.master = master  # マスターウィンドウを設定

        # チャットインターフェースを初期化
        self.init_window()

        # LLM モデルを初期化
        self.llm = Llama(model_path="model path")

    # ウィンドウを初期化
    def init_window(self):
        self.master.title("LLM Chat")  # ウィンドウのタイトルを設定
        self.pack(fill=BOTH, expand=1)  # ウィンドウサイズを動的に調整

        # チャット用のテキストボックスを追加
        chat_font = font.Font(size=14)  # フォント設定
        self.chat_text = Text(self, font=chat_font)  # テキストボックスを作成
        self.chat_text.pack(side=TOP, fill=BOTH, expand=True)  # レイアウト設定
        self.chat_text.config(state=DISABLED)  # 初期状態は入力不可に
        self.chat_text.tag_configure("user", background="lightblue")  # ユーザーのメッセージの背景色
        self.chat_text.tag_configure("llm", background="lightgreen")  # LLM のメッセージの背景色

        # ステータスラベルを追加
        self.status_label = Label(self, text="")  # ラベル作成
        self.status_label.pack(side=LEFT, fill=X)  # レイアウト設定

        # メッセージ入力用のテキストボックスを追加
        self.text_entry = Entry(self, bd=5)  # 入力ボックスを作成
        self.text_entry.pack(side=LEFT, fill=BOTH, expand=True)  # レイアウト設定
        self.text_entry.bind('<Return>', lambda event: self.send_message())  # Enter キーで send_message() を呼び出し

        # 送信ボタンを追加
        button_font = font.Font(size=10, weight="bold")  # フォント設定
        self.send_button = Button(self, text="Send", command=self.send_message, bg="lightblue", fg="darkblue", font=button_font, relief="ridge", bd=3)  # ボタン作成
        self.send_button.pack(side=RIGHT)  # レイアウト設定


    # チャットにメッセージを追加
    def add_message(self, user, message):
        self.chat_text.config(state=NORMAL)  # テキストボックスを編集可能に
        tag = "user" if user == "User" else "llm"  # タグを設定
        self.chat_text.insert(END, "{}: {}\n".format(user, message), tag)  # メッセージを追加
        self.chat_text.config(state=DISABLED)  # テキストボックスを編集不可に戻す

    # ステータスメッセージを更新
    def update_status(self, status):
        self.status_label.config(text=status)  # ステータスラベルを更新

    # LLM モデルで応答を生成
    def generate_response(self):
        # チャット履歴を全て取得
        chat_history = self.chat_text.get("1.0", END)
        
        # チャット履歴に指示と応答のタグを追加
        chat_history = chat_history + "\n Response:\n"

        # ステータスを更新
        self.update_status("Generating response...")

        # LLM モデルで応答を生成
        response = self.llm(chat_history, max_tokens=500, temperature=0.1, stop=["Instruction:", "Input:", "Response:"], echo=False)
        
        # 生成された応答をテキストとして抽出
        response_text = response['choices'][0]['text']
        response_text = response_text.replace(' Response:', '').strip()  # ' Response:' を除去

        # LLM の応答をチャットに追加
        self.add_message("LLM", response_text)

        # 入力ボックスをクリア
        self.text_entry.delete(0, 'end')

        # ステータスを更新
        self.update_status("Response generated.")

    # メッセージを送信（LLM モデルに問い合わせ）
    def send_message(self):
        user_message = self.text_entry.get()  # ユーザーメッセージを取得
        self.add_message("User", user_message)  # チャットにユーザーメッセージを追加
        self.text_entry.delete(0, 'end')  # 入力ボックスをクリア
        Thread(target=self.generate_response).start()  # 応答生成を別スレッドで開始

# Tkinter ウィンドウを作成
root = Tk()
root.geometry("800x600")  # ウィンドウサイズを設定

# ChatInterface インスタンスを作成
app = ChatInterface(root)

# アプリケーションを実行
root.mainloop()