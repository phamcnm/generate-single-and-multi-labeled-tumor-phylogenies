# !/bin/bash
# ptst.sh
# This script will generate all unrooted, n single-labeled vertices trees
# Takes in one argument n, the number of nodes

### Notes
#
# This script will create 2 folders, n_nodes_dot_files and n_nodes_png_files 
# The n_nodes_dot_files folder will store all the dot files of the trees
# The n_nodes_png_files folder will store all the png images of the trees
#
# This script will create 3 text files, newick.txt, readable_newick.txt and prufer.txt
# newick.txt will store all the newick representations of the trees
# readable_newick.txt will store all the newick reprentations, formatted for readability
# prufer.txt will store all the prufer sequences that are generated
#
# All files and folders with the same argument n will be remade when the script is run
#

### Sets Up
# creates the directories

rm -r -f ${1}_nodes_dot_files
rm -r -f ${1}_nodes_png_files
mkdir -p ${1}_nodes_dot_files
mkdir -p ${1}_nodes_png_files

# creates a text file to store all newick representations of the trees
> newick_readable.txt
echo "#n = ${1}, first collumn: the prufer sequence; second column: the root; third column: the newick representation" > newick.txt

### Generates the first prufer sequence
PRUFER=""
for (( i=1; i<=$(($1-3)); i++))
do
	PRUFER+="1 "
done
PRUFER+="1"

# prints it onto prufer.txt
echo $PRUFER > prufer.txt

### Creates the dot files and render them into png files

# z is the number of trees
z=$(($1**($1-2)))

# iterates through each tree
IFS=' '

for (( i=1; i<=$(($z-1)); i++ ))
do

	# formats the name of the files
	read -a strarr <<< $PRUFER
	pruf_file=""
	for val in "${strarr[@]}";
	do
		pruf_file+="$val"
	done

	# name of the file
	FILE=${1}_nodes_[${pruf_file}]_prufer

	# runs prufer-to-tree
	python3 ptst.py newick.txt newick_readable.txt > "${1}_nodes_dot_files/${FILE}.dot" < prufer.txt

	# increases prufer code, saving to variable PRUFER
	PRUFER=$(python3 inc.py < prufer.txt)

	# prepends the increased prufer code to prufer.txt
	printf '%s\n%s\n' "$PRUFER" "$(cat prufer.txt)" > prufer.txt

	# converts dot to png
	dot -Tpng "${1}_nodes_dot_files/${FILE}.dot" -o "${1}_nodes_png_files/${FILE}.png"
done

# for the last one
read -a strarr <<< $PRUFER
pruf_file=""
for val in "${strarr[@]}";
do
	pruf_file+="$val"
done

FILE=${1}_nodes_[${pruf_file}]_prufer
python3 ptst.py newick.txt newick_readable.txt > "${1}_nodes_dot_files/${FILE}.dot" < prufer.txt
dot -Tpng "${1}_nodes_dot_files/${FILE}.dot" -o "${1}_nodes_png_files/${FILE}.png"

