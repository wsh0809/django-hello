from tkinter import *

def on_resize(evt):
    tk.configure(width=evt.width, height=evt.height)
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR, outline=TRANSCOLOUR)

tk = Tk()
# tk.overrideredirect(True)
tk.geometry('500x400+500+150')
tk.title('will')
TRANSCOLOUR = 'gray'
tk.wm_attributes('-transparentcolor', TRANSCOLOUR)
canvas = Canvas(tk)
# canvas.configure(highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)
canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR, outline=TRANSCOLOUR)
tk.bind('<Configure>', on_resize)
tk.mainloop()
