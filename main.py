import tkinter as tk

class Application(tk.Frame):
    # label Widgetに関する情報を格納する変数
    label = None
    # labelのテキストに関する情報を格納する変数
    labelTextVariable = None

    # entry Widget for intVar用に情報を格納する変数
    entryForIntVar = None
    # entry for intVarの数値に関する情報を格納する変数
    entryTextVariableForIntVar = None

    # entry Widget for DoubleVar用に情報を格納する変数
    entryForDoubleVar = None
    # entry for DoubleVarの数値に関する情報を格納する変数
    entryTextVariableForDoubleVar = None

    # checkbutton Widget用に情報を格納する変数
    checkbutton = None
    # checkbuttonのBoolean値に関する情報を格納する変数
    checkbuttonVariable = None

    # labelのテキストを取得する。
    def getLabelText(self):
        # get() : labelのテキストを取得する。
        print(self.labelTextVariable.get())

    # labelのテキストを'hoge'へ設定する。
    def setLabelText(self):
        # set() : 引数へ設定される値へ変更する。
        self.labelTextVariable.set('hoge')
        # text optionを変更する場合
        # self.label['text'] = 'hoge'
        # self.label.configure(text='hoge')

    # entryの数値を取得する。
    def getEntryInt(self):
        # get() : entryの数値を取得する。
        print(self.entryTextVariableForIntVar.get())

    # entryの数値を1へ設定する。
    def setEntryInt(self):
        # set() : 引数へ設定される値へ変更する。
        self.entryTextVariableForIntVar.set(1)

    # entryの数値を取得する。
    def getEntryDouble(self):
        # get() : entryの数値を取得する。
        print(self.entryTextVariableForDoubleVar.get())

    # entryの数値を2.2へ設定する。
    def setEntryDouble(self):
        # set() : 引数へ設定される値へ変更する。
        self.entryTextVariableForDoubleVar.set(2.2)

        # entryの数値を取得する。

    # checkbuttonのBoolean値を取得する。
    def getCheckbutton(self):
        # get() : checkbuttonのBoolean値を取得する。
        print(self.checkbuttonVariable.get())

    # checkbuttonのBoolean値をTrueへ設定する。
    def setCheckbutton(self):
        # set() : 引数へ設定される値へ変更する。
        self.checkbuttonVariable.set(True)

    # DoubleVar説明用に構成される関数
    def configForDoubleVar(self, frame):
        # DoubleVarを利用して、entry Widgetで扱う数値情報を変数として扱う。
        # 初期化として、1.1を格納する。
        self.entryTextVariableForDoubleVar = tk.DoubleVar(value=1.1)

        # Frameを親要素として、entry Widgetを作成する。
        # textvariable : 数値情報を扱う変数を代入する。
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        self.entryForDoubleVar = tk.Entry(frame, textvariable=self.entryTextVariableForDoubleVar)

        # Frameを親要素とした場合に、entry Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.entryForDoubleVar.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        getEntryDoubleButton = tk.Button(frame, text="数値取得", width=15, command=self.getEntryDouble)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        getEntryDoubleButton.pack(side=tk.LEFT)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        setEntryDoubleButton = tk.Button(frame, text="数値設定", width=15, command=self.setEntryDouble)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        setEntryDoubleButton.pack(side=tk.LEFT)

        # DoubleVar説明用に構成される関数

    # BooleanVar説明用に構成される関数
    def configForBooleanVar(self, frame):
        # BooleanVarを利用して、checkbutton Widgetで扱うBoolean情報を変数として扱う。
        # 初期化として、Falseを格納する。
        self.checkbuttonVariable = tk.BooleanVar(value=False)

        # Frameを親要素として、checkbutton Widgetを作成する。
        # variable : Boolean情報を扱う変数を代入する。
        # Checkbuttonについて : https://kuroro.blog/python/gspi4F2pMIkzHN7l0f1F/
        self.checkbutton = tk.Checkbutton(frame, variable=self.checkbuttonVariable)

        # Frameを親要素とした場合に、checkbutton Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.checkbutton.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        getCheckbuttonButton = tk.Button(frame, text="Boolean取得", width=15, command=self.getCheckbutton)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        getCheckbuttonButton.pack(side=tk.LEFT)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        setCheckbuttonButton = tk.Button(frame, text="Boolean設定", width=15, command=self.setCheckbutton)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        setCheckbuttonButton.pack(side=tk.LEFT)

    # IntVar説明用に構成される関数
    def configForIntVar(self, frame):
        # IntVarを利用して、entry Widgetで扱う数値情報を変数として扱う。
        # 初期化として、0を格納する。
        self.entryTextVariableForIntVar = tk.IntVar(value=0)

        # Frameを親要素として、entry Widgetを作成する。
        # textvariable : 数値情報を扱う変数を代入する。
        # Entryについて : https://kuroro.blog/python/PUZp77YFxrXvMCjpZbUg/
        self.entryForIntVar = tk.Entry(frame, textvariable=self.entryTextVariableForIntVar)

        # Frameを親要素とした場合に、entry Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.entryForIntVar.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        getEntryIntButton = tk.Button(frame, text="数値取得", width=15, command=self.getEntryInt)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        getEntryIntButton.pack(side=tk.LEFT)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        setEntryIntButton = tk.Button(frame, text="数値設定", width=15, command=self.setEntryInt)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        setEntryIntButton.pack(side=tk.LEFT)

    # StringVar説明用に構成される関数
    def configForStringVar(self, frame):
        # StringVarを利用して、label Widgetで扱うテキスト情報を変数として扱う。
        # 初期化として、testの文字列を格納する。
        self.labelTextVariable = tk.StringVar(value="test")

        # Frameを親要素として、label Widgetを作成する。
        # textvariable : テキスト情報を扱う変数を代入する。
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        self.label = tk.Label(frame, textvariable=self.labelTextVariable)
        # text optionを変更する場合
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        # self.label = tk.Label(frame, text='test')

        # Frameを親要素とした場合に、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.label.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        getLabelTextButton = tk.Button(frame, text="テキスト取得", width=15, command=self.getLabelText)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        getLabelTextButton.pack(side=tk.LEFT)

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # width : ボタンの幅設定
        # command : ボタンをクリックした場合に、実行する関数を設定する。
        # buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        setLabelTextButton = tk.Button(frame, text="テキスト設定", width=15, command=self.setLabelText)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        setLabelTextButton.pack(side=tk.LEFT)

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # StringVar説明用
        # self.configForStringVar(frame)

        # # IntVar説明用
        # self.configForIntVar(frame)

        # # DoubleVar説明用
        # self.configForDoubleVar(frame)

        # BooleanVar説明用
        self.configForBooleanVar(frame)

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
