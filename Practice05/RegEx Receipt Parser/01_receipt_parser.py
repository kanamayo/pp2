import re
with open("raw.txt", "r", encoding='utf-8') as file:
    text = file.read()
prices = re.findall("Стоимость\n(\d{1,},\d{2})", text)
for i in prices:
    print(i)
# print(prices)