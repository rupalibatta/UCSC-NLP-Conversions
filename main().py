from tree_class import Tree
import json


def read_amrs_from_file(filename):
    corpus = {}

    f = open(filename, 'r')
    text = f.read()
    f.close()

    data_items = text.split("\n\n")

    for item in data_items[1:]:
        lines = item.split("\n#")
        sent = amr = fname = ""
        for line in lines:
            if '::snt' in line:
                sent = line[7:]
                # print(sent)
            elif '::save-date' in line:
                amr_info_list = line.split(".txt\n")
                fname = amr_info_list[0][36:]
                # print(fname)
                amr = amr_info_list[1]
                # print(amr)

        corpus[fname] = {"sent": sent, "amr": amr}

    return corpus


def tree(amr_str):
    amr_list = amr_str.split("\n")
    count = 0
    prev_lead_spaces = 0
    for node in amr_list:
        if node == '':
            # When there is no node, I exit the loop immediately
            break
        node1 = node.replace("(", "*")
        node2 = node1.replace("/", "*")
        node3 = node2.replace(")", "*")
        # Getting each node/word, relation, and variable
        node_list = node3.split("*")
        if len(node_list) == 1 or node_list[1] == '':
            # Sometimes the node list does not split correctly or does not have enough
            # arguments so I add a blank argument
            node_list = node_list[0].split()
            node_list.append('')
        leading_spaces = len(node_list[0]) - len(node_list[0].lstrip())
        if count == 0:
            # Creating a node object with the root word
            root = Tree("root", node_list[1], node_list[2])
        else:
            # When there's a new indentation, a new branch is created
            if leading_spaces <= 6:
                # root_branch means a child's parent is the root word
                root_branch = True
            else:
                root_branch = False

            if leading_spaces > prev_lead_spaces or root_branch:
                # New_level means a whole new branch of children
                # same_level means a word is a child of the same parent but a whole new level
                # does not nee to be made
                new_level = True
                same_level = False

            else:
                # No new branch created
                new_level = False
                if leading_spaces == prev_lead_spaces:
                    # A node is still a child of the parent node of the prev node
                    same_level = True
                else:
                    same_level = False
            root.child(node_list[0], node_list[1], node_list[2],
                       new_level, same_level, root_branch)

        count += 1
        prev_lead_spaces = leading_spaces
    # print(root)
    return root


def traverse(tree):
    qa_pair_list = [{"question": "Who did it?", "answer": "Jasmine"},
                    {"question": "Why did she do it?", "answer": "she was tired"},
                    {"question": "When did she do it?", "answer": "after work"}]
    return qa_pair_list


def main():
    corpus = read_amrs_from_file('data/amr-little-prince-v1.6.txt')
    # print(corpus)
    output_dict = {}

    for id in corpus:
        amr_dict = corpus[id]
        output_dict[id] = {}
        for key in amr_dict:
            # Adding  new keys to the output dictionary
            if key == "sent":
                output_dict[id]["sent"] = amr_dict[key]
            if key == "amr":
                output_dict[id]["amr"] = amr_dict[key]
                amr_str = amr_dict[key]
                if amr_str != "(c / chapter\n  :mod 1)":
                    tree1 = tree(amr_str)
                    qa_pair_list = traverse(tree1)
                    output_dict[id]["qa_pairs"] = qa_pair_list
    # print(output_dict)

    json1 = json.dumps(output_dict)
    f = open("output_dict.json", "w")
    f.write(json1)
    f.close()


main()
