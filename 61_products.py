products = []
while True:
	name = input('請輸入名稱:')
	if name == 'q':
		break
	price = input('請輸入價格:')	
	products.append([name, price])
print(products) 
for p in products:
	print("名稱:", p[0], "價格:", p[1])
with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')