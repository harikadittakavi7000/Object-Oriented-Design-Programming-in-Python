class TrieNode:
    """A node in the trie data structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # mark if this node is the end of a word
        self.is_end = False

        # a dictionary for child nodes
        # where keys are characters, values are nodes
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        A trie  data structure has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")
        self.output = None

    def insert(self, new_word):
        """Insert a word into the trie"""
        node = self.root

        for letter in new_word.lower():
            # Check if there is a child containing the character, if yes, move down the trie
            if letter in node.children:
                node = node.children[letter]
            else:
                # If a character is not found, create a new node in the trie
                new_node = TrieNode(letter)
                node.children[letter] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

    def trie_traverse(self, node, list_of_words, prefix):
        """Recursive helper function to traverse the trie"""
        if node.is_end:
            list_of_words.append(prefix + node.char)
        for child in node.children.values():
            self.trie_traverse(child, list_of_words, prefix + node.char)

    def search_substring(self, substring):
        """
        Given a substring, retrieve all words stored in
        the trie with that substring
        """
        node = self.root
        self.output = []
        list_of_words = []
        self.trie_traverse(node, list_of_words, "")

        for word in list_of_words:
            if substring in word:
                self.output.append(word)

        return self.output

    def print_all_words(self):
        """Print all words in trie"""
        list_of_words = []
        node = self.root
        self.trie_traverse(node, list_of_words, "")
        return list_of_words


t = Trie()
input_words = input("Enter words to be inserted in trie, separated by space: ").split(" ")
check_substring = input("Enter substring to search in words: ")

for input_word in input_words:
    t.insert(input_word)

print(t.search_substring(check_substring))
print(t.print_all_words())
