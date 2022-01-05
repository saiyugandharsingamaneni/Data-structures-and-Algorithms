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
    def post_traversal(self):
        elements=[]
        #visits left tree
        if self.left:
            elements+=self.left.post_traversal()
        #vists right tree
        if self.right:
            elements+=self.right.post_traversal()
        #vists root
        elements.append(self.data)
        
    def pre_traversal(self):
        elements=[self.data]
        #visits left tree
        if self.left:
            elements+=self.left.append.pre_traversal()
        #visits right tree
        if self.right:
            elements+=self.right.append.pre_traversal()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
        
def build_tree(elements):
    root=BinarySearchTreeNode(elements[0])
    
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    numbers = [15,12,7,14,27,20,23,88 ]

    numbers_tree = build_tree(numbers)
    print("Input numbers:",numbers)
    print("Min:",numbers_tree.find_min())
    print("Max:",numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_traversal())
    print("Post order traversal:", numbers_tree.post_traversal())