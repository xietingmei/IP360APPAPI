#-*- coding: utf-8 -*-

import time
import sys
import datetime
import random
import hashlib

reload(sys)
sys.setdefaultencoding('utf8')

test=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()-24*60*60))
print test
end=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print end
end1=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))
print end1
startObj=time.strftime('''%a %b %d %Y %H:00:00 GMT+0800 (中国标准时间)''',time.localtime(time.time()-168*60*60))
print startObj
endObj=time.strftime('''%a %b %d %Y %H:00:00 GMT+0800 (中国标准时间)''',time.localtime(time.time()-168*60*60))
print endObj

test=time.strftime('%H:%M:%S')
print test

boundary = '----------%s' % hex(12345 * 1000)
print boundary

