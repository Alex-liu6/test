import paramiko                                 #导入paramiko模块
import time                                     #导入time模块
import getpass                                  #导入gepass模块
from datetime import datetime                   #导入datetime模块

username ="admin"                               #设置SSH的用户名
password = getpass.getpass('Password:')         #通过getpass（）函数获取用户输入的SSH用户名并赋值给password

for i in range(1):
    ip="10.32.132.86"
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password)
    command=ssh_client.invoke_shell()
    command.send("terminal length 0"+"\n")          #调度交换机执行命令不分页显示，此为Cisco命令。（HUAWEI为[~HUAWEI]screen-length 0）
    output=(command.send("show running-config"+"\n"))      #调度交换机执行命令
 
    time.sleep(2)                          #暂停2秒，并将命令执行过程赋值给output对象，通过print output语句回显内容
    now=datetime.now()                     #读取当前时间

    backup=open("/root/backup/"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"-"+ip+".txt","wb")     #打开备份文件

    recv=command.recv(65535)       #将查询运行配置的回显内容赋值给recv这个对象

    backup.write(recv)            #将回显内容写入backup这个对象，相当于写入了备份文件中

    backup.close()                #关闭打开的文件

ssh_client.close()                #结束，断开SSH连接
