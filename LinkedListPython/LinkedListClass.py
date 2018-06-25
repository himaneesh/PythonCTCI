'''
Created on 24-Jun-2018

@author: gsPC
'''



class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0;
    def getSize(self):
        return self.size;
    def insert(self,data):
        if(self.head):
            self.__insertWithHead(data)
        else:
            self.__insertWithouHead(data)
        print("Inserted "+ str(data))
    def delete(self,data):
        if(self.head is None):
            print( "Invalid Access")
        elif(self.head.data == data and self.head.next is None):
            self.head=None
            self.size=0
            return "Deleted"+" "+str(data)
        elif(self.head.data==data):
            self.head = self.head.next;
            self.size-=1
            return "Deleted"+" "+str(data)
        else:
            curr=self.head
            nxt=curr.next
            while(nxt is not None):
                if(nxt.data==data):
                    curr.next=nxt.next
                    nxt=None
                    self.size-=1
                    return "Deleted"+" "+str(data)
                curr=nxt
                nxt=curr.next
                
    def printList(self):
        print("---------------------------")
        if(self.head):
            curr = self.head
            while(curr is not None):
                print(curr.data)
                curr=curr.next
        else:
            print( "Invalid Access")
    
    def __insertWithHead(self,data):
        curr=self.head
        prev=None
        while(curr is not None):
            prev=curr
            curr=curr.next
        curr=Node(data);
        prev.next=curr
        self.size+=1
    def __insertWithouHead(self,data):
        self.head = Node(data)
        self.size=1;
        
    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def getdata(self):
        return self.data
    def getNextNode(self):
        return self.next
    def setNextNode(self,node):
        self.next = node
    def setdata(self,data):
        self.data = data
        