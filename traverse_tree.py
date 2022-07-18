#csv conversion, tree traversal, node processing
import csv
import re

#convert csv to dictionary
#goes into the main method, dictionary is global
def convertcsv(file):
	with open(file, newline='') as f:
		reader = csv.reader(f)
		mydict = {rows[0]:rows[1:] for rows in reader}
	return mydict

#return qa pair for a node
def process(node, parent_node):
	regex = r'\((.*)\)'
	template_list = mydict[node.relation]
	question_list = []
	#replace the text in parenthesis with the parent node value
	for i in template_list:
		temp = re.match(regex, template_list[i]).group(1)
		#idk how to find 'parent verb' or 'arg 0 verb'
		question_list.append(template_list[i].replace(temp, temp)) #new temp would be the parent word or arg0/1
	#if there's more than 1 question, choose the highest scoring one
	if (len(question_list) > 1):
		question = question_list[0] #I'm just choosing the first one in the array, idk how to find the highest f score
	else:
		question = question_list[0]
	qa_pair_list = [question, node.val]
	return qa_pair_list

#preorder tree traversal
def traverse(tree):
	If tree:
		If tree.relation is “root”:
			parent_node = tree.val
			for i : tree.children
				process(tree.tree[i], parent_node)
				Parent_node = tree.tree[i]
				traverse(tree.tree[i])
		Else:
			for i : tree.children
				process(tree.tree[i], parent_node)
				Parent_node = tree.tree[i]
