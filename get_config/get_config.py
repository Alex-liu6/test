import paramiko                                                    #导入paramiko模块，用于ssh登录
from device_list import device_info_list                           #从device_list中导入device_info_list

USER = device_info_list[1]['username']                             #定义变量USER等于device_info_list字典中第二个列表的username键的值
PASS = device_info_list[1]['password']                             #定义变量PASS等于device_info_list字典中第二个列表的password键的值
IP = device_info_list[1]['ip_address']                             #定义变量IP等于device_info_list字典中第二个列表的ip_address键的值
PORT = '22'                                                        #定义变量PORT等于 22 字符串

def get_config(IP1=IP):                                                       #定义函数get_config，默认值IP1等于IP
    ssh = paramiko.SSHClient()                                                #创建SSH对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())                 #允许连接不在know_hosts文件中的主机（也就是ssh的认证）
    ssh.connect(hostname=IP1,port=PORT,username=USER,password=PASS)           #连接服务器
    stdin, stdout, stderr = ssh.exec_command('show runn | include name')      #执行命令
    result = stdout.read()                                                    #获取命令结果
    print (str(result,encoding='utf-8'))
    result = str(result, encoding='utf-8')
    ssh.close()                                                               #关闭连接
    return result




'''
#输出结果
hostname CSR_2
ip domain name alex.com
multilink bundle-name authenticated
 subject-name cn=IOS-Self-Signed-Certificate-3781475301
username admin privilege 15 password 0 admin
'''
