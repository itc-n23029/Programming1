import calendar


def colored_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    cal_str = f"    {calendar.month_name[month]} {year}\nMo Tu We Th Fr Sa Su\n"

    for week in cal:
        for day in week:
            if day == 0:
                cal_str += "   "
            elif calendar.weekday(year, month, day) == 5:
                cal_str += "\x1b[34m{:2}\x1b[0m ".format(day)
            elif calendar.weekday(year, month, day) == 6:
                cal_str += "\x1b[31m{:2}\x1b[0m ".format(day)
            else:
                cal_str += "{:2} ".format(day)
        cal_str += "\n"

    return cal_str


print(colored_calendar(2023, 8))
