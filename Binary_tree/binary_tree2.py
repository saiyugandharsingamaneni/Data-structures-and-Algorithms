class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def add_child(self,data):
        if data == self.data:
            return
        if data <self.data:
        #add on the left side of the subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
        #add on the right side of the subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements=[]
        #visits left tree
        if self.left:
            elements+=self.left.in_order_traversal()
            
        #visits root node
        elements.append(self.data)
        
        #visits right tree
        if self.right:
            elements+=self.right.in_order_traversal()
        
        return elements
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ =='__main__':
    countries=["INDIA","USA","FRANCE","UK","RUSSIA","GERMANY","CHINA","JAPAN","CANADA"]
    country_tree=build_tree(countries)
    print(country_tree)
    print("UK in the list",country_tree.search("UK"))
        
        