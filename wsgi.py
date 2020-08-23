import datetime
import calendar
from flask import Flask, jsonify
import socket


application = Flask(__name__)

@application.route("/")
def hello():
    return "/weekday/<int:i_year>/<int:i_month>/<int:i_day>"

@application.route("/weekday/<int:i_year>/<int:i_month>/<int:i_day>")
def weekday( i_year, i_month, i_day):
    my_date = datetime.date(i_year, i_month, i_day)
    ret_weekday = calendar.day_name[my_date.weekday()]

    ret_hostname = socket.gethostname()

    return jsonify( { 'weekdate': ret_weekday, 'worker': ret_hostname } )

if __name__ == "__main__":
    application.run()
