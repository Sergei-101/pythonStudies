num = input('Введите номер билетика: ')
res = [int(x) for x in str(num)]
res_one = int(res[0])+int(res[1])+int(res[2])
res_two = int(res[3])+int(res[4])+int(res[5])
if res_one==res_two:
    print('Поздравляем, у вас счастливый билетик')
else:
    print('Может в другой раз повезет')