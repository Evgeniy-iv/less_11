class Error(Exception):
    pass


class ValueTextError(Error):
    pass


numbers_list = []
while True:

    try:
        i_num = input("Введите число: ")

        if i_num == 'stop':
            break
        elif i_num.lstrip('-').replace('.', '', 1).isdigit() is False:
            raise ValueTextError

        else:
            i_num = float(i_num)
            numbers_list.append(i_num)
    except ValueTextError:
        print("Введенное значение не является числом\n")

print(numbers_list)
