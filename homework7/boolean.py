"""
x =100
y =1
print(x==y)
print(x != y)
print(x >y)
print(x <y)
print(x >=y)
print(x <=y)
print(False)
print(True)
print(1)
print(2)
if x>y :
    print("x가 더크다")
    print("첫조건")
else:
    print("y가 더크다")
    print("두조건")
"""


"""
score =int(input("성적입력 : "))

if score >= 60 :
    print("합격")
else :
    print("불합격")
    print("목표점수에 ", 60-score, "점올리면 합격입니다.")

if score%2 ==0:
    print("짝수입니다")
else:
    print("홀수 입니다.")
"""

"""
level = input("나이를 입력하시오: ")
level = int(level)

if level >29 :
    print("이 영화를 보실 수 있습니다.")

else:
    print("이 영화를 보실 수 없습니다.")
    print(29-level,"살 더 먹고 오심시오")
"""

"""
import turtle

pen = turtle.Pen()
t = turtle.Pen()
t.shape(name="turtle")

jungsu = turtle.textinput("정수는", "정수를입력하시오")

jungsu = int(jungsu)

pen.penup()
pen.goto(100,100)
pen.pendown()
pen.write("거북이가 여기로오면 양수 입니다.")



pen.penup()
pen.goto(100, 0)
pen.pendown()
pen.write("거북이가 여기로오면 0 입니다.")


pen.penup()
pen.goto(100, -100)
pen.pendown()
pen.write("거북이가 여기로오면 음수 입니다.")


if jungsu > 0 :

    t.goto(100,100)
if jungsu == 0 :

    t.goto(100, 0)

if jungsu < 0 :

    t.goto(100, -100)

turtle.exitonclick()

"""

"""
import turtle

t = turtle.Turtle()


while True:
    commend = input("명령을 입력하시오 : ")
    if commend == 'l' or commend == 'L' :
        t.left(90)
        t.forward(100)
    if commend == 'r' or commend == 'R' :
        t.right(90)
        t.forward(100)

"""

year = int(input("year : "))

if year%4 == 0 and year%100 !=0 or year%400 == 0 :
    print("윤년")
else:
    print("윤년 아님")
