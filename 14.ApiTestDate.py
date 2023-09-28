from datetime import timedelta
a = timedelta(days = 2,hours= 4)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print((c.seconds / 3600))
print((c.total_seconds() / 3600))


from datetime import datetime
a = datetime(2012,9,23)
print(a)
print((a + timedelta(days=10)))

now = datetime.today()
print(now)

# 自动处理闰年
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)

# 如果你需要执行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等， 可以考虑使用 dateutil模块
# 需要注意的就是，它会在处理月份(还有它们的天数差距)的时候填充间隙 dateutil.relativedelta()
a = datetime(2012, 9, 23)
# a += timedelta(months=1)
# Traceback (most recent call last):
#   File "C:\Users\Administrator\PycharmProjects\pythonProject\14.ApiTestDate.py", line 27, in <module>
#     a += timedelta(months=1)
# TypeError: 'months' is an invalid keyword argument for __new__()

from dateutil.relativedelta import  relativedelta
a = a + relativedelta(months=+1)
print(a)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

# 上面的算法原理是这样的：先将开始日期和目标日期映射到星期数组的位置上(星期一索引为0)， 然后通过模运算计算出目标日期要经过多少天才能到达开始日期。然后用开始日期减去那个时间差即得到结果日期。
print(datetime.today())
print(get_previous_byday('Monday'))
print(get_previous_byday('Tuesday'))
print(get_previous_byday('Sunday', datetime(2012, 12, 21)))


# 计算当前月份的日期范围
from datetime import datetime, date, timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
   print(first_day)
   first_day += a_day



#string -> date
# strptime() 的性能要比你想象中的差很多， 因为它是使用纯Python实现，并且必须处理所有的系统本地设置
text = '2012-09-01'
y = datetime.strptime(text,"%Y-%m-%d")
z = datetime.now()
diff = z - y
print(diff)


# 这个函数比 datetime.strptime() 快7倍多。 如果你要处理大量的涉及到日期的数据的话，那么最好考虑下这个方案
def parse_ymd(s):
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

# 结合时区的日期操作
# pytz 模块一个主要用途是将 datetime 库创建的简单日期对象本地化
from datetime import datetime
from pytz import timezone
d = datetime(2012,12,21,9,30,0)
print(d)

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

# 如果你打算在本地化日期上执行计算，你需要特别注意夏令时转换和其他细节。 比如，在2013年，美国标准夏令时时间开始于本地时间3月13日凌晨2:00(在那时，时间向前跳过一小时)。 如果你正在执行本地计算，你会得到一个错误