# coding=utf-8
import os

import tkinter as tk;
from tkinter import *
from tkinter import filedialog
# from PIL import Image



root = tk.Tk()
# 这里四个参数分别为：宽、高、左、上
root.geometry("500x300+750+200")
root.title('saveWallPaper')
dirPath = StringVar()

def opendir():
    # os.environ['HOME']
    # os.path.expandvars('$HOME')
    dir = filedialog.askdirectory(initialdir=(os.path.expanduser('~')))
    if (dir != ''):
        dirPath.set(dir)



Label(root,text='保存路径:').grid(row=0,column=0)

# 文本框用来显示文件路径
Entry(root, textvariable=dirPath).grid(row=0,column=1)

tk.Button(root,text='选择',width=5,command=opendir).grid(row=0,column=2,padx=5,pady=5)

root.mainloop()


    

# if __name__ == "__main__":
#     main_panel()