class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_data_1 = input('Введите первое число: ')
inp_data_2 = input('Введите второе число ')

try:
    inp_data_1 = int(inp_data_1)
    inp_data_2 = int(inp_data_2)
    if inp_data_2 == 0:
        raise OwnError('На ноль делить нельзя!')
except ValueError:
    print('Вы ввели не число')
except OwnError as err:
    print(err)
else:
    print(f'Результат деления {inp_data_1} на {inp_data_2} равен: {inp_data_1 / inp_data_2}')
