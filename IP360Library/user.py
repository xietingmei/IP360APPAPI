#-*- coding: utf-8 -*-
'''
    created by xietingmei 2017-11-16
'''
__version__='0.1'

import string
import urllib2
import urllib
import cookielib
import json
import sys
from basiclib import *
import pysical_devices as device
import api_url as api
import time
import datetime
import random
reload(sys) 
sys.setdefaultencoding('utf8')

class IP360Login(object):

    #----------------------------------------------------------------------------------------IP360WebApi
    def ip360appapi_login(self,**confdict):
        '''
            IP360appapi登录。

            参数:
          
            举例:
            | ip360appapi login |
        '''
        # 配置login信息
        json_content = ''
        url_string = api.ADMIN_API['ip360login'].replace("account",confdict['userAccount']).replace("password",confdict['userPwd'])
        
        # 发送request到IP360APPAPI
        my_request = IP360Request(url_string,json_content)
        res = my_request.request_post()
        print "response",res
        
        tokenlist = []
        tokenlist = res.split(',')
        strname = "\"token\":"
        templist = []
        accesstoken=''
        for i in range(0,len(tokenlist)):
               if strname in tokenlist[i]:
                   templist=tokenlist[i].split(':')
                   accesstoken1 = templist[1]
                   accesstoken = accesstoken1.strip('\"}')
                   break
        print 'Get the accesstoken',accesstoken
        idlist = []
        idlist = res.split(',')
        strname = "\"userId\":"
        templist = []
        ids=''
        for i in range(0,len(idlist)):
               if strname in idlist[i]:
                   templist=idlist[i].split(':')
                   ids1 = templist[1]
                   ids = ids1.strip('\"}')
                   break
        print 'Get the id',ids
        # 解析response返回信息

        if 'token' in res:
            print 'Passed:ip360login successed';
            flag_ret = 1
            return accesstoken,ids
        else:
            print 'Failed:ip360login failed';
            flag_ret = 0
            return flag_ret

    #----------------------------------------------------------------------------------------IP360APPApi
    def ip360appapi_xianchangquzheng(self,token,**confdict):
        '''
            IP360appapi现场取证。

            参数:
          
            举例:
            | ip360appapi xianchangquzheng |
        '''
        # 配置xianchangquzheng信息
        fileDate=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        fileTitle=time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))

        json_content = '' 
        json_data = ['''fileDate=''']
        json_data.append(fileDate)
        json_data.append('''&fileLocation=''')
        json_data.append(confdict['fileLocation'])
        json_data.append('''&fileSize=''')
        json_data.append(confdict['fileSize'])
        json_data.append('''&fileTime=''')
        json_data.append(confdict['fileTime'])
        json_data.append('''&fileTitle=''')
        json_data.append(fileTitle)
        json_data.append('''.png&fileType=''')
        json_data.append(confdict['fileType'])
        json_data.append('''&hashCode=''')
        json_data.append(confdict['hashCode'])
        json_data.append('''&imei=''')
        json_data.append(confdict['imei'])
        json_data.append('''&latitudeLongitude=''')
        json_data.append(confdict['latitudeLongitude'])
        json_data.append('''&token=''')
        json_data.append(token)
        json_content += ''.join(json_data)

        url_string = api.ADMIN_API['ip360xianchangquzheng']

        
        # 发送request到IP360APPAPI
        my_request = IP360Request(url_string,json_content)
        res = my_request.request_post()
        print "response",res
         
        resoureidlist = []
        resoureidlist = res.split(',')
        strname = "\"pkValue\":"
        templist = []
        ids=''
        for i in range(0,len(resoureidlist)):
               if strname in resoureidlist[i]:
                   templist=resoureidlist[i].split(':')
                   ids1 = templist[1]
                   ids = ids1.strip('\"}')
                   break
        print 'Get the resoureid',ids
          
        fileurllist = []
        fileurllist = res.split(',')
        strname = "\"fileUrl\":"
        templist = []
        fileurl=''
        for i in range(0,len(fileurllist)):
               if strname in fileurllist[i]:
                   templist=fileurllist[i].split(':')
                   fileurl1 = templist[1]
                   fileurl = fileurl1.strip('\"}')
                   break
        print 'Get the fileurl',fileurl
        
        if '文件信息保存成功' in res:
            print 'Passed:ip360 xianchangquzheng successed';
            flag_ret = 1
            return flag_ret,ids,fileurl
        else:
            print 'Failed:ip360 xianchangquzheng failed';
            flag_ret = 0
            return flag_ret


    #----------------------------------------------------------------------------------------IP360APPApi
    def ip360appapi_uploadfilecallback(self,token,ids):
        '''
            IP360appapi 文件上传到OSS后回调。

            参数:
          
            举例:
            | ip360appapi uploadfilecallback |
        '''
        # 配置uploadfilecallback信息

        json_content = '' 
        json_data = ['''resourceId=''']
        json_data.append(ids)
        json_data.append('''&token=''')
        json_data.append(token)
        json_content += ''.join(json_data)

        url_string = api.ADMIN_API['ip360uploadfilecallback']

        
        # 发送request到IP360APPAPI
        my_request = IP360Request(url_string,json_content)
        res = my_request.request_post()
        print "response",res
         
        if 'success' in res:
            print 'Passed:ip360 uploadfile callback successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:ip360 uploadfile callback failed';
            flag_ret = 0
            return flag_ret

    #----------------------------------------------------------------------------------------IP360APPApi
    def ip360appapi_payment(self,token,ids,**confdict):
        '''
            IP360appapi 支付。

            参数:
          
            举例:
            | ip360appapi payment |
        '''
        # 配置payment信息

        json_content = '' 
        json_data = ['''type=''']
        json_data.append(confdict['type'])
        json_data.append('''&count=''')
        json_data.append(confdict['count'])
        json_data.append('''&pkValue=''')
        json_data.append(ids)
        json_data.append('''&latitudeLongitude=''')
        json_data.append(confdict['latitudeLongitude'])
        json_data.append('''&token=''')
        json_data.append(token)
        json_content += ''.join(json_data)

        url_string = api.ADMIN_API['ip360payment']

        
        # 发送request到IP360APPAPI
        my_request = IP360Request(url_string,json_content)
        res = my_request.request_post()
        print "response",res
         
        if 'success' in res:
            print 'Passed:ip360 payment successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:ip360 payment failed';
            flag_ret = 0
            return flag_ret


    #----------------------------------------------------------------------------------------IP360APPApi
    def ip360appapi_getevidencelist(self,token,**confdict):
        '''
            IP360appapi 获取云端证据列表。

            参数:
          
            举例:
            | ip360appapi getevidencelist |
        '''
        # 配置payment信息

        json_content = '' 
        json_data = ['''type=''']
        json_data.append(confdict['type'])
        json_data.append('''&mobileType=''')
        json_data.append(confdict['mobileType'])
        json_data.append('''&pageNumber=''')
        json_data.append(confdict['pageNumber'])
        json_data.append('''&pageSize=''')
        json_data.append(confdict['pageSize'])
        json_data.append('''&token=''')
        json_data.append(token)
        json_content += ''.join(json_data)

        url_string = api.ADMIN_API['ip360getevidencelist']

        
        # 发送request到IP360APPAPI
        my_request = IP360Request(url_string,json_content)
        res = my_request.request_post()
        print "response",res
         
        if '云端证据' in res:
            print 'Passed:ip360 get evidence list successed';
            flag_ret = 1
            return flag_ret
        else:
            print 'Failed:ip360 get evidence list failed';
            flag_ret = 0
            return flag_ret

if __name__ == "__main__" :
    my_obj = IP360Login()

