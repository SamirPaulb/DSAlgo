# https://leetcode.com/problems/encode-and-decode-tinyurl/

# https://youtu.be/VyBOaboQLGc
class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.n = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encodeMap:
            self.n += 1
            shortUrl = self.n
            self.encodeMap[longUrl] = shortUrl
            self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decodeMap[shortUrl]

# Time: O(1)
# Space: O(N) ; where N is number of longUrl
    
    
import string
class Codec:
    def __init__(self):
        self.chars = string.ascii_letters + string.digits
        # self.chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.encodeMap = {}
        self.decodeMap = {}
    
    def getShortUrl(self):
        code = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code
        
    def encode(self, longUrl: str) -> str:
        shortUrl = self.getShortUrl()
        while shortUrl in self.encodeMap:
            shortUrl = self.encodeMap()
        self.encodeMap[longUrl] = shortUrl
        self.decodeMap[shortUrl] = longUrl
        return self.encodeMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]
    
    

    