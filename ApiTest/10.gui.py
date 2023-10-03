import tkinter


top = tkinter.Tk()
top.title = "this is a test tile"

# Define a function to be called when the button is clicked
def button_click():
    label.config(text="Button Clicked!")
# Create a button widget
button = tkinter.Button(top, text="Click Me!", command=button_click)
# Create a label widget to display a message
label = tkinter.Label(top, text="")
# Pack the button and label widgets
button.pack()
label.pack()



# 进入消息循环
top.mainloop()

#
#
# root = tkinter()                     # 创建窗口对象的背景色
#                                 # 创建两个列表
# li     = ['C','python','php','html','SQL','java']
# movie  = ['CSS','jQuery','Bootstrap']
# listb  = Listbox(root)          #  创建两个列表组件
# listb2 = Listbox(root)
# for item in li:                 # 第一个小部件插入数据
#     listb.insert(0,item)
#
# for item in movie:              # 第二个小部件插入数据
#     listb2.insert(0,item)
#
# listb.pack()                    # 将小部件放置到主窗口中
# listb2.pack()
# root.mainloop()                 # 进入消息循环





