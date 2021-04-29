#! /usr/bin/env python3
#  -*-coding:utf-8 -*-
"""
Daily code warm up using python turtle by following and read python
code blog posts.
ref: https://michael0x2a.com/blog/turtle-examples
"""
import turtle

painter = turtle.Turtle()

painter.pencolor('green')

for i in range(50):
    painter.forward(50.5)
    painter.left(125)

painter.pencolor('gray')

for i in range(50):
    painter.forward(100)
    painter.left(125)

turtle.done()