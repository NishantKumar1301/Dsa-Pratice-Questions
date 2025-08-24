#Question : LFU Cache
#Link to the question: https://leetcode.com/problems/lfu-cache/

class Node():
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.prev = None

class DoublyLinkedList():
    """ An implementation of doubly linked list.
	Three APIs provided:
    insertAtHead(node): append the node to the head of the linked list.
    deleteNode(node): remove the referenced node. 
    deleteLastNode() : Remove the one from tail, which is the least recently used.
    """

    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head
        self.length = 0 # This denotes the length of the linked list

    def insertAtHead(self,node):
        temp = self.head.next
        node.prev = self.head
        node.next = temp
        self.head.next = node
        temp.prev=node
        self.length+=1
    
    def deleteNode(self,node):
        next_node = node.next
        prev_node = node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        node.next = None
        node.prev = None
        self.length-=1
    
    def deleteLastNode(self):
        if self.length>0:
            last_node = self.tail.prev
            self.deleteNode(last_node)
            return last_node
        return None

class LFUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int

        Three things to maintain:
        1. a dict, named as `self.cache`, for the reference of all nodes given key.
           That is, O(1) time to retrieve node given a key.
           
        2. Each frequency has a doubly linked list, store in `self.freqMap`, where key
           is the frequency, and value is an object of `DLinkedList`
        
        3. The min frequency through all nodes. We can maintain this in O(1) time, taking
           advantage of the fact that the frequency can only increment by 1. Use the following
		   two rules:
           Rule 1: Whenever we see the size of the DLinkedList of current min frequency is 0,
                   the min frequency must increment by 1.
           Rule 2: Whenever put in a new (key, value), the min frequency must 1 (the new node)
        """
        self.capacity = capacity
        self.cache = {}
        self.freqMap = {}
        self.minFreq = 0
        
    def updateFreq(self,node):
        """
        This is a helper function that used in the following two cases:
        
            1. when `get(key)` is called; and
            2. when `put(key, value)` is called and the key exists.
         
        The common point of these two cases is that:
        
            1. no new node comes in, and
            2. the node is visited one more times -> node.freq changed -> 
               thus the place of this node will change
        
        The logic of this function is:
        
            1. pop the node from the old DLinkedList (with freq `f`)
            2. append the node to new DLinkedList (with freq `f+1`)
            3. if old DlinkedList has size 0 and self.minfreq is `f`,
               update self.minfreq to `f+1`
        """
        freq = node.freq
        dll = self.freqMap[freq]
        dll.deleteNode(node)
        if dll.length==0 and freq == self.minFreq:
            self.minFreq+=1
        node.freq+=1
        new_freq = node.freq
        if new_freq not in self.freqMap:
            self.freqMap[new_freq]=DoublyLinkedList()
        self.freqMap[new_freq].insertAtHead(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.updateFreq(node)
        return node.value
        

    def put(self, key, value):
        """
        If `key` already exists in self._node, we do the same operations as `get`, except
        updating the node.val to new value.
        
        Otherwise, the following logic will be performed
        
        1. if the cache reaches its capacity, pop the least frequently used item. (*)
        2. add new node to self.freqMap
        3. add new node to the DLinkedList with frequency 1
        4. reset self._minfreq to 1
        
        (*) How to pop the least frequently used item? Two facts:
        
        1. we maintain the self.minfreq, the minimum possible frequency in cache.
        2. All cache with the same frequency are stored as a DLinkedList, with
           recently used order (Always append at head)
          
        Consequence? ==> The tail of the DLinkedList with self.minfreq is the least
                         recently used one, pop it...
        
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity ==0:
            return 
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.updateFreq(node)
        else:
            if len(self.cache)==self.capacity:
                dll = self.freqMap[self.minFreq] #This linked list stores the minFreq element
                oldest_node = dll.deleteLastNode()
                if oldest_node:
                    self.cache.pop(oldest_node.key)
            #Insert new node
            new_node = Node(key,value)
            self.cache[key]=new_node
            self.minFreq=1
            if self.minFreq not in self.freqMap:
                self.freqMap[self.minFreq] = DoublyLinkedList()
            self.freqMap[self.minFreq].insertAtHead(new_node)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)