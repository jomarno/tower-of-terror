#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:34:45 2021

@author: vanilla
"""
from random import random
from os import system

def clear_screen():
    system('clear')

gdollar = ['SKELETON', 'GHOST', 'HEADLESS AXEMAN']

rdollar = 'GOOD LUCK'
rm = 0
h = 9; m = int(random()*10) +10
p = 50

clear_screen(); print(''); print('')
print('TOWER OF TERROR')
print('===============')
print(''); print(rdollar)
rdollar = ''; fl = rm//5
r = rm - fl*5 +1
print(''); print('YOU ARE ON')
if fl==0: print('THE GROUND FLOOR')
if fl==6: print('THE TOP FLOOR')
if fl>0 and fl<6: print('FLOOR ', fl)
print('IN ROOM ', r)
print(''); print('THE TIME IS ', h,'.', m,' PM')
print(''); print('YOUR PULSE RATE IS ', p)
gf = 0
# 200 IF RM=30 THEN GOTO 350
tr = int(random()*9 +1)
if random() > 0.6:
    ty = int(random()*3)
    wdollar = gdollar[ty]
    s = int(random()*5) +fl +ty*2
    print(''); print('AHEAD YOU SEE A ', wdollar)
    gf = 1

print(''); print('RETREAT OR GO ON (R/G)')
idollar = input()
# 250 IF I$<>"G" AND I$<>"R" THEN GOTO 240
if idollar == 'g':
    if gf == 1:
        p = p + s*2
        rdollar = 'AAAHHHH!'
    p = p -1
    rm = rm +1

if idollar == 'r':
    rm = rm -1
    p = p -5

if rm = -1: rm = 0
m = m + int(random()*3 +1)
if m > 59:
    m = m -60
    h = h +1

# 300 IF H=12 THEN GOTO 360
# 310 IF P>150 THEN GOTO 380
if p < 40: p = 40
if fl==tr and random()>0.5:
    rdollar = 'YOU FELL THROUGH A TRAP DOOR!'
    rm = rm -5
    p = p +10

# GOTO 60
