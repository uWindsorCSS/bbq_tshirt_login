class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.word_end = True

    def autocomplete(self, word, limit = 5):
        current = self.root
        matching_prefix = ""

        for char in word:
            if char not in current.children:
                break
            current = current.children[char]
            matching_prefix += char

        ret = []
        queue = [(matching_prefix + c, node)\
                    for c, node in current.children.items()]

        while len(queue) > 0:
            if len(ret) >= limit:
                break

            prefix, node = queue.pop()
            if node.word_end:
                ret.append(prefix)
            queue.extend([(prefix + c, n) for c, n in node.children.items()])
        return ret
