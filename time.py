import time;
import calendar;
local_time=time.localtime(time.time())

print local_time

r=raw_input("enter year");
m=raw_input("enter month");

print"calendar"


cal=calendar.month(int(r),int(m))

print cal


local_time2=time.asctime(time.localtime(time.time()))

print local_time2