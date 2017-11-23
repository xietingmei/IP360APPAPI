#-*- coding: utf-8 -*-
'''
    created by xietingmei 2017-11-16
'''
__version__='0.1'

import json
import requests
import urllib2
import urllib
import cookielib
import MySQLdb
import pysical_devices as device
import api_url as api


#  ----------------------------------------------------发送Json配置到Api

class IP360Request(object):
    myresponse = ''

    def __init__(self,url,strjson):
        self.dutip = device.DICT__DEVICE_IP360_SERVER['IP']
        self.port = device.DICT__DEVICE_IP360_SERVER['HTTP_PORT']
        self.strdata = strjson
        self.headers = {"Content-Type": "application/json"}
        self.url = url
        self.auth_token = None

    def search_db(self):
        conn = MySQLdb.connect(host=device.DICT__IP360_SERVER_DB['IP'],\
                                port=device.DICT__IP360_SERVER_DB['PORT'],\
                                user=device.DICT__IP360_SERVER_DB['USERNAME'],\
                                passwd=device.DICT__IP360_SERVER_DB['PASSWORD'])

        curs = conn.cursor()
        cmd = "USE " + device.DICT__IP360_SERVER_DB['DB_NAME']
        curs.execute(cmd)
        # 执行sql语句
        curs.execute("select token from eap_auth_token order by id")
        row = curs.fetchall()
        count = curs.rowcount
        curs.close()
        conn.commit()
        conn.close()
        print "db count = %d" %count
        self.auth_token = row[count-1][0]


    def request_post(self):
        '''
            通过http post发送Json格式request字符串到系统。


        '''
        print "enter post config"
        if self.url==api.ADMIN_API['ip360newright']:
            print self.strdata
            strcode = self.strdata.encode('utf8')
            boundary = '----------%s' % hex(12345 * 1000)
            self.headers = {"Content-Type": "multipart/form-data; boundary=%s" % boundary,"User-Agent":"Mozilla/4.0"}
            req = urllib2.Request('http://'+ self.dutip + ":" + self.port + self.url,data=strcode,headers=self.headers)
        else:
            print self.strdata
            strcode = self.strdata.encode('utf8')
            self.headers = {"Content-Type": "application/x-www-form-urlencoded","User-Agent":"Mozilla/4.0"}
            req = urllib2.Request('http://'+ self.dutip + ":" + self.port + self.url,data=strcode,headers=self.headers)
        print self.dutip
        print self.port
        print self.url
        response = urllib2.urlopen(req)
        return response.read()


    def request_get(self):
        '''
            通过http get发送Json格式的request字符串到系统。

        '''
        print self.url
        print self.dutip
        print self.port
        
        response = requests.get('http://'+ self.dutip + ":" + self.port + self.url)
        return response

    def decode_response(self):
        '''
            解析DUT返回的json response信息。

            返回：response中的 error_no 和 error_string 信息。           
            举例:
            |${error_string}= |&{dictname}|
            |log|${error_string}|
        '''
        resp_dict = json.loads(NgfwPost.myresponse.content)
        head_value = resp_dict['head']
        error_no = head_value['error_code']
        error_string =  head_value['error_string']
    
        print 'error_no = %s'%(error_no)
        print 'error_string = %s'%(error_string)
        ## Added by xietingmei for get response data information.
        ret_value = ''
        if 'data' in resp_dict:
            ret_value = resp_dict['data']
        elif 'body' in resp_dict:
            ret_value = resp_dict['body']
        else:
            ret_value = ''
        return ret_value


if __name__ == "__main__":
    print "start request"
    dut_ip = '47.94.74.150'
    dut_string = ''
    dut_url = "/user/v2/login?params="
    data = 'http://' + dut_ip + dut_url
    print "request_string=%s" %data
    my_obj = IP360Request(dut_ip,dut_url,dut_string,9060)
    my_response = my_obj.request_get()
    print my_response






    
