import re


class Date:

    @classmethod
    def number_from_date(cls, number_string):
        number = number_string.replace('-', '')
        number = int(number)
        return number

    @staticmethod
    def date_validation(date):
        re_date = re.compile(
            r'(?<!\d)(?:0?[1-9]|[12][0-9]|3[01])-(?:0?[1-9]|1[0-2])-(?:19[0-9][0-9]|20[01][0-9])(?!\d)')
        assert re_date.match(date), f'Формат даты неверный'
        try:
            month_31_list = ['01', '03', '05', '07', '08', '10', '12']
            if (date[0:2] == '31' and date[3:5] not in month_31_list) or (int(date[0:2]) > 28 and date[3:5] == '02'):
                raise ValueError
        except ValueError:
            print(f'Неверное количество дней в месяце')
        else:
            print(f'Дата верна')


print(Date.number_from_date('28-02-2019'))
date_inst = Date()
date_inst.date_validation('31-02-2019')
