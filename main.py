import tkinter as tk

class Application(tk.Frame):
    # label Widgetのテキストに関する情報を格納する変数
    labelTextVariable = None
    # label Widgetに関する情報を格納する変数
    label = None

    # label Widgetのテキスト情報を変更する関数
    def runLabelText(self, event):
        # get() : label Widgetのテキストを取得する。
        # print(self.labelTextVariable.get())
        # set() : label Widgetのテキストをhogeへ変更する。
        self.labelTextVariable.set('hoge')

    # StringVar説明用に構成される関数
    def configForStringVar(self, frame):
        # StringVarを利用して、label Widgetで扱うテキスト情報を文字列型変数として扱う。
        # 初期値として、testの文字列を格納する。
        self.labelTextVariable = tk.StringVar(value="test")

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # textvariable : テキスト情報を表示する。値を可変なself.labelTextVariableとする。
        # background : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # width : 幅の設定
        # height : 高さの設定
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        self.label = tk.Label(frame, textvariable=self.labelTextVariable, background='blue', width=10, height=5)

        # label Widgetをクリックした場合に、関数を実行できるようにbind関数を利用する。
        # 第一引数 : イベント内容
        # 第二引数 : 実行する関数
        # bindについて : https://kuroro.blog/python/eI5ApJE1wkU7bHsuwk0H/
        self.label.bind("<ButtonPress>", self.runLabelText)

        # frame Widget(Frame)を親要素とした場合に、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.label.pack()

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # StringVar説明用
        self.configForStringVar(frame)

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
