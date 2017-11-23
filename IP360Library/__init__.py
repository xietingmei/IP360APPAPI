from mysqlip360 import MysqlIP360
from user import IP360Login
from uploadfileoss import UploadFileOss 

__version__='0.1'

class IP360Library(MysqlIP360, IP360Login, UploadFileOss):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
























