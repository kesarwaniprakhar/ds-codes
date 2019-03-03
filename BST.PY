# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:52:27 2019

@author: prakhar prakash
"""

class Node:
    def __init__(self,dataval,key):
        self.dataval = dataval
        self.leftnextnode = None
        self.rightnextnode = None
        self.key = key
        
class BST:
    
    def __init__(self):
        self.root = None
       
        
    def insert(self,data,keyval,node):  
        if node is None:
            self.root = Node(data,keyval)
           
        
        else: 
            
            if keyval< node.key:
                if node.leftnextnode is None:
                    node.leftnextnode = Node(data,keyval)
                    
                    
                else:
                    self.insert(data,keyval,node.leftnextnode)
                
              
            else:
                if keyval > node.key:
                    if node.rightnextnode is None:
                        node.rightnextnode = Node(data,keyval)
                        
                        
                        
                    else:
                        self.insert(data,keyval,node.rightnextnode)
                
    
    def traverse(self,node):
        if node != None:
           self.traverse(node.leftnextnode)
           print(node.dataval)
           self.traverse(node.rightnextnode)
        
        
        
tree1 = BST()
tree1.insert('prakhar',5,tree1.root)
tree1.insert('prakash',1,tree1.root)
tree1.insert('kesarwani',8,tree1.root) 
tree1.insert('58',9,tree1.root)
tree1.traverse(tree1.root)               