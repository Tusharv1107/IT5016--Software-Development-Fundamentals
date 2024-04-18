# a = "Good Afternoon"
# b = input("What is your name?")
# a += b
# c = a + b
# print(a)
# print(c)

# f-string
website = "fun learning"
print (f"welcome to {website}")

words= ["We", "are", "learning", "python"]
joined = "  ".join(words)
print(joined)

print(joined.upper())
print(joined.upper())

basket = ["Banana", "apple", "kiwi"]
price = 5
text = "welcome to the grocery, everything is{} dollars"
print(text.format(price))

quantity = 6
discountable = 500

myorder = "I want {} peices of item under discount code of{} for {}dollars"
print(myorder.format(quantity, discountable, price))
total = price * quantity
print(f"total price: {total}")
