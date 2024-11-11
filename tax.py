salary = int(input("Enter YOur Salary: "))

if salary < 600000:
    print("FBR can't charge any tex pecrentage on You")
elif salary < 1200000:
    tax_charge_amount = salary - 600000
    payable_tax = tax_charge_amount * 5/100
    print(payable_tax)

elif salary < 1800000:
    tax_charge_amount = salary - 1200000
    payable_tax = 30000 + tax_charge_amount * 10/100
    print(payable_tax)

elif salary < 2500000:
    tax_charge_amount = salary - 1800000
    payable_tax = 90000 + tax_charge_amount * 15/100
    print(payable_tax)

elif salary < 3500000:
    tax_charge_amount = salary - 2500000
    payable_tax = 195000 + tax_charge_amount * 17.5/100
    print(payable_tax)

elif salary < 5000000:
    tax_charge_amount = salary - 3500000
    payable_tax = 370000 + tax_charge_amount * 20/100
    print(payable_tax)

elif salary < 8000000:
    tax_charge_amount = salary - 5000000
    payable_tax = 670000 + tax_charge_amount * 22.5/100
    print(payable_tax)

elif salary < 12000000:
    tax_charge_amount = salary - 8000000
    payable_tax = 1345000 + tax_charge_amount * 25/100
    print(payable_tax)

elif salary < 30000000:
    tax_charge_amount = salary - 12000000
    payable_tax = 2345000 + tax_charge_amount * 27.5/100
    print(payable_tax)

elif salary < 50000000:
    tax_charge_amount = salary - 30000000
    payable_tax = 7295000 + tax_charge_amount * 30/100
    print(payable_tax)

elif salary < 75000000:
    tax_charge_amount = salary - 50000000
    payable_tax = 13295000 + tax_charge_amount * 32.5/100
    print(payable_tax)

elif salary > 75000000:
    tax_charge_amount = salary - 75000000
    payable_tax = 90000 + tax_charge_amount * 35/100
    print(payable_tax)
