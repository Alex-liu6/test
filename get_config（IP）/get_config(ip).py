import  paramiko                                                               #导入paramiko模块，用于SSH登录
from device_ip_list import IP_ADDR                                             #从device_ip_list中导入IP_ADDR

USER = 'admin';                                                                #定义变量USER等于字符串admin
PASS = 'admin';                                                                #定义变量PASS等于字符串admin
PORT = 22                                                                      #定义变量PORT等于整数22

def get_config(IP):                                                            #定义函数get_config，参数为IP
    ssh = paramiko.SSHClient()                                                 #创建SSH对象
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())                  #允许连接不在know_hosts文件中的主机
    ssh.connect(hostname=IP,port=PORT,username=USER,password=PASS)             #连接服务器
    stdin, stdout, stdeer = ssh.exec_command('show run | include name')        #执行命令
    result = stdout.read()                                                     #获取命令结果
    # print(str(result,encoding='utf-8'))
    result = str(result, encoding='utf-8')
    ssh.close()                                                                #关闭连接
    return result

for x in  IP_ADDR:                                                             #for循环，定义x存在于IP_ADDR
    a = get_config(x)                                                          #定义变量a 等于函数get_coonfig(x)
    print(a)                                                                   #打印变量a


'''    
    with open('/home/alex/config.text', 'a+') as f:                            #将输出结果写入到文件中
        f.write(a + '\n')
        f.close()
'''


'''
#输出结果
hostname CSR_1
ip domain name alex.com
multilink bundle-name authenticated
 subject-name cn=IOS-Self-Signed-Certificate-3585396926
username admin privilege 15 password 0 admin
username alex privilege 10 password 0 alex666
username Restconf-Alex privilege 15 password 0 alex-test


hostname CSR_2
ip domain name alex.com
multilink bundle-name authenticated
 subject-name cn=IOS-Self-Signed-Certificate-3781475301
username admin privilege 15 password 0 admin
'''
