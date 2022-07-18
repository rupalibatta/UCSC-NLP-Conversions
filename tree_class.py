class Tree:

    def __init__(self, relation, var, value):
        self.child_value = None
        self.child_rel = None
        self.child_var = None
        self.relation = relation
        self.val = value
        self.var = var
        self.tree = []
        self.node_dict = {}
        self.tree.append(self.val)

    def child(self, child_rel, child_var, child_value, new_level, same_level, root_branch):
        self.child_var = child_var.strip()
        self.child_rel = child_rel
        # self.child_value = child_value
        # """
        # When the same variable is repeated twice, I need to fetch the value from the dict
        # print(len(child_value), child_value)
        if child_value == "" and len(child_value) == 1:
            # if len(child_value) > 1:
            self.child_value = self.node_dict[self.child_var]
        else:
            self.child_value = child_value
            self.node_dict[self.child_var] = self.child_value

        prev_type = type(self.tree[-1][-1])
        if new_level:
            if root_branch:
                # Adding the first big list that contains ALL the children
                self.tree.append([self.child_value])
            else:
                # Adding a new list of children to the bigger list
                if prev_type == list:
                    # A child of a child
                    self.tree[-1][-1].append([self.child_value])
                else:
                    self.tree[-1].append([self.child_value])
        elif same_level:
            # Adding a child to the smaller list of children already created
            # However, a new list does not need to be made
            if root_branch:
                self.tree[-1].append(self.child_value)
            else:
                self.tree[-1][-1].append(self.child_value)
        else:
            if prev_type == list:
                self.tree[-1][-1].append(self.child_value)
            else:
                self.tree[-1].append(self.child_value)

    def __str__(self):
        return f"{self.tree}"


r"""
'(s / see-01\n      
:ARG0 (i / i)\n      
:ARG1 (p / picture\n            
:mod (m / magnificent)\n            
:location (b2 / book :wiki -\n                  
:name (n / name :op1 "True" :op2 "Stories" :op3 "from" :op4 "Nature")\n                  
:topic (f / forest\n                        
:mod (p2 / primeval))))\n      
:mod (o / once)\n      
:time (a / age-01\n            
:ARG1 i\n            
:ARG2 (t / temporal-quantity :quant 6\n                  
:unit (y / year))))'
"""
