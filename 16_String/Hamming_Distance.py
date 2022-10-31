import hashlib

def hamming_distance(chaine1, chaine2):
    return sum(c1 != c2 for c1, c2 in zip(chaine1, chaine2))

def hamming_distance2(chaine1, chaine2):
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(chaine1, chaine2))))

if __name__=="__main__":    
    chaine1 = hashlib.md5("chaine1".encode()).hexdigest()
    chaine2 = hashlib.md5("chaine2".encode()).hexdigest()

    assert len(chaine1) == len(chaine2)

    print(hamming_distance(chaine1, chaine2))

    print(hamming_distance2(chaine1, chaine2))
