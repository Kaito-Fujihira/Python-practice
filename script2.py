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