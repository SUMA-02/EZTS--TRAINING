#hashing(chaining method)
class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
hash_table = [None] * 10  

def head(head):
    global hash_table
    Head = Node(head)
    Head.next = None
    hash_table[head] = Head

def insert(Head, value):
    val = Node(value)
    if Head.next is None:
        Head.next = val
        val.next = None
    else:
        curr = Head
        while curr.next is not None:
            curr = curr.next
        curr.next = val
        val.next = None

def print_link_list(Head):
    if Head is None:
        print("List is Empty")
        return
    curr = Head
    while curr is not None:
        print(curr.value,end=" ")
        curr = curr.next

def search(key):
    r = key % 10
    curr = hash_table[r]
    while curr is not None:
        if curr.value == key:
            print(f"Key {key} found in hash table.")
            return True
        curr = curr.next
    print(f"Key {key} not found in hash table.")
    return False

K = [10, 16, 62, 100, 20, 80, 72, 7, 76, 99]
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for j in L:
    head(j)
for i in range(len(K)):
    r = K[i] % 10  
    insert(hash_table[r], K[i])
for head_node in hash_table:
    if head_node is not None:
        print_link_list(head_node)
search_key = int(input())
search(search_key)