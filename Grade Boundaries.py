#
a=int (input('English Score'))
b=int (input('Maths Score'))
if a>=90:
    print ('Acceptable')
elif a>=80 and a<90:
    print ('Bad')
elif a>=70 and a<80:
    print ('Complete trash')
elif a>=60 and a<70:
    print ('Disgrace to your Family')
elif a<=60:
    print ('Emir')
   
if b>=90:
    print ('Acceptable')
elif b>=80 and a<90:
    print ('Bad')
elif b>=70 and a<80:
    print ('Complete trash')
elif b>=60 and a<70:
    print ('Disgrace to your Family')
elif b<=60:
    print ('Emir')

if a+b>=180:
    print("scholarship")
