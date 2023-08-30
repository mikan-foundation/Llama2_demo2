---
marp: true
theme: default
header: "**Llama2でチャットアプリを作るハンズオン by未完Labo**"

size: 16:9
paginate: true

style: |
    section.title {
        --title-height: 130px;
        --subtitle-height: 70px;

        overflow: visible;
        display: grid;
        grid-template-columns: 1fr;
        grid-template-rows: 1fr var(--title-height) var(--subtitle-height) 1fr;
        grid-template-areas: "." "title" "subtitle" ".";
    }
    section.title header{
        color:white;
    }
    section.title h1,
    section.title h2 {
        margin: 0;
        padding: 0;
        text-align: center;
        height: var(--area-height);
        line-height: var(--area-height);
        font-size: 92px;
        color: white;

        border: 1px dashed gray; /* debug */
    }

    section.title h1 {
        grid-area: title;
        --area-height: var(--title-height);
    }

    section.title h2 {
        grid-area: subtitle;
        --area-height: var(--subtitle-height);
    }

    section {
        justify-content: start;
        font: "Meiryo";
        
    }
    
    table {
        padding-left: 60%;
    }

    section.title h6 {
        font-size:3px;
    }

---
<!-- _class: title -->


![bg](images/Llama2ハンズオンサムネイル.png)

<!--
_color: black
-->
---

# 今日のイベントについて
<br>

###### 最近話題の**言語モデル**と**Tkinter**というライブラリを使ってチャットアプリを作ろう！という勉強会です。

###### 全2回でこの第1回は言語モデルを自分のパソコンで動かし、かつTkinterを触ることができるというのがゴールになります。

###### 第2回では第1回で学んだことを活かしてAIとの対話形式のチャットアプリを作っていきます。

<br>

### 本日のイベントは北海道でITエンジニアを目指すU-25のためのコミュニティ未完Laboが主催します

---
# 未完Laboについて
#### 「**技術で地域を良くする。**」がコンセプトの未完Foundationが運営する、北海道・札幌のITに関わる全てのU-25のためのオンラインコミュニティです。

#### 「**技術を学ぶためには、まずは技術で遊び・研究・探求すること**」をモットーに「技術を学び、技術で遊ぶ」というコンセプトで運営されています。

---

# 自己紹介

#### 岩本宙士
###### Twitter:@Iwamoto_eng

##### pythonでbotや管理システム・小規模なAIアプリを作成

#####  バックエンドが好き、データ・AI大好き

##### 別で生成AIコミュニティのマネージャーもしてます

![bg right](images/profile_image.jpg)

---

# LLMとは？
## 大規模言語モデルという意味

###### 多くのテキストデータから学習して文章を生成するAIモデル

## なぜ最近話題なのか？

###### 自然な応答、問題発言をしない、使いやすいインターフェースのアプリ

###### このハンズオンでは自分でチャットアプリを1から作ってみることで使いやすいインターフェースの凄さとchatGPTの精度の高さを実感出来ます

###### Llama2はMetaとMicrosoftが開発した大規模言語モデルで大きいモデルはGPT-3.5と同等の性能


---
# 何故Llama2？

## オープンソースで誰でも使えて商用利用も可能


###### 最近の言語モデルのトレンドは大規模化、その中でノートパソコンでも動かせる軽めの言語モデルでモデルさえあればオフライン環境で実行ができる



| モデル名| パラメータ数|
|-----------|-------------|
| GPT-4     | 100兆       |
| Bing AI   | 1兆         |
| GPT-3     | 1750億      |
| Llama2 70B| 700億       |



---
# Tkinterでチャットアプリを作るために必要な機能

<!-- _class: image -->

![width:1000ox](images/tkinter2.png)

---

# 実際にどんな関数を実装するか考えよう

#### 1.ウィンドウ初期化用関数
#### 2.チャットにメッセージを追加する関数
#### 3.生成中などのステータスメッセージを更新する関数
#### 4.メッセージを生成する関数(前回作成したものLlama2のプログラムを流用)
#### 5.テキストボックスのメッセージをLlama2に渡す関数


---

# 開発環境を準備しよう

##### 1.好きな場所に今日の作業フォルダを作成する
##### 2.作成したフォルダをVSCodeで開く
##### 3.VSCodeの Terminal > New Terminal からターミナルを開く
##### 4.python -m venv .venv を実行します
##### 5.Mac / Windowsで以下のコマンドを実行してください
**Mac** ```.venv/bin/activate``` **Windows** `.venv/Scripts/activate`

---
# 開発環境を準備しよう

##### 1.VSCode上でmain.pyを作成
##### 2.画面の右上を確認して以下のような表記があればOK
![](images/python_env_image.png)
##### 3.でなければ、拡張機能を左のメニューのExtensionsからインストール
![](images/extensions_image.png)

---

# Llama2のモデルのダウンロードと環境構築

#### 1.discordに送信したLlama2ライセンスのコピーを読んでください
#### 2.discordに送信したモデルのダウンロードリンクからダウンロードしてください
#### 3.VSCodeのターミナルから以下のコマンドを実行してください
`pip install llama-cpp-python`

### ※コードやコマンドは全てdiscordのllama2アプリ第2回チャンネルにも貼っていきます

---

# 試しに生成した結果のみを画面に表示してみよう

`chatapp_test.py`
![width:1000px](images/chatapp_test1.png)

---

# 固まったのはなぜ？
![width:1000px](images/roop_image.png)

---

# チャットアプリの要素を個別に実装していこう - 1

`chatapp_demo1.py`
![width:1200px](images/demo1.png)

---
# チャットアプリの要素を個別に実装していこう - 2

`chatapp_demo2.py`
![width:1200px](images/demo2.png)

---

# チャットアプリの要素を個別に実装していこう - 3 

`chatapp_demo3.py`
![width:1000px](images/demo3.png)

---

# ※余裕がある人向け:Llama2の文章を翻訳してやり取りしよう

### 以下のコマンドを実行してgoogletransのver4.0.0-rc1をインストールした後、下記のプログラムを実行する
`pip install googletrans==4.0.0-rc1`

`translate-jp.py`
![width:600px](images/program6.png)