import paramiko                             #导入paramiko模块
import time                                 #导入time模块
import getpass                              #导入getpass模块

username = input('Username:')               #通过input（）函数获取用户输入的SSH用户名并赋值给username【python2调用函数为raw_input】
password = input('Password:')               #同上

for i in range(1,5):                          #通过for i in range（1,5）和ip="10.32.132."+str(i)语句实现循环登录交换机设备1到设备4
    ip="10.32.132."+str(i)
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip,username=username,password=password)
    command=ssh_client.invoke_shell()
    command.send("configure terminal" +"\n")              #调度交换机命令行执行命令
    command.send("aaa"+"\n")
    command.send("username admin privilege 15 password Aa123456"+"\n")
    command.send("end"+"\n")
    command.send("write"+"\n")
    command.send("\n")

    time.sleep(2)                   #暂停2秒，并将命令执行过程赋值给output对象，通过print output语句回显内容
    output=command.recv(65535)
    print (output)
 ssh_client.close()                 #退出SSH
