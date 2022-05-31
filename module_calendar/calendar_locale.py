import calendar

c = calendar.LocaleTextCalendar(locale="zh_CN")
c.prmonth(2017, 7, w=1, l=1)

print()

c = calendar.LocaleTextCalendar(locale="fr_FR")
c.prmonth(2017, 7)
