#! /usr/bin/env pyhton3
# -*- coding:utf-8 -*-
""" official python docs
turtle star.
"""
from turtle import (
    color,
    begin_fill,
    forward,
    left,
    pos,
    end_fill,
    done
)
color('red', 'yellow')
begin_fill()
while True:
    forward(300)
    left(270)
    if abs(pos()) < 1:
        break
end_fill()
done()
