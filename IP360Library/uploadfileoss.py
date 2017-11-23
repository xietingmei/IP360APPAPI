#-*- coding: utf-8 -*-
'''
    created by xietingmei 2017-11-23
'''

import os
import sys
import oss2

class UploadFileOss(object):
   #basedir='test/test.png'
   #ossDir="mobileRight/990/20171123/bd6eea77e1ee485eb46f1a1ed679bef3-20171123_100412.png"


   def upload_file_oss(self,basedir,ossDir):
        print ('uploading..',basedir,'remoteName',ossDir)
        ossAuth=oss2.Auth('LTAItT8aLl7ObpgJ','TNqsCO8QEPFMxjxd8ca8xOz9AdG3Cx')
        ossBucket=oss2.Bucket(ossAuth,'oss-cn-beijing.aliyuncs.com','ip360-test')
        result=ossBucket.put_object_from_file(ossDir,basedir)
        if result.status==200:
            print('http status: {0}'.format(result.status))
            print('request_id: {0}'.format(result.request_id))
            print('ETag: {0}'.format(result.etag))
            print('date: {0}'.format(result.headers['date']))
            return 1
        else:
            return 0
          

if __name__ == "__main__" :
      my_obj = UploadFileOss()

