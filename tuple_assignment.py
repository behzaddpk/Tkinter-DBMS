from collections import namedtuple

product = namedtuple('product', ['id', 'Product_name', 'Product_category', 'Product_price'])
products = [product(1, 'HP', 'Laptop', 6000)]

print("Welcome to invontory managment: ")
print("1, Add Product")
print("2, view Product")
print("3, search Product")
print("4, Delete Product")
print("5, Modify Product")
print("6, Exit")
while True:
    type = int(input("Chose an Optionn: "))

    if type == 1:
        id = int(input("Enter product id:  "))
        name = input("Enter product Name: ")
        category = input ("Enter Product Category: ")
        price = input("Enter Product Price: ")
        products.append(product(id, name, category, price))
        print('Data Added Succesfully')
    elif type == 2:
        for index in range(len(products)):
            print(products[index].id, '\t', products[index].Product_name, '\t', products[index].Product_category, '\t', products[index].Product_price, '\t',)

    elif type == 3:
        id = int(input("Enter product id:  "))
        product = None
        for index in range(len(products)):
            if products[index].id == id:
                product = products[index]
                break
        
        if (product):
            print('id: ', product.id)
            print('Product Name: ', product.Product_name)
            print('Product Category: ', product.Product_category)
            print('Product Price: ', product.Product_price)
        
        else:
            print('product not found')