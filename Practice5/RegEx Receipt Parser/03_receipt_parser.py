import re
with open("raw.txt", "r", encoding='utf-8') as file:
    text = file.read()
names = re.findall("ИТОГО\:\n(.+)", text)
for i in names:
    print(i)