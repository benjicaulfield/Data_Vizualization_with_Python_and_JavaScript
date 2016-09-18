__author__ = 'Bradley'

import datetime
from dateutil import parser
import json

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder)

now_str = dumps({'time': datetime.datetime.now()})
print(now_str)

time_str = '2012/01/01 12:32:11'

dt = datetime.datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')
dt = datetime.datetime.strptime('01/01/2012', '%Y/%m/%d %H:%M:%S')
print(dt)