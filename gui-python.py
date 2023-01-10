from tkinter import *

class GUI(Frame):
    def __init__(self, master: Tk = None):
        super().__init__(master)
        self.master = master
        self.master.geometry('450x300')
        self.master.resizable(0, 0)
        self.master.title('Enter Script')

        # ボタンの配置
        button_to_func = {
            'Run': lambda: exec(self.text.get(1.0, END), globals()),
        }
        i = 0
        for button_str, func in button_to_func.items():
            button = Button(self.master, text = button_str, command = func)
            button.pack()
            button.place(x = 5 + 40 * i, y = 10)
            i += 1

        # テキストの配置
        self.text = Text(
            self.master,
            background = '#b0b0b0',
            width = 30,
            height = 20,
        )
        self.text.pack()
        self.text.place(x = 220, y = 10)

tk = Tk()
gui = GUI(master = tk)
gui.mainloop()