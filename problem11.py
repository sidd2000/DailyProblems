"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a dictionary of all possible 
query strings, return all strings as a list in the dictionary that have s as a prefix.

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

"""

# We preprocess the data into a trie
 
class TrieNode(): 
	def __init__(self): 
		
		# Initialising one node for trie 
		self.children = {} 
		self.last = False

class Trie(): 
	def __init__(self): 
		
		# Initialising the trie structure. 
		self.root = TrieNode() 
		self.word_list = [] 

	def formTrie(self, keys): 
		
		# Forms a trie structure with the given set of strings 
		# if it does not exists already else it merges the key 
		# into it by extending the structure as required 
		for key in keys: 
			self.insert(key) # inserting one key to the trie. 

	def insert(self, key): 
		
		# Inserts a key into trie if it does not exist already. 
		# And if the key is a prefix of the trie node, just 
		# marks it as leaf node. 
		node = self.root 

		for a in list(key): 
			if not node.children.get(a): 
				node.children[a] = TrieNode() 

			node = node.children[a] 

		node.last = True

	def search(self, key): 
		
		# Searches the given key in trie for a full match 
		# and returns True on success else returns False. 
		node = self.root 
		found = True

		for a in list(key): 
			if not node.children.get(a): 
				found = False
				break

			node = node.children[a] 

		return node and node.last and found 

	def suggestionsRec(self, node, word): 
		
		# Method to recursively traverse the trie 
		# and return a whole word. 
		if node.last: 
			self.word_list.append(word) 

		for a,n in node.children.items(): 
			self.suggestionsRec(n, word + a) 

	def printAutoSuggestions(self, key): 
		
		# Returns all the words in the trie whose common 
		# prefix is the given key thus listing out all 
		# the suggestions for autocomplete. 
		node = self.root 
		not_found = False
		temp_word = '' 

		for a in list(key): 
			if not node.children.get(a): 
				not_found = True
				break

			temp_word += a 
			node = node.children[a] 

		if not_found: 
			return 0
		elif node.last and not node.children: 
			return -1

		self.suggestionsRec(node, temp_word) 
 
		return self.word_list
def problem11(keys, key):
    # creating trie object 
    t = Trie() 

    # creating the trie structure with the 
    # given set of strings. 
    t.formTrie(keys) 

    # autocompleting the given key using 
    # our trie structure. 
    comp = t.printAutoSuggestions(key) 
    

    if type(comp) != list: 
        return []
    else:
        return comp


def test_problem11a(): 
    keys = ["hello", "dog", "hell", "cat", "a", 
             "help", "helps", "helping"] # keys to form the trie structure. 
    key = "hel" # key for autocomplete suggestions. 
    assert problem11(keys,key) == [ 'hell', 'hello', 'help', 'helps', 'helping']
    
def test_problem11b(): 
    keys = ["hello", "dog", "hell", "cat", "a", 
             "help", "helps", "helping"] # keys to form the trie structure. 
    key = "help" # key for autocomplete suggestions. 
    assert problem11(keys,key) == ['help', 'helps', 'helping']



