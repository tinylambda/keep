import datetime


today = datetime.date.today()
print(today)
print("ctime: ", today.ctime())
tt = today.timetuple()
print("tuple: tm_year = ", tt.tm_year)
print("tm_mon = ", tt.tm_mon)
print("tm_mday = ", tt.tm_mday)
print("tm_hour = ", tt.tm_hour)
print("tm_min = ", tt.tm_min)
print("tm_sec = ", tt.tm_sec)
print("tm_wday = ", tt.tm_wday)
print("tm_yday = ", tt.tm_yday)
print("tm_isdst = ", tt.tm_isdst)

print("original: ", today.toordinal())
print("year: ", today.year)
print("month: ", today.month)
print("day: ", today.day)
