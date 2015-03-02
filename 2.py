annualInterestRate = 0.2
balance = 320000
mi = float(annualInterestRate)/12
x = float(balance)/12
y = (float(balance)*((1 + mi)**12))/12
def rembal(a,b,c):
        for m in range(1,13):    
                rb = float(b) - c
                b = float(rb) * (1 + float(a)/12)
        return b


while True:
        nb = balance
        ans = (x+y)/2
        nnb=round((rembal(annualInterestRate,nb,ans)),2)
        if nnb > 0.01 :
                x = ans
        elif nnb < 0.01:
                y = ans
        else:
            break
                
        
print('lowest payment:' + str(round(ans,2)))
