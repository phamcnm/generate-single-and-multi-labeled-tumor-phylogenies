"""ptst.py
==============

@ author
@ dates

This program will convert a prufer code to its tree representation
It takes in two argument, two files to write the tree's newick representation
The first file stores it in a way that is easier to parse for machines
The second file stores it in a human readable way
It reads the prufer sequence from stdin
It prints out the tree in dot syntax, onto stdout
It uses tree.py as the data structures for the trees

"""

import sys
import tree as T


def printTree(prufer):
	"""Converts a prufer sequence into tree, prints the dot syntax onto stdout

	Parameters
	----------
	prufer
		a prufer sequence as a list

	Returns
	-------
	the corresponding tree stored as the data structure from tree.py

	"""
	# creates an empty tree
	t = T.Tree()
	m = len(prufer) # length of the prufer sequence
	print("graph ", end = '')

	# prints out the prufer sequence as the name of the graph
	for i in range(m):
		print(prufer[i], end = '')

	print(" {")

	n = m + 2 # number of vertices
	vertex_set = [0]*n

	# increases the element in vertex_set for each occurence of it in the sequence
	for i in range(n-2):
		vertex_set[prufer[i] - 1] += 1

	# For each number in the sequence, find the first (lowest-numbered) node, j, with degree 0
	# Add the edge (j+1, prufer[i]) to the tree, and decrement the degrees of j and prufer[i]-1.
	for i in range(m):
		for j in range(n):
			if vertex_set[j] == 0:
				vertex_set[j] = -1
				print("\t%d -- %d" % (j+1, prufer[i]))
				t.add([j+1, prufer[i]])
				vertex_set[prufer[i]-1] += -1
				break
	j = 0
	edge = []
	# Two nodes with degree 0 will remain. They make the last edge.
	for i in range(n):
		if vertex_set[i] == 0 and j == 0:
			print("\t%d -- " %(i+1), end = '')
			edge.append(i+1)
			j += 1
		elif vertex_set[i] == 0 and j == 1:
			print(i+1)
			edge.append(i+1)
	t.add(edge)

	print("}")

	return t


def main():
	"""main function

	Converts the prufer sequence to tree
	Writes the newick represation of the tree to a file

	"""
	# reads the prufer sequence, on the first line, from stdin
	# stores it in a list
	prufer = list(map(int, sys.stdin.readline().split()))

	# converts to tree
	t = printTree(prufer)

	g = open(str(sys.argv[1]), "a")

	# opens a file to write the newick format
	f = open(str(sys.argv[2]), "a")
	f.write("--------------------------------\n")
	f.write("prufer sequence is %s\n" % prufer)

	# iterates to set each node to be the root
	n = len(prufer) + 2 # the number of nodes
	for i in range(n):
		newick = t.printNewick(i+1)
		g.write("%s\t%d\t%s\n" %(prufer,i+1,newick))
		f.write("root is %d: " % (i+1))
		f.write("%s\n" %(newick))	
	f.write("\n")
	f.close()
	g.close()


if __name__ == "__main__":
	main()

