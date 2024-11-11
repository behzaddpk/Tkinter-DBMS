products = [{'id': 1, 'name': 'Iphone', 'category': 'Mobile', 'price': 8000,}]

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
        products.append({'id': id, 'name': name, 'category': category, 'price': price,})
        print("Added Success fully")
    elif type == 2:
        for index in range(len(products)):
            print(products[index].get('id'),  products[index].get('name'),  products[index].get('category'), products[index].get('price'))
    elif type == 3:
        id = int(input("Enter option to search product: "))
        product = None
        for index in range (len(products)):
            if (products[index].get('id') == id):
                product = products[index]
                break
        if (product):
            print("id: ", product.get(id))
            print("name: ", product.get('name'))
            print("category: ", product.get('category'))
            print("price: ", product.get('price'))
        else:
            print("Product not found")
        
    elif type ==4:
        id = int(input("Enter option to Delete product: "))
        deleted = False
        for index in range (len(products)):
            if (products[index].get('id') == id):
                del products[index]
                deleted = True
        if deleted:
            print("Product Deleted")
        else:
            print("No product found")
    elif type ==5:
        id = int(input("Enter option to Modify product: "))
        updated = False
        for index in range (len(products)):
            if (products[index].get('id') == id):
                name = input("Enter product Name: ")
                category = input ("Enter Product Category: ")
                price = input("Enter Product Price: ")
                products[index] = ({'id': id, 'name': name, 'category': category, 'price': price,})
                updated = True
        if updated:
            print("Product updated")
        else:
            print("No product found")
    elif type ==6:
        break

    else:
        print('You choose invalid optionn')