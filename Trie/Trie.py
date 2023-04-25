class TrieNode:
    """A node in the trie data structure"""

    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self):
        """A trie  data structure has at least the root node,
        which does not store any character"""

        self.root = TrieNode("")
        self.output = None

    def insert(self, new_word):
        """Insert a word into the trie"""

        node = self.root
        for letter in new_word.lower():
            # Check if there already is a child containing the character,
            # if yes, move down the trie
            if letter in node.children:
                node = node.children[letter]
            else:
                # If a character is not found, create a new node in the trie
                new_node = TrieNode(letter)
                node.children[letter] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

    def search_substring(self, node, substring, node_values):
        """Given a substring, retrieve words stored in
        the trie with that substring"""

        if node.is_end:
            current_word = node_values + node.char
            if substring in current_word:
                print(current_word)
        # Recursive iteration to traverse the trie
        for child in node.children.values():
            self.search_substring(child, substring, node_values + node.char)

    def print_all_words(self, node, list_of_words, node_values):
        """Print all words in trie"""

        if node.is_end:
            list_of_words.append(node_values + node.char)
        # Recursive iteration to traverse and construct list of all words in trie
        for child in node.children.values():
            self.print_all_words(child, list_of_words, node_values + node.char)
        return list_of_words


if __name__ == '__main__':
    t = Trie()
    input_words = input("Enter words to be inserted into the Trie "
                        "(separated by space): ").split(" ")
    check_substring = input("Enter substring to search in words: ")

    for input_word in input_words:
        t.insert(new_word=input_word)

    print(f'Words in the Trie which contain the substring "{check_substring}":')
    t.search_substring(node=t.root, substring=check_substring, node_values="")
    words_in_trie = t.print_all_words(node=t.root, list_of_words=[], node_values="")
    print(f"Complete list of words present in the Trie: {words_in_trie}")
