
# Найдите сумму цифр трехзначного числа.
n=input('введите трехначное число: ')
print(int(n[0])+int(n[1])+int(n[2]))

# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше 
# журавликов, чем Петя и Сережа вместе?

s=int(input('введите общее колличество журавликов: '))
a=s//6
b=a*4
print(f'Петя и Сережа сделали по {a} журавликов\nКатя сделала {b} журавликов')

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

n=input('Введите номер билета: ')
if int(n[0])+int(n[1])+int(n[2])==int(n[3])+int(n[4])+int(n[5]):
    print('Поздравляем Ваш билет Счастливый!!!')
else:
    print('NO')

# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

print('Введите размер шоколадки: ')
a=int(input('введите количество долек в длину: '))
b=int(input('введите количество долек в ширину: '))
с=int(input('введите количество долек которое хотите отломить: '))
if с==a or с==b or с==a*2 or с==a*3 or с==a*4 or с==b*2 or с==b*3 or с==b*4 or с==b*5 or с==b*5:
    print('шоколдака делится на два прямоугольника')
else:
    print('шолоколадка не делится на два прямоугольника')