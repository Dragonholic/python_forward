# 커피가격 1000원계산
#202001606_고용운

americano_price = 2000
cafelatte_price = 3000
capuccin_price = 3500

total_cost = int(input("총 재료비용: "))
americano = int(input("아메리카노 판매 개수:"))
cafelatte = int(input("카페라때 판매 개수:"))
capuccino = int(input("카푸치노 판매 개수:"))

total = americano*americano_price + cafelatte*cafelatte_price + capuccino*capuccin_price
benefit = total_cost - total

print("총 매출은", total, "원 입니다.", "순이익은", benefit,"입니다.")