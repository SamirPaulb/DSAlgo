# Using LinkedList and Dictionary  => Optimized for Interviews





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