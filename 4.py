balance=4428
annualInterestRate=.18

newbalance=balance
x=10
nb = balance

while float(nb) > 0 :
    nb = balance
    for m in range(1,13):
        rb = float(nb) - x
        nb = float(rb) * (1 + float(annualInterestRate)/12)
    x += 10

print('Lowest Payment :' + str(x))
