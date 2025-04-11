from turtle import *
screensize(3000, 3000)
hideturtle()
color('red')
speed(10000)
begin_fill()
left(90)
k = 40
pd()

for i in range(2):
    fd(27*k)
    rt(90)
    fd(8*k)
    rt(90)
end_fill()
pu()
fd(4*k)
rt(90)
fd(2*k)
lt(90)

begin_fill()
pd()
for i in range(2):
    fd(17*k)
    rt(90)
    fd(7*k)
    rt(90)
end_fill()
pu()
canvas = getcanvas()
tracer(0)
wk = 0
for x in range(-100*k, 100*k, k):
    for y in range(-100*k, 100*k, k):
        if canvas.find_overlapping(x,y,x,y) != ():
            wk=wk+1
            goto(x,-y)
            dot(5, 'blue')
print(wk)

done()
exit()