def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences

class TreeNode:
    def __init__(self):
        self.data: str = ''
        self.children: list[TreeNode] = []

def suffix_trie(string):
    root = TreeNode()
    for i in range(len(string)):
        suffix = string[i:]
        pointer : TreeNode = root

        # print(f"cur: {suffix}")
        for char in suffix:
            # print(f"cur char: {char}")
            found = False
            for child in pointer.children:
                if child.data == char:
                    # print(f"found, moving to child.")
                    pointer = child
                    found = True
                    break

            if not found:
                # print(f"not found, adding node and moving to child.")
                new_node = TreeNode()
                new_node.data = char.strip()
                pointer.children.append(new_node)
                pointer = new_node

    return root

def suffix_trie_2_str(root:TreeNode):
    if not root or len(root.children) == 0: return "$"
    if len(root.children) == 1: return root.data + suffix_trie_2_str(root.children[0])

    string = ''
    for child in root.children:
        if len(child.children) > 1: string += child.data + '\n'
        string += suffix_trie_2_str(child) + '\n'

    return string.strip()

if __name__ == "__main__":
    with open('input.txt','r') as file: input = file.read().strip()
    print(f"input:   \n{input}")

    output = suffix_trie_2_str(suffix_trie(input))
    with open("output.txt", 'w') as file:
        file.write(str(output))
    print(f"output:  \n{output}")
