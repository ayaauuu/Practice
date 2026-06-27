import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()



prices = re.findall(r"\n(\d[\d ]*,\d{2})\nСтоимость", text)

prices = [float(price.replace(" ", "").replace(",", ".")) for price in prices]



products = re.findall(r"\d+\.\n(.+?)\n\d+,\d+\s+x", text)


total = re.search(r"ИТОГО:\n([\d ]*,\d{2})", text)

if total:
    total = total.group(1)



datetime = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})", text)

if datetime:
    datetime = datetime.group(1)



payment = re.search(r"(Банковская карта|Наличные)", text)

if payment:
    payment = payment.group(1)



result = {
    "Products": products,
    "Prices": prices,
    "Total": total,
    "DateTime": datetime,
    "Payment": payment
}

print(json.dumps(result, ensure_ascii=False, indent=4))
