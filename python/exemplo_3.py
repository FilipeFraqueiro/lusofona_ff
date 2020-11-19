#!usr/bin/python

inteiros = []

# inteiros = [int_ for int_ in range(1, 1024+1)]
# print(inteiros)

file = open("portList.txt", "w")

[file.write(str(int_) + "\n") for int_ in range(1, 1024+1)]

file.close()



#################################################################
ip_subnet_mask_C = "192.168.1."

ips = []

# ips = [ip_subnet_mask_C + str(ip) for ip in range(256)]
# print(ips)

file = open("ipList.txt", "w")

[file.write(ip_subnet_mask_C + str(ip) + "\n") for ip in range(256)]

file.close()





