import sys
import os
from itertools import *

def banner():
	sys.stdout.write('''
  _______ _       _ _______ _______ _       ______                        
 (_______|_)     | (_______|_______| )     / _____)                   _   
  _____   _      | |_     _    _   |/__   ( (____   ____  ____ ____ _| |_ 
 |  ___) | |     | | |   | |  | |  /___)   \____ \ / ___)/ ___)  _ (_   _)
 | |_____| |_____| | |___| |  | | |___ |   _____) | (___| |   | |_| || |_ 
 |_______)_______)_|\_____/   |_| (___/   (______/ \____)_|   |  __/  \__)
                                                              |_|         

 by: Max_Cano
''')
                                                             
def clear():
	os.system("clear")

def tips():
	print (' ----------------------------------------------------------------------------------')
	print (' Tip: Add simbols like "_" "-" "." if you think that will be a posibility')
	print (' ----------------------------------------------------------------------------------')
	print (' Tip: Add words with capital letters, example: "Dylan" & "dylan"         ')
	print (' ----------------------------------------------------------------------------------')
	print (' Tip: Be sure first about how many elemts you will put                   ')
	print (' ----------------------------------------------------------------------------------')
	print ('                                                                                   ')


def mklist():
	global lst
	global output
	lst = []
	while True:
		try:
			output = input("Name of the file with extention : ")
			number = int((input("How many elements you will put? : ")))
			break
		except ValueError:
			print("\n ERROR : Please enter a number!!")
			mklist()
	for i in range (number):
		x = (input("Enter posibility : "))
		lst.append((x))
	return(lst)
	return(output)

def Permutation():
	print ("Wait...")
	global perm
	permutations(lst)
	perm = list(permutations(lst, 1)), list(permutations(lst, 2)), list(permutations(lst, 3)), list(permutations(lst, 4))
	#add other list with the next number if you want more permutations
	#print (perm)
	return perm

def mkfile():
	repr(perm)
	f = open(output, "w")
	f.write (repr(perm))
	f.close()


def ask():
	print ("\n".join([str(x) for x in lst]))
	ask = (input('Are you sure about the elements? [y/n] : '))
	if ask == 'y':
		start2()
	else:
		start()
def editFile():
	file = open(output, "r")
	string = file.read().replace('\n','').replace('-', ' ')
	jump = ")"
	symbols = "][(,' "
	for char in jump:
		string = string.replace(char,"\n")
	for char in symbols:
		string = string.replace(char,"")
	#print (string)
	def changeFile():
		f = open(output, "w")
		f.write (string)
		f.close()

	changeFile()
	print("Proces Finished!!")
	print('Check the file "' + output + '"')

def start():
	clear()
	banner()
	tips()
	mklist()
	ask()

def start2():
	Permutation()
	mkfile()
	clear()
	banner()
	editFile()
	

start()
