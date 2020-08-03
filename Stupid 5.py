import random 
a=1
b=100
num = random.randint(1,100)

while True:
    print('Range so far%d-%d'%(a,b))
    ans = int(input('Insert Number:'))
    if ans>num:
        b = ans
    elif ans<num:
        a = ans
    elif ans==num:
        print('Stonks')
        break