#讀取檔案
products = []
with open ('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue
		name,price = line.strip().split(',')
		products.append([name, price])
print(products)
#輸入檔案
while True:
	name = input('請輸入名稱:')
	if name == 'q':
		break
	price = input('請輸入價格:')	
	products.append([name, price])
print(products) 
#印出商品
for p in products:
	print("名稱:", p[0], "價格:", p[1])
#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f: 
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')