# -*- coding: utf-8 -*-
# 这是一个简单的 Hello World 程序
# 目的：在控制台打印问候语
# Name:Reach 
#----------------------------------------------------------------------------------------------

import turtle

print("你好，世界！")  # 使用中文输出
print("Hello World")  # 使用英文输出

# 设置画布
screen = turtle.Screen()
screen.title("Hello World 绘图")
screen.bgcolor("white")

# 创建画笔
pen = turtle.Turtle()
pen.pensize(2)
pen.color("blue")

# 绘制文字
pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.write("你好，世界！", font=("Arial", 16, "normal"))
pen.penup()
pen.goto(-100, -50)
pen.pendown()
pen.write("Hello World!", font=("Arial", 16, "normal"))

# 隐藏画笔
pen.hideturtle()

# 保持窗口显示
screen.mainloop()
