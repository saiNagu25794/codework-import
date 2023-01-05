
def get_the_yesterday_today_tomorrow_date():
    from datetime import datetime, timedelta

    presentDay = datetime.now()
    yesterday = presentDay - timedelta(1)
    Tomarrow = presentDay + timedelta(1)


    print("Yesterday Date = ",yesterday.strftime("%d-%m-%Y"))
    print("Today's Date = ", presentDay.strftime("%d-%m-%Y"))
    print("Tomarrow Date = ",Tomarrow.strftime("%d-%m-%Y"))






#Python | Find yesterday’s, today’s and tomorrow’s date

if __name__ == "__main__":
    get_the_yesterday_today_tomorrow_date()