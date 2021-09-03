# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 16:53:22 2021
@author: Sai Ma
"""

import turtle

turtle.colormode(255)

panel = turtle.Screen()

w = 750
h = 750

panel.setup(width = w, height = h)

image = "Bezos.gif"
panel.bgcolor("aquamarine")
panel.bgpic(image)

turtle.pensize(3)
turtle.begin_fill()
turtle.color("CadetBlue")
turtle.circle(45)
turtle.fillcolor("cyan")
turtle.end_fill()

turtle.up()
turtle.goto(150,-150)
turtle.down()
turtle.right(90)
turtle.fd(100)

turtle.up()
turtle.goto(85,85)
turtle.down()
turtle.pensize(3)
turtle.fd(20)
turtle.right(60)
turtle.fd(20)
turtle.right(60)
turtle.fd(20)
turtle.right(60)
turtle.fd(20)
turtle.right(60)
turtle.fd(20)
turtle.right(60)
turtle.fd(20)
turtle.right(60)

turtle.begin_fill()
turtle.up()
turtle.goto(100,200)
turtle.down()
turtle.color("chocolate")
turtle.pensize(6)
turtle.left(45)
turtle.fd(100)
turtle.right(120)
turtle.fd(200)
turtle.right(60)
turtle.fd(100)
turtle.right(120)
turtle.fd(200)
turtle.fillcolor("DarkSalmon")
turtle.end_fill()

turtle.up()
turtle.goto(-120,-30)
turtle.down()
turtle.pensize(3)
turtle.fd(100)
turtle.left(72)
turtle.fd(100)
turtle.left(72)
turtle.fd(100)
turtle.left(72)
turtle.fd(100)
turtle.left(72)
turtle.fd(100)

turtle.up()
turtle.goto(175,85)
turtle.fillcolor("CadetBlue1")
turtle.shape("square")
turtle.done()