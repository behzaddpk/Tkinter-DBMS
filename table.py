def table(num, limit):
    for a in range(1,limit + 1):
        print(num, ' x ', a, ' = ', num * a)

num = int(input('Write table of: '))
limit = int(input('Write Multiplication no: '))



solution = table(num, limit)
