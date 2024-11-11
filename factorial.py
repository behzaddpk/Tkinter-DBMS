def fact(counter):
    result = 1
    for i in range(1, counter+1):
        result *= i

    print(f'your anser of {counter} is {result}')

counter = int(input('write the value: '))
fact(counter)