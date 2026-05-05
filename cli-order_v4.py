menu = {
    "咖啡": 50,
    "蛋糕": 80,
    "紅茶": 30
}

order_dict = {}

# 刪除函式
def delete_item(order_dict , name):
    if name in order_dict:
        del order_dict[name]
    else:
        print("查無此商品")

# 更改函式
def update_item(order_dict , name , count):
    if name in order_dict:
        order_dict[name] = count
    else:
        print("查無此商品")

# 新增函式
def add_item(order_dict , menu , name , count):
    if name not in menu:
        print("查無此商品")
        return

    if name in order_dict:
        order_dict[name] += count
    else:
        order_dict[name] = count
    
# 訂單、菜單函式
def checkout(order_dict , menu):
    total = 0
    for name , count in order_dict.items():
        subtotal = menu[name] * count
        print(f"{name} x {count} = {subtotal}")
        total += subtotal
    print(f"總金額是: {total}")


# 輸入
while True:
    ordering = input("請輸入指令: ")

    if ordering == "結束":
        break

    parts = ordering.split()
    command = parts[0]



    # 刪除
    if command == "刪除":

        if len(parts) != 2:
            print("輸入格式錯誤，請輸入: 刪除 商品 ")
            continue

        name = parts[1]
        delete_item(order_dict , name)
    

    # 更改
    elif command == "更改":

        if len(parts) != 3:
            print("輸入格式錯誤，請輸入: 更改 商品 數量")
            continue 

        name = parts[1]
        count = parts[2]

        try:
            count = int(parts[2])
            if count <= 0:
                print("請輸入正整數")
                continue
        except ValueError:
            print("請輸入正整數")
            continue

        update_item(order_dict , name , count)

    # 累加、新增
    else:
        if len(parts) != 2:
            print("輸入格式錯誤，請輸入: 商品 數量 ")
            continue

        name = parts[0]
        try:
            count = int(parts[1])
            if count <= 0:
                print("請輸入正整數")
                continue
        except ValueError:
            print("請輸入正整數")
            continue

        
        add_item(order_dict , menu , name , count)


# 明細、計算金額
checkout(order_dict , menu)
