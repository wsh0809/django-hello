import tkinter
from time import sleep
from threading import Thread
from psutil import net_io_counters
from PIL import Image, ImageTk, ImageDraw
from bspider import get_prices

# 椭圆形窗口的宽度和高度
width, height = 320, 160
# 创建有用程序主窗口，设置初始大小和位置
root = tkinter.Tk()
# 注意，宽度和高度之间是小写字母x，不是乘号符号
root.geometry(f'{width}x{height}+1300+650')
# 两个方向都不允许修改大小
root.resizable(False, False)
# 不显示标题栏
root.overrideredirect(True)
# 设置白色透明度，这样子图片中所有的白色区域都被认为是透明的了
root.attributes('-transparentcolor', 'white')
# 顶层显示，不被其他窗口遮挡
root.attributes('-topmost', True)
# 标签组件的背景图片，第四个元素表示透明度
image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)
# 在图片上填充一个椭圆形
draw.ellipse((0, 0, width, height), fill=(200, 200, 200, 0))
image_tk = ImageTk.PhotoImage(image)
# 创建标签组件，设置字体，子号，对齐方式和背景图片
lbTraffic = tkinter.Label(root, text='', font=('楷体', 12), foreground='#ffa000', bg='#ffffff', compound=tkinter.CENTER,
                          anchor='center', image=image_tk)
lbTraffic.place(x=0, y=0, width=width, height=height)
# 鼠标左键按下时设置为False表示可以移动窗口
canMove = tkinter.BooleanVar(root, False)
# 记录鼠标左键按下的位置
X = tkinter.IntVar(root, value=0)
Y = tkinter.IntVar(root, value=0)

# 鼠标左键抬起时的事件处理函数
def onLeftButtonDown(event):
    X.set(event.x)
    Y.set(event.y)
    canMove.set(True)
root.bind('<Button-1>', onLeftButtonDown)

# 鼠标移动时的事件处理函数
def onLeftButtonMove(event):
    if not canMove.get():
        return
    newX = root.winfo_x() + (event.x-X.get())
    newY = root.winfo_y() + (event.y-Y.get())
    g = f'{width}x{height}+{newX}+{newY}'
    root.geometry(g)
root.bind('<B1-Motion>', onLeftButtonMove)

# 鼠标右键抬起时的事件处理函数
def onRightButtonUp(event):
    # 停止刷新网速显示器
    running.set(False)
    # 关闭主程序窗口
    root.destroy()
root.bind('<ButtonRelease-3>', onRightButtonUp)

def compute_traffic():
    # traffic_io = net_io_counters()[:2]
    while running.get():
        # traffic_ioNew = net_io_counters()[:2]
        msgs = get_prices()
        lbTraffic['text'] = '\n'.join(msgs)
        sleep(60)
        # traffic_io = traffic_ioNew
running = tkinter.BooleanVar(root, True)
# 创建并启动子线程，更新窗口上的流量数据
Thread(target=compute_traffic).start()

root.mainloop()
