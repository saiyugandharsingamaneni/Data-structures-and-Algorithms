class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_begining(self,data):   #inserting_at_begining of the linked list
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        listr=" "
        while itr:
            listr += str(itr.data)+'-->'
            itr = itr.next
             
        print(listr)
    
    def insert_at_end(self,data):    #inserting_at_end of the linked list
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr=itr.next
        
        itr.next=Node(data,None)
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
    def get_length(self):   #get_length of linked_list 
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr=itr.next
            
        return count
        
if __name__=='__main__':       #inserting_data in to linked list
    ll=LinkedList()
    ll.insert_values(["oranges","mangos","grapes","banana"])
    ll.print()
    print("length:",ll.get_length())