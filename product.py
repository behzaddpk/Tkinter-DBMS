product_id = [1]
product_name = ['i phone']
product_category = ['Mobile']
product_price = ['7000']

print("Welcome to invontory managment: ")
print("1, Add Product")
print("2, view Product")
print("3, search Product")
print("4, Delete Product")
print("5, Modify Product")
print("6, Exit")
while True:
    type = int(input("Chose an Optionn: "))

    if type ==1:
        id = int(input("Enter product id:  "))
        name = input("Enter product Name: ")
        category = input ("Enter Product Category: ")
        price = input("Enter Product Price: ")
        product_id.append(id)
        product_name.append(name)
        product_category.append(category)
        product_price.append(price)
        print("Added Success fully")
    elif type ==2:
        for index in range(len(product_id)):
            print(product_id[index], "\t", product_name[index], "\t", product_category[index], "\t", product_price[index], "\t",)
    elif type ==3:
        id = int(input("Enter option to search product: "))
        if id in product_id:
            index = product_id.index(id)
            print("id: ", product_id[index])
            print("name: ", product_name[index])
            print("category: ", product_category[index])
            print("price: ", product_price[index])
        else:
            print("Product not found")
        
    elif type ==4:
        id = int(input("Enter option to Delete product: "))
        if id in product_id:
            index = product_id.index(id)
            product_id.pop(index)
            product_name.pop(index)
            product_category.pop(index)
            product_price.pop(index)
            print("product is deleted")
        else:
            print("Product not found")
    elif type ==5:
        id = int(input("Enter option to modify product: "))
        if id in product_id:
            index = product_id.index(id)
            product_name[index] = input("Enter product name:")
            product_category[index] = input("Enter category name: ")
            product_price[index] = input("Enter price: ")
            print("Product Modify")
        else:
            print("record not found")
    elif type ==6:
        break

    else:
        print('You choose invalid optionn')