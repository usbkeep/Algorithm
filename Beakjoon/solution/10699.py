# 오늘 날짜
# https://www.acmicpc.net/problem/10699

"""
    서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
"""
import datetime

#utc = datetime.datetime.today()
#utc = datetime.datetime.utcnow()

utc = datetime.datetime.now()
kst = utc + datetime.timedelta(hours = 9)


print(kst.date())