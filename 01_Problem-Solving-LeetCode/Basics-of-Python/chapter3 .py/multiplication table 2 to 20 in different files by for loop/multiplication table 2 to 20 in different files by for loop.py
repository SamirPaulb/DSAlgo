for i in range(1,21):
    with open(f"table_of_{i}.txt",'w') as f : 
        f.write(f"The Multiplication Table of {i} is Written below:\n")
        for j in range(1,11):
            f.write(f"{i} X {j} = {i*j}\n")
            
        
