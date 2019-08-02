#this is for generating dates
import datetime


days_of_week = ["Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday", "Sunday"]

class Day:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def __repr__(self):
        return self.name + " " + str(self.date)
def Generator(days, first_day):
    M_map = []
    if first_day == "Monday":
        day_index = 0
    if first_day == "Tuesday":
        day_index = 1
    if first_day == "Wednessday":
        day_index = 2
    if first_day == "Thursday":
        day_index = 3
    if first_day == "Friday":
        day_index = 4
    if first_day == "Saturday":
        day_index = 5
    if first_day == "Sunday":
        day_index = 6
    for day_c in range(1, days+1):
        day = Day(days_of_week[day_index], day_c)
        M_map.append(day)
        if day_index == 6:
            day_index = 0
        else:
            day_index += 1
    return M_map


class DaySchedual:
    def __init__(self, date):
        self.date = date
        self.schedual = {
               "00:00-00:30h": "",
               "00:30-01:00h": "",
               "01:00-01:30h": "",
               "01:30-02:00h": "",
               "02:00-02:30h": "",
               "02:30-03:00h": "",
               "03:00-03:30h": "",
               "03:30-04:00h": "",
               "04:00-04:30h": "",
               "04:30-05:00h": "",
               "05:00-05:30h": "",
               "05:30-06:00h": "",
               "06:00-06:30h": "",
               "06:30-07:00h": "",
               "07:00-07:30h": "",
               "07:30-08:00h": "",
               "08:00-08:30h": "",
               "08:30-09:00h": "",
               "09:00-09:30h": "",
               "09:30-10:00h": "",
               "10:00-10:30h": "",
               "10:30-11:0h": "",
               "11:00-11:30h": "",
               "11:30-12:00h": "",
               "12:00-12:30h": "",
               "12:30-13:00h": "",
               "13:00-13:30h": "",
               "13:30-14:00h": "",
               "14:00-14:30h": "",
               "14:30-15:00h": "",
               "15:00-15:30h": "",
               "15:30-16:00h": "",
               "16:00-16:30h": "",
               "16:30-17:00h": "",
               "17:00-17:30h": "",
               "17:30-18:00h": "",
               "18:00-18:30h": "",
               "18:30-19:00h": "",
               "19:00-19:30h": "",
               "19:30-20:00h": "",
               "20:00-20:30h": "",
               "20:30-21:00h": "",
               "21:00-21:30h": "",
               "21:30-22:00h": "",
               "22:00-22:30h": "",
               "22:30-23:00h": "",
               "23:00-23:30h": "",
               "23:30-00:00h": "",
        }

    def AddAction(self):
        time_period = input("Choose time period:")
