#Question : LRU Cache
#Link to the question: https://leetcode.com/problems/lru-cache/


"""
1. Create a doubly linked list which store the key , value
2. In the dictionary , for the particular key store the Node(key, value)
3. Create insertAtHead and delete the node method
4 . for the get(): if key not in cache return -1 , else find the node from the cache and delete from the linked list then add it to the head of linked list and return the value of the node
5 . for put() : if key is in cache then update the node value , delete it from the linked list and insert at the head , else : if len(cache)==capacity of cache then delete the oldest node that is referenced at the tail , then create a new node and store the key and the node in cache and insert it to the head of linkedin list
"""

#Doubly Linked List Class
class Node():
    def __init__(self,key,value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head
        
    def insertAtHead(self,node):
        temp = self.head.next
        node.prev = self.head 
        node.next = temp
        self.head.next = node
        temp.prev = node
    
    def deleteNode(self,node):
        previous_node = node.prev
        next_node = node.next
        previous_node.next = next_node
        next_node.prev = previous_node
        node.next = None
        node.prev = None


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.deleteNode(node)
        self.insertAtHead(node)
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.deleteNode(node)
            self.insertAtHead(node)
        else:
            if len(self.cache)==self.capacity:
                oldest_node = self.tail.prev
                self.cache.pop(oldest_node.key)
                self.deleteNode(oldest_node)
                del oldest_node
            new_node = Node(key,value)
            self.cache[key]= new_node
            self.insertAtHead(new_node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)