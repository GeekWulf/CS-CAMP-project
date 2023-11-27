#------------------------------------------ประกาศ lib ---------------------------------------#
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
#------------------------------------------ประกาศ lib ---------------------------------------#

#------------------------------------------กำหนดหน้าต่าง---------------------------------------#
root = tk.Tk()
root.title('White Board')
root.geometry('900x900')
root.configure(bg='#f2f3f5')
root.resizable(True,True)  
#------------------------------------------กำหนดหน้าต่าง---------------------------------------#

#------------------------------------------set ตำเเหน่งเริ่มต้น ---------------------------------------#
current_x = 0
current_y = 0
color = 'black'
#------------------------------------------set ตำเเหน่งเริ่มต้น ---------------------------------------#

#------------------------------------------set cersor ล่าสุด ---------------------------------------#
def locate_xy(work):
    global current_x,current_y
    current_x = work.x
    current_y = work.y
#------------------------------------------set cersor ล่าสุด---------------------------------------#

#------------------------------------------วาด---------------------------------------#
def addline(work):
    #canvas.create_line((current_x, current_y, work.x, work.y), width=get_current_value(),fill=color, capstyle=ROUND, smooth=TRUE)
    global current_x,current_y
    canvas.create_line((current_x,current_y, work.x, work.y), width=5,fill=color,capstyle=ROUND, smooth=TRUE) #width = กำหนดความหนาของปากกา  
    current_x, current_y = work.x, work.y
#------------------------------------------วาด---------------------------------------#

#------------------------------------------เปลี่ยนสีปากกา---------------------------------------#
def show_color(new_color):
    global color
    color = new_color
#------------------------------------------เปลี่ยนสีปากกา---------------------------------------#

#------------------------------------------icon---------------------------------------#
image_icon = PhotoImage(file='pen.png')
root.iconphoto(False,image_icon)
#------------------------------------------icon---------------------------------------#

#------------------------------------------สร้างกระดาษ---------------------------------------#
canvas = Canvas(root,width=1980,height=1600,background='white',cursor='hand2')  #backgrond
canvas.place(x=10,y=10)
#------------------------------------------สร้างกระดาษ---------------------------------------#

#------------------------------------------รับค่าจาก mouse---------------------------------------#
canvas.bind('<Button-1>')
canvas.bind('<B1-Motion>')
#------------------------------------------รับค่าจาก mouse---------------------------------------#

#------------------------------------------สร้างช่องเก็บสี---------------------------------------#
colors = Canvas(root,bg='#ffffff',width=40,height=330,bd=0) #color section
colors.place(x=10,y=20)
#------------------------------------------สร้างช่องเก็บสี---------------------------------------#

eraser = PhotoImage(file='eraser.png')  #ภาพยางลบ

#------------------------------------------สร้างช่องเปลี่ยนสี---------------------------------------#
def display_pallete():
    id = colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('black'))

    id = colors.create_rectangle((10,40,30,60),fill='gray')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('gray'))

    id = colors.create_rectangle((10,70,30,90),fill='brown4')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('brown4'))

    id = colors.create_rectangle((10,100,30,120),fill='red')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('red'))

    id = colors.create_rectangle((10,130,30,150),fill='orange')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('orange'))

    id = colors.create_rectangle((10,160,30,180),fill='yellow')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('yellow'))

    id = colors.create_rectangle((10,190,30,210),fill='green')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('green'))

    id = colors.create_rectangle((10,220,30,240),fill='blue')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('blue'))
    
    id = colors.create_rectangle((10,250,30,270),fill='purple')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('purple'))

    id = colors.create_image(10, 300, anchor=(NW), image=eraser)    #x = 10, y = 300
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('white'))

display_pallete()
#------------------------------------------สร้างช่องเปลี่ยนสี---------------------------------------#

#------------------------------------------วาด---------------------------------------#
canvas.bind('<Button-1>', locate_xy) 
canvas.bind('<B1-Motion>', addline)
#------------------------------------------วาด---------------------------------------#

root.mainloop() #run project
