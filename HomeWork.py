n=int(input('Введите трехзначное число '))
if 999>=n>=100:
    sum = 0
    while n>0:
        z = n%10
        sum = z+sum
        n//=10
    print(sum)
else:
    print('Я же просил трехзначное')