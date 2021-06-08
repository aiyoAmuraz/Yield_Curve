import workalendar.america as america
import workalendar.usa as usa
import workalendar.asia as asia
import workalendar.europe as europe
import workalendar.africa as africa
import workalendar.oceania as oceania
from datetime import datetime, date, timedelta

american_countries=set(america.__all__.__str__().split("'")) -set(['(',')',", ",","])
usa_countries=set(usa.__all__.__str__().split("'")) -set(['(',')',", ",","])
asian_countries=set(asia.__all__.__str__().split("'")) -set(['(',')',", ",","])
european_countries=set(europe.__all__.__str__().split("'")) -set(['(',')',", ",","])
african_countries=set(africa.__all__.__str__().split("'")) -set(['(',')',", ",","])
oceanian_countries=set(oceania.__all__.__str__().split("'")) -set(['(',')',", ",","])


class timeline:
    def __init__(self,country: str):
        self.calendar=None
        if country in american_countries:
            exec(f'self.calendar=america.{country}()')
        elif country in usa_countries:
            exec(f'self.calendar=usa.{country}()')
        elif country in asian_countries:
            exec(f'self.calendar=asia.{country}()')
        elif country in european_countries:
            exec(f'self.calendar=europe.{country}()')
        elif country in african_countries:
            exec(f'self.calendar=africa.{country}()')
        elif country in oceanian_countries:
            exec(f'self.calendar=oceania.{country}()')
        else :
            print("Country is not correctly spelled. Please check workalendar list of countries.")

        if country in ['Canada','Australia','NewZealand']:
            self.ISDA_compliance='wednesday_the_third'
        else:
            self.ISDA_compliance = 'friday_the_second'

    def find_following_working_day(self,date : date):
        while self.calendar.is_holiday(date):
            date=date+timedelta(1)
        return self.calendar.find_following_working_day(date)
