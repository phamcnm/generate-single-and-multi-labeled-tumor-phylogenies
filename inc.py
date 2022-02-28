"""inc.py
==============

This program will take in a prufer sequence and generate the one that follows it
For example, [2,3,4] is followed by [2,3,5], which is followed by [2,4,1]
It takes in no arguments
It reads from stdin, and prints out the prufer sequence that follows, onto stdout

"""

import sys


def increase(arr):
	"""Prints out the prufer sequence that follows

	Parameters
	----------
	arr
		a prufer sequence as a list

	Returns
	-------
	None
	It mutates the list itself

	"""
	m = len(arr) # length of the prufer sequence
	
	# sets the cursor to be at the farthest right element
	i = m - 1

	# finds the farthest right element that can go up
	while arr[i] == m + 2:

		# if it cannot, move the cursor left
		i += -1

		# if the cursor went pass the farthest left, the sequence is maxed
		if i < 0:
			raise IndexError()

	# increases the sequence by one, at the found spot
	arr[i] += 1

	# sets all elements to the right of the found spot, to be 1
	for j in range(m-1, i, -1):
		arr[j] = 1


def main():
	"""main function

	Prints out the prufer sequence that follows that one it reads in

	"""
	# reads the prufer sequence, on the first line, from stdin
	# stores it in a list
	prufer = list(map(int, sys.stdin.readline().split()))

	# calls the function that mutates the list to store the sequence that follows
	increase(prufer)

	# prints out the new prufer sequence onto stdout
	m = len(prufer) # length of the prufer sequence
	for i in range(m - 1):
		print(prufer[i], end = ' ')
	print(prufer[m-1], end = '')


if __name__ == "__main__":
	main()

	