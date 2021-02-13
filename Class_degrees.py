M = int(input('donner nombre d èlève :'))
while M < 4 or M > 40 :
    M = int(input('donner nombre d èlève :'))
N = [0]*M
s = 0
for i in range(M) :
    print('èlève n° : ' , i+1 )
    N[i] = float(input('donner le moyenne  d èlève : '))
    while N[i] < 0 or N[i] > 20 :
        N[i] = float(input('donner le moyenne d èlève : '))
    if N[i] >= 10 :
        s += 1
r = (s/M) * 100
print('Taux de rèussite : ' , r ,'%')
x = 20
b = []
for i in range(100) :
    for j in range(M) :
        if N[j] == x :
            b.append(N[j])
    x -= 0.25
print('la meilleur note est : ' , b[0])
print('la mauvaise naote est : ', b[-1])
