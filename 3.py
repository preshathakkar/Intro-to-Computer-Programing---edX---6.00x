balance=4428
annualInterestRate=.18
minimumMonthlyPayment=0
newbalance=balance
while minimumMonthlyPayment*11 <= balance:    
        newbalance = (newbalance - minimumMonthlyPayment)* (1+(annualInterestRate/12))
        minimumMonthlyPayment += 10
print "Lowest Payment: ", minimumMonthlyPayment
