device_info_list = [                                         #创建一个列表，里边包含两个字典
{
    'hostname' : 'CSR_1',
    'username' : 'admin',
    'password' : 'admin',
    'ip_address' : '192.168.1.1'
  },
{
    'hostname' : 'CSR_2',
    'username' : 'admin',
    'password' : 'admin',
    'ip_address' : '192.168.1.2'
  }
]

'''
for x in range(len(device_info_list)):                       #for循环，定义x等于device_info_list列表的长度
    print(x)                                                 #打印x
    for a,b in device_info_list[x].items():                  #for循环，定义a，b 并将字典解压缩
        print(a,b)                                           #打印a，b
        
'''


'''
#输出结果
0
hostname CSR_1
username admin
password admin
ip_address 192.168.1.1
1
hostname CSR_2
username admin
password admin
ip_address 192.168.1.2
'''
