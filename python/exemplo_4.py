#!usr/bin/python
#coding=utf-8
import sys
import os
# 1
# 2
# 3
# 4
# 5
def listar():
	"Lista a directoria"
	result = os.listdir()
	print(result)
	print()
# 1
# 2
# 3
# 4
# 5
def criar():
	"Cria a directoria"
	path = input("\tEnter folder name (or path): ")

	try:
		os.mkdir(path)
		print("Success\n")

	except Exception as e:
		# print(e)
		print("Could not create folder")
		print()
# 1
# 2
# 3
# 4
# 5
def editar():
	"Edita a directoria"
	print("Edit folder")
# 1
# 2
# 3
# 4
# 5
def remover():
	"Remove a directoria"
	path = input("\tEnter folder name (or path): ")
	
	try:
		os.rmdir(path)
		print("Success\n")

	except Exception as e:
		# print(e)
		print("Could not delete folder")
		print()
# 1
# 2
# 3
# 4
# 5
def main():
	print("Select an option:")
	print("\t0 - exit")
	print("\t1 - listar")
	print("\t2 - criar")
	print("\t3 - editar")
	print("\t4 - remover")
	print()

	try:
		while True:
			option = input("Enter option: ")

			try:
				option = int(option)

			except Exception as e:
				# print(e)
				print("Verify input!\n")
				
				continue

			if option == 0:
				print("\nBye!")
				break

			elif option == 1:
				listar()

			elif option == 2:
				criar()

			elif option == 3:
				editar()

			elif option == 4:
				remover()

			else:
				print("Wrong option!\n")

	except KeyboardInterrupt:
		print("\n\nYou stoped the program!")
		sys.exit()
# 1
# 2
# 3
# 4
# 5
if __name__ == "__main__":
	main()