# C:\Users\qzz\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
# -*- coding: utf-8 -*-
import os, os.path
import shutil
import getpass
# coding=utf-8
import tkinter as tk;
from tkinter import *
from tkinter import filedialog





def move_file(wallPaper_path, save_path):  # 复制文件

    filelist = os.listdir(wallPaper_path)
    if os.path.exists(save_path):

        for file in filelist:
            Oldfile = os.path.join(wallPaper_path, file);  # 原来的文件路径
            desfile=os.path.join(save_path, file+'.jpg');
            if os.path.exists(desfile):
                print("wall paper already exist!")
            else:
                shutil.copy(Oldfile, save_path)
                print ('.....move_file....done')
    else:
        os.mkdir(save_path)
        for files in filelist:
            Olddir = os.path.join(wallPaper_path, files);  # 原来的文件路径
            shutil.copy(Olddir, save_path)
        print ('....create new folder and move_file.... done')

def rename_file(save_path):  # 重命名文件
    filelist = os.listdir(save_path)
    for file in filelist:
        filename = os.path.splitext(file)[0];  # 文件名
        print(filename)
        oldfile=os.path.join(save_path,file) # 需要更改的文件路径
        print(oldfile)
        # filetype=os.path.splitext(files)[1];#文件扩展名
        newfile = os.path.join(save_path, filename + ".jpg");  # 新的文件路径
        print(newfile)
        if os.path.exists(newfile):
            print("this image already exits!")
        else:
            os.rename(oldfile, newfile);  # 重命名
            print newfile;
    print ('.............rename_file............ done')

def opendir():
    # os.environ['HOME']
    # os.path.expandvars('$HOME')
    dir = filedialog.askdirectory(initialdir=(os.path.expanduser('~')))
    if (dir != ''):
        dirPath.set(dir)
        return dir

if __name__ == "__main__":
    path_head ="C:\Users\\"
    path_tail='\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets'
    user = getpass.getuser()
    print("system username:" + path_head+user+path_tail)
    wallpath =path_head+user+path_tail
    root = tk.Tk()
    # 这里四个参数分别为：宽、高、左、上
    root.geometry("500x300+750+200")
    root.title('saveWallPaper')
    dirPath = StringVar()
    Label(root, text='保存路径:').grid(row=0, column=0)
    # 文本框用来显示文件路径
    Entry(root, textvariable=dirPath).grid(row=0, column=1)
    tk.Button(root, text='选择', width=5, command=opendir).grid(row=0, column=2, padx=5, pady=5)
    save_path = opendir()
    move_file(wallpath, save_path);
    rename_file(save_path);
    root.mainloop()