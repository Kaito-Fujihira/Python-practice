#lesson2-2
fruits = ["apple", "banana", "orange"]
print(fruits[0])
print("好きな果物は" + fruits[2] + "です")

#lesson2-3
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits)
fruits[0] = "cherry"
print(fruits[0])


#lesson2-4
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
  print("好きな果物は" + fruit + "です")


#lesson2-5
fruits = {"apple": "りんご", "banana": "バナナ"}
print(fruits["banana"])
print("appleは" + fruits["apple"] + "という意味です")


#lesson2-6
fruits = {"apple": 100, "banana": 200, "orange": 400}
fruits["banana"] = 300
fruits["grape"] = 500
print(fruits)


#leesson2-7
fruits = {"apple": "りんご", "banana": "バナナ", "grape": "ぶどう"}
for fruit_key in fruits:
  print(fruit_key + "は" + fruits[fruit_key] + "という意味です")