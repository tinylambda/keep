from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *


if __name__ == "__main__":
    d = datetime.now()
    print(d)

    print(d + relativedelta(weekday=FR))
    print(d + relativedelta(weekday=FR(-2)))
    print(d + relativedelta(weekday=TU(-1)))
