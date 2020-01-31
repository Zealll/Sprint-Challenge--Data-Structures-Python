import time

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def create(self, value):
        node = Node(value)

        if not self.root:
            self.root = node
        else:

            current_node = self.root

            while True:
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = node
                        break
                    else:
                        current_node = current_node.right


    def lookup(self, value):
        if not self.root:
            return False

        current_node = self.root

        while current_node:

            if value < current_node.value:
                current_node = current_node.left

            elif value > current_node.value:
                current_node = current_node.right

            elif value == current_node.value:
                return True


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# Original
# Run Time: +-6 secs O(n*n)

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# ===== MVP SOLUTION =====

# Run Time: +-0.05 secs O(n)

bst = BST()

duplicates = []
for name in names_1:
    bst.create(name)

for name in names_2:
    if bst.lookup(name):
        duplicates.append(name)




# ============ STRETCH SOLUTION ===========

# Solution 1 - List Comprehension
# Run Time: +-1 sec

# duplicates = [ i for i in names_1 if i in names_2 ]


# Solution 2 - Binary Search
# Run Time: +-0.7 secs

# duplicates = []

# sort = sorted(names_2)

# def b_search(arr, target):
#     if len(arr) == 1:
#         # print(arr[0])
#         return arr[0]

#     first = arr[ :len(arr) // 2]
#     second = arr[len(arr) // 2: ]

#     if target > first[len(first) - 1]:
#         return b_search(second, target)
#     elif target < second[0]:
#         return b_search(first, target)



# for name in names_1:
#     if name == b_search(sort, name):
#         duplicates.append(name)




# Solution 3 - cache
# Run Time: +-0.005 This solution is on steroids

# duplicates = []
# cache = {}

# for name in names_1:
#     cache[name] = True

# for name in names_2:
#     if name in cache:
#         duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
