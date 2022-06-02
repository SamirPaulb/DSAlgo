# https://leetcode.com/problems/lru-cache/

# Using LinkedList and Dictionary  => Optimized for Interviews
# https://youtu.be/akFRa58Svug
# https://youtu.be/UudCSLREm08


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key])
            self.makeRecent(self.dic[key])
            return self.dic[key].val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
            self.dic[key] = ListNode(key, value)
            self.makeRecent(self.dic[key])
        else:
            if len(self.dic) == self.capacity:
                del self.dic[self.head.key]
                self.remove(self.head)
            self.dic[key] = ListNode(key, value)
            self.makeRecent(self.dic[key])
        
    def remove(self, node):
        if self.head.key == node.key:
            self.head = self.head.next
        elif self.tail and self.tail.key == node.key:
            self.tail = self.tail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
    def makeRecent(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node






# Using LinkedList and Dictionary  => Optimized for Interviews

class Node(object):
    def __init__(self, key, x):
        self.key = key
        self.value = x
        self.next = None
        self.prev = None
    
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity    
        self.dic = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            self.makeMostRecent(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.dic:
            # Invalidate oldest if required:
            if len(self.dic) == self.capacity:
                del self.dic[self.head.key]
                self.removeHead()
            node = Node(key, value)
            self.dic[key] = node
        else:
            # Update the value:
            node = self.dic[key]
            node.value = value
        self.makeMostRecent(node)
            
    def makeMostRecent(self, node):
        if self.head and self.head.key == node.key:
            self.removeHead()
        # Make this item the most recently accessed (tail):
        if self.tail and not self.tail.key == node.key:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            node.next = None
            self.tail.next = node  # Old tail's next is the node.
            node.prev = self.tail  # Node's previous is the old tail.
        self.tail = node  # New tail is the node.
        if not self.head:
            self.head = node  # If this is the first item make it the head as well as tail.
    
    def removeHead(self):
        self.head = self.head.next
        if self.head:
            self.head.prev = None



'''
# Using OrderedDict Dictionary  => Optimized but NOT for Interviews
class LRUCache:

    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.capacity = capacity
        self.cacheLen = 0
        
    def get(self, key):
        if key in self.dic:
            ans = self.dic.pop(key) 
            self.dic[key] = ans  # set this this key as new one (most recently used)
            return ans
        else:
            return -1

    def put(self, key, value):
        if key in self.dic:
            ans = self.dic.pop(key)
            self.dic[key] = ans
        else:
            if self.cacheLen >= self.capacity:  # self.dic is full
                self.dic.popitem(last = False)  # pop the last recently used element (lru)
                self.cacheLen -= 1
                
            self.dic[key] = value
            self.cacheLen += 1
            
# Time Complexity = O(1) ; as search and pop operation from dictionary is of O(1)
# Space Complexity = O(N) ; for making the dictionary
'''


'''
# Using Array and Dictionary  => NOT Optimized
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = {}
        self.arr = []
        
    def get(self, key):
        if key in self.arr: 
            i = self.arr.index(key)
            res = self.arr[i]
            self.arr.pop(i)
            self.arr.append(res)
            return self.dic[res]
        else: return - 1

    def put(self, key, value):
        if key in self.arr:
            i = self.arr.index(key)
            self.arr.pop(i)
            self.arr.append(key)
            self.dic[key] = value
        else:
            if len(self.arr) >= self.capacity:
                self.arr.pop(0)
            self.arr.append(key)
            self.dic[key] = value
            
# Time Complexity: O(N) ; as O(N) for searching in array and O(N) for rearranging the indexing after popping. so time = O(N) + O(N) = O(N)
# Space Complexity: O(N) ; for making the array and dictionary to store key and value
'''