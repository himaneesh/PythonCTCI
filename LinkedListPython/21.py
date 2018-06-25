'''
Created on 23-Jun-2018

@author: gsPC
'''
from LinkedList.LinkedListClass import LinkedList


def dupsDriver():
    linkedlistT = LinkedList()
    linkedlistT.insert(1)
    linkedlistT.insert(1)
    linkedlistT.insert(1)
    linkedlistT.insert(1)
    linkedlistT.insert(1)
    linkedlistT.insert(5)
    linkedlistT.insert(6)
    linkedlistT.insert(5)
    
    
    dictDup={}
    curr=linkedlistT.head
    while(curr is not None):
        if(dictDup.get(str(curr.data))):
            linkedlistT.delete(curr.data)
        else:
            dictDup.__setitem__(str(curr.data), curr)
        curr=curr.next
        
    dictDup.clear()
    linkedlistT.printList()
    print("Size---")
    print(linkedlistT.getSize())
if __name__ == '__main__':
    dupsDriver()