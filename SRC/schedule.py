from flask import Flask
import calendar

hc = calendar.HTMLCalendar(firstweekday=0)
str = hc.formatmonth(2021, 1)
print (str)

@app.route('/route_name')
def method_name():
    pass