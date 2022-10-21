content = True
i = 1
with open('log.txt','r') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Python is present and in the line number {i}")
        i = i+1
        