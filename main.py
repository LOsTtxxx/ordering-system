total = 0
order_dict = {}

menu = {
    "咖啡": 50,
    "蛋糕": 80,
    "紅茶": 30
}


while True:
    ordering = input("請輸入商品 + 數量: ")

    if ordering == "結束":
        break

    name , count = ordering.split()
    count = int(count)

    if name not in menu:
        print("此商品不存在")
        continue

    if name in order_dict:
        order_dict[name] += count
    else:
        order_dict[name] = count
    
for name , count in order_dict.items():
    subtotal = menu[name] * count 
    print(f"{name} x {count } = {subtotal}")
    total += subtotal
print(f"總金額是: {total}")








