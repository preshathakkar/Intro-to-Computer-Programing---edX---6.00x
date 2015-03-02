balance = 4428
annualInterestRate = 0.18
payment = 10

def monthlyPay(p, b):
	months = 12
	while months > 0:
		b = (b-p)*(1+(annualInterestRate/12))	
		months -= 1
	return b

while balance > 0.0:
	if monthlyPay(payment, balance) <= 0:
		break
	else:
		payment += 10


print('Minimum monthly payment: ' + str(payment))
