from datetime import datetime, timedelta


# my_time = datetime.now()


def my_month_ru(my_time):
    # my_time = my_time - timedelta(weeks=2)
    my_time = my_time
    month = my_time.month
    if month == 1:
        m = "Январь"
    elif month == 2:
        m = "Февраль"
    elif month == 3:
        m = "Март"
    elif month == 4:
        m = "Апрель"
    elif month == 5:
        m = "Май"
    elif month == 6:
        m = "Июнь"
    elif month == 7:
        m = "Июль"
    elif month == 8:
        m = "Август"
    elif month == 9:
        m = "Сентябрь"
    elif month == 10:
        m = "Октябрь"
    elif month == 11:
        m = "Ноябрь"
    elif month == 12:
        m = "Декабрь"
    return str(my_time.day) + " " + m + " " + str(my_time.year)


def my_month_uz(my_time):
    # my_time = my_time - timedelta(weeks=2)
    my_time = my_time
    month = my_time.month
    if month == 1:
        m = "Yanvar"
    elif month == 2:
        m = "Fevral"
    elif month == 3:
        m = "Mart"
    elif month == 4:
        m = "Aprel"
    elif month == 5:
        m = "May"
    elif month == 6:
        m = "Iyun"
    elif month == 7:
        m = "Iyul"
    elif month == 8:
        m = "Avgust"
    elif month == 9:
        m = "Sentabr"
    elif month == 10:
        m = "Oktabr"
    elif month == 11:
        m = "Noyabr"
    elif month == 12:
        m = "Dekabr"
    return str(my_time.day) + " " + m + " " + str(my_time.year)


# print(my_month_ru(my_time))

