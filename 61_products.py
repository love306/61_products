products = []
while True:
	name = input('請輸入名稱:')
	if name == 'q':
		break
	price = input('請輸入價格:')	
	products.append([name, price])
print(products) 
for p in products:
	print(p)
	print(p[0])