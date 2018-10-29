import string
import sys
#################################################################################
# Will Lackey
# 2018
#
# This is a program for creating and manipulating matrices for Discrete Time Markov Chains
#
# Currently Supports:
#	Transient Distribution
#	Occupancy Times
#	Cost Model
#	Matrix Sums
#	Matrix Multiplication 
#
# ASSUME ALL MATRICES ARE N x N
#
# To Do:
#	periodic or aperiodic
################################################################################


class Matrix:
	'Base class for matrices'
	def __init__(self, name, n, a):
		self.name = name
		self.n = n
		self.a = a

def cost_model(a, c):

	big_c = expand_c(c, len(a))

	g = matrix_multiplication(a, big_c)

	small_g = [0 for x in range(len(a))]
	for i in range(len(a)):
		small_g[i] = g[i][0]

	return small_g

def expand_c(c, num):

	new_matrix = [[0 for x in range(num)] for y in range(num)]

	for i in range(num):
		new_matrix[i][0] = c[i]

	return new_matrix

def print_c(a):
	x = len(a)
	
def print_to_console(a):
	ax = len(a[0])
	ay = len(a)
	print("")
	for y in range(ay):
		print("|", end = "")
		for x in range(ax):
			print(" %.4f " %(a[y][x],), end = "")
		print("|")
	print("")

def occupancy_time(a, r):
	m0 = m_identity(len(a))
	m1 = a
	i = 2
	sum = sum_of_matrix(m0, m1)
	
	for i in range(2, r + 1):

		sum = sum_of_matrix(sum, trans_dist(a, i))
	
	return sum 

def sum_of_matrix(a, b):
	x = len(a[0])
	y = len(a)
	new_matrix = [[0 for x1 in range(x)] for y1 in range(y)]

	for j in range(y):
		for i in range(x):
			new_matrix[j][i] = a[j][i] + b[j][i]

	return new_matrix

def trans_dist(a, num):
	temp = a
	for i in range(num - 1):
		temp = matrix_multiplication(temp, a)
	return temp

def matrix_multiplication(a, b):
	ax = len(a[0])
	ay = len(a)
	new_matrix = [[0 for x in range(ax)] for y in range(ay)]

	for y in range(ay):
		for x in range(ax):
			for i in range(ax):
				new_matrix[y][x] = new_matrix[y][x] + (b[i][x] * a[y][i])
	return new_matrix

def m_identity(num):
	new_matrix = [[0 for x in range(num)] for y in range(num)]
	for y1 in range(num):
		for x1 in range(num):
			if (x1 == y1):
				new_matrix[y1][x1] = 1

	return new_matrix

def enter_matrix(n):
	a = [[0 for x in range(n)] for y in range(n)]
	print("Enter the matrix, line by line, seperated by a space.")
	for x in range(n):
		val = 0
		j = input('')
		for i in j.split(' '):
			a[x][val] = float(i)
			val = val + 1

	return a

def enter_c(num):
	a = [0 for x in range(num)]
	print("Enter c, seperated by a space.")
	j = input('')
	n = j.split(' ')
	for i in range(num):
		#print("n = " + n)
		a[i] = float(n[i])
	return a

if __name__ == '__main__':

	process = ""
	n = int(input("Enter the height/width of your N x N matrix.\n"))
	a = enter_matrix(n)
	inital = Matrix("inital", n, a)
	while(process != "end"):
		print("---------------------------------------------------")
		process = input("\n\nWhat action would you like to preform?\n\ntrandist = Transient Distribution\n\nocctime = Occupancy Time\n\ncostmodel = Cost Model\n\nsum = Sum of Two Matricies\n\nmatrixmult = Matrix Multiplication\n\nnewmatrix = Start with a new matrix\n\nviewmatrix = View inital and resulting matrices\n\nend = Quit\n\n")
		print("")
		
		if process == ("trandist"):
			isaNum = False
			num = int(input("According to what n?\n"))	
			result = Matrix("result", inital.n, trans_dist(inital.a, num))
			print_to_console(result.a)

		elif process == ("occtime"):
			r = int(input("According to what r?\n"))
			#print_to_console(occupancy_time(a, r))
			result = Matrix("result", inital.n, occupancy_time(inital.a, r))
			print_to_console(result.a)

		elif process == ("sum"):
			print('\nSecond Matrix')
			ans = input("Use (n)ew matrix or last (r)esult?\n")
			if ans == ("n"):
				b = enter_matrix(inital.n)
			else:
				b = result.a
			#print_to_console(sum_of_matrix(a, b))
			result = Matrix("result", inital.n, sum_of_matrix(inital.a, b))
			print_to_console(result.a)

		elif process == ("matrixmult"):
			print('\nSecond Matrix')
			ans = input("Use (n)ew matrix or last (r)esult?\n")
			if ans == ("n"):
				b = enter_matrix(inital.n)
			else:
				b = result.a
			#print_to_console(matrix_multiplication(a, b))
			result = Matrix("result", inital.n, matrix_multiplication(inital.a, b))
			print_to_console(result.a)

		elif process == ("costmodel"):
			c = enter_c(inital.n)
			print(cost_model(inital.a, c))

		elif process == ("newmatrix"):
			n = int(input("Enter the height/width of your matrix.\n"))
			a = enter_matrix(n)
			inital = Matrix("inital", n, a)

		elif process == ("viewmatrix"):
			print("Inital:")
			print_to_console(inital.a)
			print("Result:")
			print_to_console(result.a)

		elif process == ("end"):
			break
		else:
			print("Sorry, command not regognized. Please try again.")


		
	