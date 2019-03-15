# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 23:46:55 2019

@author: prakhar prakash
"""

class Node:
    def __init__(self,dataval = None):
        self.dataval = dataval
        self.nextval = None
        
        
class linkedlist:
    def __init__(self):       
        self.head = None
        
    def insertbeg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nextval = self.head
            self.head = new_node
        
        
        
        
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.dataval)
            current = current.nextval
            
list1 = linkedlist()
list1.insertbeg(46)
list1.insertbeg(96)
list1.insertbeg('prakhar')
list1.insertbeg('pawan')
list1.traverse()           