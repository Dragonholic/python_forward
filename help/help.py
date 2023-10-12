import turtle
t = turtle.Turtle()


#그래프 xy축 그리는 부분
turtle.up()
turtle.back(300)
turtle.down()
turtle.forward(600)
turtle.stamp()
turtle.back(300)
turtle.left(90)
turtle.up()
turtle.back(300)
turtle.down()
turtle.forward(600)
turtle.stamp()
turtle.home()
#그래프 축 끝


#변수 값 선언
a = 2
b = -4
a = int(a)
b = int(b)
x = -300
dx = 1
y = 0
#변수값선언 끝

#그래프 자체 그림
t.up()                          # 여기가 tutle. 이아니라 t. 으로 써야하는 곳
t.pencolor("red")
t.down()
# 위에 그래프 xy축 그리는 거랑 그래프 그리는 거랑 분리 해야해서 그럼



while x <= 300 :
    y=(a*x+b)
    t.goto(x,y)
    x = x + dx
# 그래프 그리는 거