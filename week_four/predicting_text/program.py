# Implement the following Node class API.
# If you delete something important, this code is copied in specification.py

from typing import Dict, List


class Node:

    completeWords: List[str] = list()

    def __init__(self, prefix: str):
        """
        Creates a Node with the given string prefix.
        The root node will be given prefix ''.
        You will need to track:
        - the prefix
        - whether this prefix is also a complete word
        - child nodes
        """
        self.prefix = prefix
        self.children: Dict[str, Node] = dict()

    def get_prefix(self) -> str:
        """
        Returns the string prefix for this node.
        """
        return self.prefix

    def get_children(self) -> List["Node"]:
        """
        Returns a list of child Node objects, in any order.
        """
        return list(self.children.values())

    def is_word(self) -> bool:
        """
        Returns True if this node prefix is also a complete word.
        """
        return self.prefix in Node.completeWords

    def add_word(self, word: str) -> None:
        """
        Adds the complete word into the trie, causing child nodes to be created as needed.
        We will only call this method on the root node, e.g.
        >>> root = Node('')
        >>> root.add_word('cheese')
        """
        # If word has already been added, don't add it again
        if word in Node.completeWords:
            return

        # Add the word to global list of complete words
        Node.completeWords.append(word)

        # Create the nodes
        Node.__recursive_add(self, word, word, 1)

    @staticmethod
    def __recursive_add(nodeToAppendTo: "Node", completeWord: str, remainingWord: str, depth: int) -> None:
        # If whole word is exhausted, stop the recursion
        if len(remainingWord) == 0:
            return

        # If the current letter in the word are already created, don't create a new node
        for key in nodeToAppendTo.children.keys():
            if key is remainingWord[0]:
                Node.__recursive_add(
                    nodeToAppendTo.children[key],
                    completeWord,
                    remainingWord[1:],
                    depth+1)
                return

        # If the letter does not exist yet, create new node
        nodeToAppendTo.children[remainingWord[0]] = Node(completeWord[:depth])
        Node.__recursive_add(
            nodeToAppendTo.children[remainingWord[0]],
            completeWord,
            remainingWord[1:],
            depth+1)

    def find(self, prefix: str) -> "Node":
        """
        Returns the node that matches the given prefix, or None if not found.
        We will only call this method on the root node, e.g.
        >>> root = Node('')
        >>> node = root.find('te')
        """
        currentChild: Node = self

        try:
            for i, letter in enumerate(prefix):
                currentChild = currentChild.children[letter]
        except KeyError:
            return None

        return currentChild

    def words(self) -> List[str]:
        """
        Returns a list of complete words that start with my prefix.
        The list should be in lexicographical order.
        """
        words: List[str] = list()

        for word in Node.completeWords:
            if word.startswith(self.prefix):
                words.append(word)

        words.sort()

        return words


if __name__ == '__main__':
    # Write your test code here. This code will not be run by the marker.

    # The first example in the question.
    root = Node('')
    for word in ['tea', 'ted', 'ten']:
        root.add_word(word)
    node = root.find('te')
    print(node.get_prefix())
    print(node.is_word())
    print(node.words())

    # The second example in the question.
    root = Node('')
    for word in ['inn', 'in', 'into', 'idle']:
        root.add_word(word)
    node = root.find('in')
    print(node.get_prefix())
    children = node.get_children()
    print(sorted([n.get_prefix() for n in children]))
    print(node.is_word())
    print(node.words())

    # The third example in the question.
    with open('./week_four/predicting_text/the_man_from_snowy_river.txt') as f:
        words = f.read().split()
    root = Node('')
    for word in words:
        root.add_word(word)
    print(root.find('th').words())

    # The fourth example
    root = Node('')
    for word in ['dog', 'dog-house', 'dogged']:
        root.add_word(word)
    node = root.find('dog')
    print(node.get_prefix())
    child_nodes = node.get_children()
    print(sorted([n.get_prefix() for n in child_nodes]))
    leaf_node = root.find('dog-house')
    leaf_children = None if leaf_node is None else leaf_node.get_children()
    print(leaf_children == [])
