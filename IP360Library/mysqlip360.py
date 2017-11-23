#-*- coding: utf-8 -*-
'''
    created by xietingmei 2017-11-16
'''
__version__='0.1'

import string
import MySQLdb
import pysical_devices as device

class MysqlIP360(object):


    #----------------------------------------------------------------------------------------mysql_create_ip360_db
    def mysql_create_ip360_db(self):
        '''
            创建mysql ip360数据库。

            参数:
            
            举例:
            | mysql create ip360 db |
        '''

        # 连接数据库
        conn = MySQLdb.connect(host=device.DICT__IP360_SERVER_DB['IP'],\
                                port=device.DICT__IP360_SERVER_DB['PORT'],\
                                user=device.DICT__IP360_SERVER_DB['USERNAME'],\
                                passwd=device.DICT__IP360_SERVER_DB['PASSWORD'])
        curs = conn.cursor()

        # 删除原有数据库
        cmd = "DROP DATABASE " + device.DICT__IP360_SERVER_DB['DB_NAME']
        curs.execute(cmd)

        # 创建数据库
        cmd = "CREATE DATABASE IF NOT EXISTS " +  device.DICT__IP360_SERVER_DB['DB_NAME'] + " DEFAULT CHARSET utf8 COLLATE utf8_general_ci"
        curs.execute(cmd)

        curs.close()
        conn.commit()
        conn.close()

        return 1

#----------------------------------------------------------------------------------------mysql_search_table
    def mysql_search_table(self,db_name,sql_string):
        '''
            查询数据表。

            参数：
            db_name: 要查询的数据库，如 ip360_test
            sql_string: sql语句

            举例:
            | mysql search table | ${db_name} | ${sql} |
        '''
        # 连接数据库
        if db_name==device.DICT__IP360_SERVER_DB['DB_NAME']:
            conn = MySQLdb.connect(host=device.DICT__IP360_SERVER_DB['IP'],\
                                port=device.DICT__IP360_SERVER_DB['PORT'],\
                                user=device.DICT__IP360_SERVER_DB['USERNAME'],\
                                passwd=device.DICT__IP360_SERVER_DB['PASSWORD'])
        curs = conn.cursor()

        # 进入数据库
        cmd = "USE " + db_name
        curs.execute(cmd)

        # 执行sql语句
        curs.execute(sql_string)
        row = curs.fetchall()
        count = curs.rowcount

        curs.close()
        conn.commit()
        conn.close()

        if count==0:
            print "no record in db" 
            return 0
        else:
            print "count=%d row = %s" %(count,row[count-1])
            return row[count-1][0]


if __name__ == "__main__" :
    my_obj = MysqlIP360()

