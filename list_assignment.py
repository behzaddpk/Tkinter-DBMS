product_id = [1]
product_name = ['Dell']
product_type = ['laptop']
product_price = [7000]


print("Welcome to Invontory Managament: ")
print("1, Add Product: ")
print("2, View Product: ")
print("3, Search View: ")
print("4, Delete Product: ")
print("5, modify Product: ")
print("6, Exit: ")



while True:
    type = int(input('Choose an Option: '))


    if type == 1:
        id = int(input('Enter Id: '))
        name = input('Enter Product Name: ')
        type = input('Enter Product Type: ')
        price = input('Enter Product Price: ')
        product_id.append(id)
        product_name.append(name)
        product_type.append(type)
        product_price.append(price)
        print('Data added Successfully')
    elif type == 2:
        for index in range(len(product_id)):
            print (product_id[index], '\t', product_name[index], '\t', product_type[index], '\t', product_price[index])
    elif type == 3:
        id = int(input('Enter Id to Search: '))
        if id in product_id:
            index = product_id.index(id)
            print('id: ', product_id[index])
            print('name: ', product_name[index])
            print('type: ', product_type[index])
            print('price: ', product_price[index])
        else:
            print("Product not Found")
    elif type == 4:
        id = int(input('Enter Id to Deleted: '))
        if id in product_id:
            index = product_id.index(id)
            product_id.pop(index)
            product_name.pop(index)
            product_type.pop(index)
            product_price.pop(index)
            print('product deleted')
        else:
            print("Product not Found")   
    elif type == 5:
        id = int(input('Enter Id to Modify: '))
        if id in product_id:
            index = product_id.index(id)
            product_name[index] = input("Enter Product Name: ")
            product_type[index] = input("Enter Product type: ")
            product_price[index] = input("Enter Product price: ")

    elif type == 6:
        break
    else:
        print ("please chose an valid Number")