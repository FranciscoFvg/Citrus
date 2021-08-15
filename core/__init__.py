import datetime

class SystemInfo:
    def __init__(self):
        pass

    @staticmethod
    def get_time():
        now = datetime.datetime.now()
        answer = 'Estamos no ano {}, mês {}, dia {} e são {}:{}'.format(now.year, now.month, now.day, now.hour, now.minute)
        return answer

