x = int(input('weigh :'))
y =  float(input('high : '))
imc = x / (y**2)
if imc < 18.5 :
    print('skiny')
    a = 18.5-imc
    h = a*(y**2)
    print('u should increase ur weight at least : ',int(h))
elif imc >= 18.5 and imc <= 25 :
    print('PERFECT')
else :
    print('overweigh')
    b = imc - 25
    k = b*(y**2)
    print( 'u should decrease ur weigh at least :' ,int(k))
