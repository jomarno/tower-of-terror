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

enemies = ['SKELETON', 'GHOST', 'HEADLESS AXEMAN']
comment = 'GOOD LUCK'
room_global = 0
hour = 9; minutes = int(random()*10) + 10
pulse = 50

while(True):
    clear_screen()
    print(''); print('')
    print('TOWER OF TERROR')
    print('===============')
    print(''); print(comment)
    comment = ''
    floor = room_global//5
    room_in_floor = room_global - floor*5 + 1
    print(''); print('YOU ARE ON')

    if floor == 0: print('THE GROUND FLOOR')
    if floor == 6: print('THE TOP FLOOR')
    if floor>0 and floor<6: print('FLOOR ', floor)

    print('IN ROOM_global ', room_in_floor)
    print(''); print('THE TIME IS ', hour,'.', minutes,' PM')
    print(''); print('YOUR PULSE RATE IS ', pulse)
    flag = 0

    if room_global == 30:
        print('WELL DONE ')
        break
    
    trap = int(random()*9 + 1)

    if random() > 0.6:
        ty = int(random()*3)
        enemy = enemies[ty]
        shock = int(random()*5) + floor + ty*2
        print(''); print('AHEAD YOU SEE A ', enemy)
        flag = 1

    print(''); print('RETREAT OR GO ON (R/G)')
    action = input()

    # 250 IF I$<>"G" AND I$<>"R" THEN GOTO 240

    if action == 'g':
        if flag == 1:
            pulse = pulse + shock*2
            comment = 'AAAHHHH!'
        pulse = pulse - 1
        room_global = room_global + 1

    if action == 'r':
        room_global = room_global - 1
        pulse = pulse - 5

    if room_global == - 1: room_global = 0

    minutes = minutes + int(random()*3 +1)
    
    if minutes > 59:
        minutes = minutes -60
        hour = hour +1

    if hour == 12:
        print("IT'S MIDNIGHT!")
        print('TOO LATE!')
        break

    if pulse > 150:
        print('YOU HAVE GONE MAD AND')
        print('LEAPT FROM A WINDOW!')
        break

    if pulse < 40: pulse = 40

    if floor==trap and random()>0.5:
        comment = 'YOU FELL THROUGH A TRAP DOOR!'
        room_global = room_global - 5
        pulse = pulse + 10
