
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")


    def insert(self, word):
        node = self.root
    #traverse the word character by character 
        for char in word:
    #check if the character is there in the list of children 
            if char in node.children:
                node = node.children[char]
            else:
    # else make a new TrieNode corresponding to that character 
                new_node = TrieNode(char)
    # add the new node to the list of children 
                node.children[char] = new_node
                node = new_node
    #after traversig the word set .is_end to true for the last #char
        node.is_end = True

    def dfs(self, node, pre):
        if node.is_end:
            self.output.append((pre + node.char))
        for child in node.children.values():
            self.dfs(child, pre + node.char)


    def search(self, x):
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.output = []
        self.dfs(node, x[:-1])
        return self.output


file_path = "input.txt"
with open(file_path, 'r') as f:
    data = f.read()

lines = data.split()
digits = len(lines[0])
tr = Trie()

for line in lines:
    tr.insert(line)

oxygenrating = ""
for i in range(0, digits):
   ones = tr.search(oxygenrating + "1")
   print(f"there are {len(ones)} ones")
   zeroes = tr.search(oxygenrating + "0")
   print(f"there are {len(zeroes)} zeroes")

   if not ones:
       oxygenrating += "0"
   elif not zeroes:
       oxygenrating += "1"
   elif (len(ones) >= len(zeroes)):
       oxygenrating += "1"
   else:
       oxygenrating += "0"

   print(oxygenrating)

co2rating = ""
for i in range(0, digits):
   ones = tr.search(co2rating + "1")
   print(f"there are {len(ones)} ones")
   print(tr.search(co2rating + "1"))
   zeroes = tr.search(co2rating + "0")
   print(f"there are {len(zeroes)} zeroes")
   print(tr.search(co2rating + "0"))

   if not zeroes:
       co2rating += "1"
   elif not ones:
       co2rating += "0"
   elif (len(zeroes) <= len(ones)):
       co2rating += "0"
   else:
       co2rating += "1"

   print(co2rating)

print(f"oxygenrating: {oxygenrating} or {int(oxygenrating, 2)}")
print(f"co2rating: {co2rating} or {int(co2rating, 2)}")
print(f"life support rating: {int(oxygenrating, 2) * int(co2rating, 2)}")


