# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 06:43:24 2019

@author: prakhar prakash
"""
"""
inserting a node at the end of linded list

"""
class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None
    
     
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            loc = self.head
            while loc.nextval is not None:
                loc = loc.nextval
            loc.nextval = new_node
            new_node.nextval = None
        
        
        
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.dataval)
            current = current.nextval
        
        
        
        
        
        
list1 = linkedlist() 
list1.insert('monday') 
list1.insert('Tuesday')
list1.insert(34)
list1.traverse()
     