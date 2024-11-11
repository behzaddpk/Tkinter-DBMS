from unicodedata import name


prd_id = [1,2,3]
prd_name = ['iphone', 'oppo', 'redme']
prd_price = [9000, 8000, 7000]



manu = list(zip(prd_id, prd_name, prd_price))

print(manu)