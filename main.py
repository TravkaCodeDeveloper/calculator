a = int(
    input('Введите первое число: ')
)

print(
    '[1. + ][2. - ][3. * ][4. /]'
)
operator = input(
    'Выберите оператор(напишите число) '
)
b = int(
    input(
        'Введите второе число: '
    )
)

result = ''
if operator == '1':
    result = a + b
elif operator == '2':
    result = a - b
elif operator == '3':
    result = a * b
elif operator == '4':
    result = a / b

print(
    'Результат: {}'.format(
        result
    )
)
