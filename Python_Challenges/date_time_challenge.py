from datetime import datetime
from pytz import timezone

format = '%H-%p'
now_utc=datetime.now(timezone('UTC'))


def office_time():
    if range(9,17,1):
        print ('office is open')
    else:
        print('office is closed')

now_portland = now_utc.astimezone(timezone ('US/Pacific'))
print (now_portland.strftime(format))
office_time()
        
now_newYork = now_utc.astimezone(timezone ('US/Eastern'))
print (now_newYork.strftime(format))
office_time()

now_london = now_utc.astimezone(timezone ('Europe/London'))
print (now_london.strftime(format))
office_time()






    
