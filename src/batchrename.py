#/usr/bin/python
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import *
from os import *
def findSubStr(substr, str, i):
    count = 0
    while i > 0:
        index = str.find(substr)
        if index == -1:
            return -1
        else:
            str = str[index+1:]
            i -= 1
            count = count + index + 1
    return count - 1

def getPath():
    path_=path.normpath(askdirectory())
    path1.set(str(path_)+'\\')



def renamefile(drectory):
    if drectory=='.\\' or drectory=='':
        showerror('错误提示','文件路径不正确，请重新选择')
        return
    for file in listdir(drectory):
        catdir = path.join(path.dirname(drectory), file)
        if path.isdir(catdir):
            continue
        # 文件名
        filename =path.splitext(file)[0]
        # 文件扩展
        filetype =path.splitext(file)[1]
        olddir=path.join(path.dirname(drectory), file)
        newfiledir=path.join(path.dirname(drectory),filename[0:findSubStr(filename, '_', 5)]+filetype)
        # olddir=olddir.replace('\\', '/')
        # newfiledir = newfiledir.replace('\\', '/')
        # renames(olddir,newfiledir)
    showinfo('结果','批量修改成功')
root = Tk()
path1 =  StringVar()
Label(root,text = '目标路径:').grid(row = 0,column=0,padx=10,pady=10)
Entry(root,textvariable = path1).grid(row =0,column=1)
Button(root,text='路径选择',command = getPath).grid(row=0,column=2)
Button(root,text='批量重命名',command = lambda: renamefile(path1.get())).grid(row=1,column=1,padx=10,pady=10)
# 设置窗口位置和大小
root.title('批量重命名脚本')
# 设置窗口大小并且居中显示
# 屏幕宽度以及屏幕高度
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
dialog_width = 300
dialog_height = 100
# 前两个参数是窗口的大小，后面两个参数是窗口的位置
root.geometry("%dx%d+%d+%d" % (dialog_width, dialog_height, (screenwidth-dialog_width)/2, (screenheight-dialog_height)/2))
root.grid
root.mainloop()
