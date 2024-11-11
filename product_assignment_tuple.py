from collections import namedtuple

def findDataIndex(data, id):
    idx = None
    for index in range (len(data)):
        if (data[index].id == id):
            idx = index
            break
    return idx;

def findDataItem(data, id):
    item = None
    for index in range (len(data)):
        if (data[index].id == id):
            item = data[index]
            break
    return item;

product = namedtuple('porduct', ['id', 'name', 'category', 'price'])
products = [product(1, 'iphone', 'Mobile', '9000') ] 

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
        products.append(product(id, name, category,  price))
        print("Added Success fully")
    elif type == 2:
        for index in range(len(products)):
            print(products[index].id , products[index].name , products[index].category , products[index].price,)
    elif type == 3:
        id = int(input("Enter option to search product: "))
        product = findDataItem(products, id)
        if (product):
            print("id: ", product.id)
            print("name: ", product.name)
            print("category: ", product.category)
            print("price: ", product.price)
        else:
            print("Product not found")
        
    elif type ==4:
        id = int(input("Enter option to Delete product: "))
        index = findDataIndex(products, id)
        if (index >= 0):
            del products[index]
            print("Product Deleted")
        else:
            print("No product found")
    elif type ==5:
        id = int(input("Enter option to Modify product: "))
        index = findDataIndex(products, id)
        if (index>= 0):

            name = input("Enter product Name: ")
            category = input ("Enter Product Category: ")
            price = input("Enter Product Price: ")
            products[index] = (product(id, name, category,  price))
            updated = True
        if updated:
            print("Product Updated")
        else:
            print("No product found")
    elif type ==6:
        break

    else:
        print('You choose invalid optionn')