class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
    def insertList(self,data):
        Temp=Node(data)
        Temp.next=self.head
        self.head=Temp
        del Temp
    def printList(self):
        start=self.head        
        if start==None:
            print(" \n Linked List is empty \n")
        else:
            while start!=None:
                print(" The value is ->",start.data)
                start=start.next
    def delNode(self,data):
        start=self.head        
        if start==None:
            print(" \n Linked List is empty \n")
        else:
            curr=start
            while curr!=None:
                if curr.data==data:                                   
                     #node to delete
                    break
                else:
                    prev=curr 
                    curr=curr.next
            if curr ==None:
                print(" No matching Node ")                
            elif curr==self.head: #first node
                self.head=curr.next
                print(" Node deleted ")
                del curr
            else:
                print(" Node deleted ") 
                prev.next=curr.next
                del curr              
    
    def delList(self):
        start=self.head
        if start==None:
            print(" \n Linked List is empty \n")
        else:
            while start!=None:
                Temp=start
                start=start.next
                del Temp
        
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList()
    while True:
        # Menu for the linked list
        print(" Menu for linked list oeration")
        print(" Press 1 to insert")
        print(" Press 2 to delete a node")
        print(" Press 3 to delete the entire list")
        print(" Press 4 to print the list")
        print(" press any key to exit")
        Data=str(input(" Enter your choice ->"))
        # input id takes as string to incroporate any key
        if Data=='1':
            keyI=input(" Enter the number ->")
            llist.insertList(keyI)
        elif Data=='2':
            keyD=input(" Enter the number ->")            
            llist.delNode(keyD)
        elif Data=='3':
            llist.printList()
        else:
            break
