def payment_due(balance,payment_rate):
    '''
    (number, number) -> float

    Returns the payment to be made at the starting of the month
    having balance amount due at the payment rate specified.

    >>>payment_due(5000, 2)
    >>>100.0
    '''

    return balance*(payment_rate/100.00)


def interest(balance, payment, annual_rate):
    '''
    (number, number, number) -> float

    Returns the interest charged for a particular month
    having balance amount due at, the payment made for the month
    and at the annual interest rate specified.

    >>>interest(5000, 100, 18)
    >>>73.50
    '''

    return (balance - payment) * (annual_rate / 1200.0)

def final_balance(original_balance, annual_rate, payment_rate, months):
    '''
    (number, number, number, number) -> float

    Returns the balance amount at the month specified for the original balance
    calculating interest at the annual and payment rate given

    >>>final_balance(5000, 18, 2, 1)
    >>>4973.5
    '''
    while months >=1:
        p = payment(original_balance, payment_rate)
        i = interest(original_balance, p, annual_rate)
        original_balance = original_balance-p+i
        months -=1
        
    return original_balance
