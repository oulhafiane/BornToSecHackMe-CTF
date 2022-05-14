import re
from turtle import *
pos = -400;

def draw_avance(val):
    forward(int(val))

def draw_tourne(guid, val):
    if (guid == "droite"):
        right(int(val))
    else:
        left(int(val))

def draw_recule(val):
    backward(int(val))

def get_ins(inc):
    global pos
    Tourne = re.findall(r'^Tourne ([a-zA-Z]+) de ([0-9]+) degrees$',inc)
    Avance = re.findall(r'^Avance ([0-9]+) spaces$',inc)
    Recule = re.findall(r'^Recule ([0-9]+) spaces$',inc)

    if len(Tourne) > 0 :
        draw_tourne(Tourne[0][0], Tourne[0][1])
    elif len(Avance) > 0 :
        draw_avance(Avance[0])
    elif len(Recule) > 0 :
        draw_recule(Recule[0])
    else :
        color('white', "white")
        if (pos == -300):
            setpos(pos, 200)
            pos += 100
            right(90)
        elif (pos == -200):
            setpos(pos, 200)
            pos += 200
            left(90)
        elif (pos == 0):
            setpos(pos, 200)
            pos += 200
            left(90)
        elif (pos == 200):
            setpos(pos, 300)
            pos += 200
            left(90)
        color('red', "white")


f = open("turtle.txt", "r")
text = f.readline()
color('white', "white")
setpos(pos, 400)
pos += 100
color('red', "white")
begin_fill()
speed(0)
left(90)
while text:
    get_ins(text)
    text = f.readline()
end_fill()
done()