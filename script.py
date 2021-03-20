print("test")
print(7)
print(9 + 3)
print("9 + 3")

print(9 / 2) # 4.5(小数点で出力される)
print(7 * 5)
print(5 % 2)

name = "にんじゃわんこ"
print(name)
number = 7
print(number)


apple_price = 200
apple_count = 8
total_price = apple_price * apple_count
print(total_price)


money = 2000
print(money)
money = money + 5000
print(money)


my_name = "にんじゃ"
print("私は" + my_name + "です")


age = 24
print("私は" + str(age) + "歳です")
count = "5"
print(int(count) + 1)


x = 7 * 10
y = 5 * 6
if (x == 70):
  print("xは70です")
if (y != 40):
  print("yは40ではありません")


x = 10
if x > 30:
  print("xは30より大きいです")

money = 500
apple_price = 200
if money >= apple_price:
  print("りんごを買うことができます")
else: # lesson12
  print("お金が足りません") # lesson12

# lesson13
money = 100
apple_price = 100
if money >= apple_price:
  print("りんごを買うことができます")
elif money == apple_price:
  print("りんごを買うことができますが所持金が0になります")
else:
  print("お金が足りません")


x = 20
if 10 <= x <= 30:
  print("xは10以上30以下です")

y = 60
if 10 > y or y > 30:
  print("yは10未満または30より大きいです")

z = 55
if not(z == 77):
  print("zは77ではありません")


apple_price = 200
count = 5
total_price = apple_price * count
print("購入するりんごの個数は" + str(count) + "個です")
print("支払金額は" + str(total_price) + "円です")


apple_price = 200
input_count = input("購入するりんごの個数を入力してください：")
count = int(input_count)
total_price = apple_price * count

print("購入するりんごの個数は" + str(count) + "個です")
print("支払金額は" + str(total_price) + "円です")


apple_price = 200
count = 5
total_price = apple_price * count
print("購入するりんごの個数は" + str(count) + "個です")
print("支払金額は" + str(total_price) + "円です")


apple_price = 200
money = 1000
input_count = input("購入するりんごの個数を入力してください：")
count = int(input_count)
total_price = apple_price * count

print("購入するりんごの個数は" + str(count) + "個です")
print("支払金額は" + str(total_price) + "円です")

if money > total_price:
  print("りんごを" + str(count) + "個買いました")
  print("残高は" + str(money) + "円です")
elif money == total_price:
  print("りんごを" + str(count) + "個買いました")
  print("財布が空になりました")
else:
  print("お金が足りません")
  print("りんごを買えませんでした")