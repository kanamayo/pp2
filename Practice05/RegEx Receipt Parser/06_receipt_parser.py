import re
import json
with open("raw.txt", "r", encoding='utf-8') as file:
    text = file.read()
prices = re.findall("Стоимость\n(\d{1,},\d{2})", text)
time = re.findall("Время\: (.+)", text)
products = re.findall("\d+\.\n(.+)", text)
total = re.findall("ИТОГО\:\n(.+)", text)
payment = re.findall("Банковская карта|Наличные", text)
js = {
    "products": products,
    "prices": prices,
    "total": total,
    "time": time,
    "payment": payment,
}
print(json.dumps(js, indent=4, ensure_ascii=False))
# for i in js:
    # print(i)