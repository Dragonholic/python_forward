print("몸무게를 kg 단위로 입력하시오 :",end="")
kg = float(input())
print("키를 미터단위로 입력하시오 :", end="")
m = float(input())

bmi = kg / (m**2)
print("당신의 BMI =", bmi)