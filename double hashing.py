#double hashing
def insert(l, size):
    hash_list = [False] * size
    
    for item in l:
        h1k = item % size
        h2k = 1 + (item % (size - 1))
        for i in range(size):
            hk = (h1k + i * h2k) % size
            if hash_list[hk] == False:
                hash_list[hk] = item
                break
        else:
            print("table is full.")
    return hash_list
l =list(map(int,input().split(" ")))
size = int(input())
hash_list = insert(l, size)
print(hash_list)