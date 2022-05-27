from web3 import Web3
from web3.contract import Contract
import tkinter
from threading import Thread
from psutil import net_io_counters
from PIL import Image, ImageTk, ImageDraw
from time import sleep

class Address:
    public_key = ""
    __private_key = ""

    def __init__(self, address, private_key):
        self.public_key = Web3.toChecksumAddress(address)
        self.__private_key = private_key

    def get_private_key(self):
        return self.__private_key

    def get_address(self):
        return self.public_key


class Net:
    test_net = "https://bsc-dataseed.binance.org/"
    main_net = "https://bsc-dataseed.binance.org/"


class NodeClient:
    def create(url, proxy):
        provider = Web3.HTTPProvider(url, request_kwargs={"proxies": {'https': proxy, 'http': proxy}})
        web3 = Web3(provider)
        return web3


class Kit:

    def __init__(self, web3: Web3, address: Address):
        self.web3 = web3
        self.address = address

    def get_web3(self):
        return self.web3

    def get_address(self):
        return self.address


class SmartContract:

    def __init__(self, _contract: Contract):
        self.contract = _contract

    def get_balance(self, address):
        return self.contract.functions.balanceOf(address).call()


class CustomWindow:

    def __init__(self, callback):
        # 回调显示的内容
        self.callback = callback
        # 椭圆形窗口的宽度和高度
        self.width, self.height = 320, 160
        # 创建有用程序主窗口，设置初始大小和位置
        self.root = tkinter.Tk()
        # 注意，宽度和高度之间是小写字母x，不是乘号符号
        self.root.geometry(f'{self.width}x{self.height}+1300+650')
        # 两个方向都不允许修改大小
        self.root.resizable(False, False)
        # 不显示标题栏
        self.root.overrideredirect(True)
        # 设置白色透明度，这样子图片中所有的白色区域都被认为是透明的了
        self.root.attributes('-transparentcolor', 'white')
        # 顶层显示，不被其他窗口遮挡
        self.root.attributes('-topmost', True)
        # 标签组件的背景图片，第四个元素表示透明度
        self.image = Image.new('RGBA', (self.width, self.height), (255, 255, 255, 0))
        self.draw = ImageDraw.Draw(self.image)
        # 在图片上填充一个椭圆形
        self.draw.ellipse((0, 0, self.width, self.height), fill=(200, 200, 200, 0))
        self.image_tk = ImageTk.PhotoImage(self.image)
        # 创建标签组件，设置字体，子号，对齐方式和背景图片
        self.lbTraffic = tkinter.Label(self.root, text='', font=('楷体', 12), foreground='#ffa000', bg='#ffffff',
                                  compound=tkinter.CENTER,
                                  anchor='center', image=self.image_tk)
        self.lbTraffic.place(x=0, y=0, width=self.width, height=self.height)
        # 鼠标左键按下时设置为False表示可以移动窗口
        self.canMove = tkinter.BooleanVar(self.root, False)
        # 记录鼠标左键按下的位置
        self.X = tkinter.IntVar(self.root, value=0)
        self.Y = tkinter.IntVar(self.root, value=0)
        self.root.bind('<Button-1>', self.onLeftButtonDown)
        self.root.bind('<B1-Motion>', self.onLeftButtonMove)
        self.root.bind('<ButtonRelease-3>', self.onRightButtonUp)

        self.running = tkinter.BooleanVar(self.root, True)
        # 创建并启动子线程，更新窗口上的流量数据
        Thread(target=self.show_content).start()
        self.root.mainloop()

    # 鼠标左键抬起时的事件处理函数
    def onLeftButtonDown(self, event):
        self.X.set(event.x)
        self.Y.set(event.y)
        self.canMove.set(True)

    # 鼠标移动时的事件处理函数
    def onLeftButtonMove(self, event):
        if not self.canMove.get():
            return
        newX = self.root.winfo_x() + (event.x - self.X.get())
        newY = self.root.winfo_y() + (event.y - self.Y.get())
        g = f'{self.width}x{self.height}+{newX}+{newY}'
        self.root.geometry(g)

    # 鼠标右键抬起时的事件处理函数
    def onRightButtonUp(self, event):
        # 停止数据脚本
        self.running.set(False)
        # 关闭主程序窗口
        self.root.destroy()

    def show_content(self):
        while self.running.get():
            msg = self.callback()
            self.lbTraffic['text'] = msg
            sleep(30)

