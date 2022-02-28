"""tree.py
"""

from sortedcontainers import SortedSet, SortedDict


class Tree:
	"""
	A class used to represent an unrooted tree

	Attributes
	----------
	tree
		a sorted dictionary
		keys are nodes
		values are the set of adjacent nodes of each key

    Methods
    -------
    add(endpoints)
    	adds an edge to the tree

    """

	def __init__(self):
		"""Initializes an empty unrooted tree
		"""
		self.tree = SortedDict()


	def add(self, endpoints):
		"""Adds an edge to the tree

		Parameters
		----------
		endpoints
			an edge represented as a list of two endpoints

		Raises
		------
		IndexError
			if the length of the endpoints list is not two, there is an error

		"""
		if len(endpoints) != 2:
			raise IndexError("an edge must have two endpoints")

		# updates the values for endpoints[0]
		if endpoints[0] not in self.tree:
			self.tree[endpoints[0]] = SortedSet()
		self.tree[endpoints[0]].add(endpoints[1])

		# updates the values for endpoints[1]
		if endpoints[1] not in self.tree:
			self.tree[endpoints[1]] = SortedSet()
		self.tree[endpoints[1]].add(endpoints[0])


	def print(self):
		"""Prints out the tree
		"""
		print(self.tree)


	def printNewick(self, root):
		"""Obtains the newick representation of the tree

		Parameters
		----------
		root
			the root of this tree

		Returns
		-------
		A string that is the newick representation

		"""
		# this method is similar to a breadth-first search

		# sets the string to be the root, for starters
		newick = str(root)

		# visited[] to keep track of visited node
		visited = [root]

		# queue[] to keep track of nodes to visit next
		queue = [root]

		while queue:
			curr = queue.pop(0)

			# the set of edges of curr
			nexts = self.tree[curr]

			# the string to be inserted
			# will be in the format "(" + the children + ")"
			inserting = ""

			# finds the index to insert the children
			idx = newick.find(str(curr)) 
			
			# iterates through the edges of curr, in ascending order
			for n in nexts:

				# visits n if it's not yet
				if n not in visited:
					visited.append(n)
					queue.append(n)

					# adds n to the string to be inserted
					inserting += "%s " % n

			inserting = inserting[:-1] # strips the last " "

			# inserts the string in
			if inserting != "":
				newick = newick[:idx] + "(%s)" % inserting + newick[idx:]

		return newick

