class TextEditor:

    def __init__(self):
        self.txt = ''  
        self.ptr = 0  

    def addText(self, text: str) -> None:
        self.txt = self.txt[:self.ptr] + text + self.txt[self.ptr:]
        self.ptr += len(text)  

    def deleteText(self, k: int) -> int:
        org = len(self.txt)  
        self.txt = self.txt[:max(self.ptr - k, 0)] + self.txt[self.ptr:]
        self.ptr = max(self.ptr - k, 0)  
        return org - len(self.txt)

    def cursorLeft(self, k: int) -> str:
        self.ptr = max(self.ptr - k, 0)  
        return self.txt[max(0, self.ptr - 10):self.ptr]

    def cursorRight(self, k: int) -> str:
        self.ptr = min(self.ptr + k, len(self.txt))  
        return self.txt[max(0, self.ptr - 10):self.ptr]
