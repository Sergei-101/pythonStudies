n = int(input('Введите кол-во долек n: '))
m = int(input('Введите кол-во долек m: '))
k = int(input('Сколько долек вы хотите отломить k: '))
if (n-1)>=k or (m-1)>=k:
    print('Да')
else:
    print("Нет")