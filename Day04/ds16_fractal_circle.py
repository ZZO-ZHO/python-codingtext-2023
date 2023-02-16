# 프랙탈 원 그리기
import turtle

turtle.setup(width=600, height=600)
t = turtle.Turtle()
t.shape('turtle')

c = t.clone()
c.color('green')

for i in range(4,10):
    c.color('red')
    c.circle(i*10)
    c.color('green')
    c.circle(i*-10)

turtle.mainloop()
