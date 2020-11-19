list_ = ["windows", "macos", "linux", "solaris", "android", "ios"]


#################################################

file_name = "export.txt"

file = open(file_name, "w")

for val in list_:
	if val != "solaris":
		print(val)
		file.write(val + "\n")

file.close()


#################################################

file_name = "export_2.txt"

file = open(file_name, "w")

i = 0
while i < len(list_):
	val = list_[i]
	if val != "solaris":
		print(val)
		file.write(val + "\n")
	i += 1


file.close()


