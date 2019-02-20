# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 21:00:46 2019

@author: prakhar prakash
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
        count = 1
        loc = int(input('Enter the position to insert the node'))
        start = self.head
        
        
      # if self.head is None:
      #      print('There is no node therefore inserting at first position')
      #      self.head = new_node 
            
            #count+=1  unnecessary     
            
        if loc is 1:
            if self.head is None:
                print('There is no node therefore inserting at first position')
                self.head = new_node
            else:
                new_node.nextval = self.head
                self.head = new_node
                
            
            
        else:
            while count < loc-1:
                start = start.nextval
                count += 1
            if count is loc-1:
                new_node.nextval = start.nextval
                start.nextval = new_node
            
            
        
        

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.dataval)
            current = current.nextval        
            
            
list1 = linkedlist() 
list1.insert('January')
list1.insert('February')
list1.insert('March')
list1.insert('December')


list1.traverse()          