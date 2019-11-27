# 协程： 单线程 + 异步IO
# 因为是单线程所以不用加锁

import time
import tkinter
import tkinter.messagebox
from threading import Thread

def main():
    class DownloadTaskThread(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成！')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state = tkinter.DISABLED)
        # 通过daemon参数将线程设置成守护线程（主程序退出就不再保留执行)
        # 在线程中处理耗时间的下载任务
        DownloadTaskThread(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者')

    top=tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button2 = tkinter.Button(panel, text='关于', command = show_about)
    button1.pack(side='left')
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == '__main__':
    main()