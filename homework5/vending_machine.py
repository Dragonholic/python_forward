print("투입한돈 : ", end="")
input_mon = int(input())
print("물건값 : ", end="")
price = int(input())

change = input_mon - price
print("거스름돈 : ",change)

o_back_won = int(change / 500)
back_won = int(change % 500 / 100)

print("500원 동전의 개수 : ",o_back_won)
print("100원 동전의 개수 : ",back_won)