import numpy as np
import time

def func(int a=0):
	print(a)
	print("this is func")
	
class thing():
	def _init_(self):
		pass
	def my_func(self, int a = 3, int b = 4):
		func(a)
		func(b)
	
if __name__ == __main__ :
	func()
 
