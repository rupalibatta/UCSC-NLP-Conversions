from tree_class import Tree


def tree(amr_str):
    amr_list = amr_str.split("\n")
    count = 0
    prev_lead_spaces = 0
    for node in amr_list:
        node1 = node.replace("(", "*")
        node2 = node1.replace("/", "*")
        node3 = node2.replace(")", "*")
        # Getting each node/word, relation, and variable
        node_list = node3.split("*")
        if len(node_list) == 1:
            node_list = node_list[0].split()
            node_list.append("")
        # print(node_list)
        leading_spaces = len(node_list[0]) - len(node_list[0].lstrip())
        if count == 0:
            # Creating a node object with the root word
            root = Tree("root", node_list[1], node_list[2])
        else:
            # When there's a new indentation, a new branch is created
            if leading_spaces == 6:
                # root_branch means a child's parent is the root word
                root_branch = True
                # new_level = True
            else:
                root_branch = False

            if leading_spaces > prev_lead_spaces or root_branch:
                # New branch means a whole new branch of children
                # Child means a word is a child but a whole new branch/level
                # does not nee to be made
                new_level = True
                same_level = False

            else:
                # No new branch created
                new_level = False
                # root_branch = False
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


def main():

    # """
    amr_str = '(s / see-01\n      :ARG0 (i / i)\n      :ARG1 (p / picture\n' \
              '            :mod (m / magnificent)\n            ' \
              ':location (b2 / book :wiki -\n                  ' \
              ':name (n / name :op1 "True" :op2 "Stories" :op3 "from" :op4 "Nature")\n' \
              '                  :topic (f / forest\n                        ' \
              ':mod (p2 / primeval))))\n      :mod (o / once)\n      ' \
              ':time (a / age-01\n            :ARG1 i\n            ' \
              ':ARG2 (t / temporal-quantity :quant 6\n                  ' \
              ':unit(y / year))))'
    """
    amr_str = '(b2 / be-located-at-91\n      ' \
              ':ARG1 (a3 / and\n            ' \
              ':op1 (p / plant\n                  ' \
              ':ARG1-of (g / good-02))\n            ' \
              ':op2 (p2 / plant\n                  ' \
              ':ARG1-of (b / bad-07))\n            ' \
              ':mod (i / indeed))\n      ' \
              ':ARG2 (a / and\n            ' \
              ':op1 (p3 / planet\n                  ' \
              ':location-of (l / live-01\n                        ' \
              ':ARG0 (p4 / prince\n                              ' \
              ':mod (l2 / little))))\n            ' \
              ':op2 (p5 / planet\n                  ' \
              ':mod (a2 / all)))\n      ' \
              ':ARG1-of (l3 / learn-01\n            ' \
              ':ARG0 (i2 / i)))'
    """
    tree(amr_str)


main()

r"""
'(s / see-01\n' \
'      :ARG0 (i / i)\n' \
'      :ARG1 (p / picture\n' \
'            :mod (m / magnificent)\n' \
'            :location (b2 / book :wiki -\n' \
'                  :name (n / name :op1 "True" :op2 "Stories" 
                   :op3 "from" :op4 "Nature")\n' \
'                  :topic (f / forest\n                        
                        :mod (p2 / primeval))))\n      
       :mod (o / once)\n      
       :time (a / age-01\n            
             :ARG1 i\n            
             :ARG2 (t / temporal-quantity :quant 6\n                  
                  :unit (y / year))))'
                  
                  
(b2 / be-located-at-91
      :ARG1 (a3 / and
            :op1 (p / plant
                  :ARG1-of (g / good-02))
            :op2 (p2 / plant
                  :ARG1-of (b / bad-07))
            :mod (i / indeed))
      :ARG2 (a / and
            :op1 (p3 / planet
                  :location-of (l / live-01
                        :ARG0 (p4 / prince
                              :mod (l2 / little))))
            :op2 (p5 / planet
                  :mod (a2 / all)))
      :ARG1-of (l3 / learn-01
            :ARG0 (i2 / i)))

"""
