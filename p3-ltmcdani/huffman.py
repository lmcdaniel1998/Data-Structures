class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the frequency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def __lt__(self, other):            # allows use of .sort() built in function
        return comes_before(self, other)

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node


def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:         # first check which freq comes first
        return True
    elif a.freq == b.freq:
        if a.char < b.char:           # if freqs are the same check if a.char comes before b.char
            return True
        else:
            return False
    else:
        return False


def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    # create a new node with lesser char and sum of frequencies
    if a.char < b.char:
            new_char = a.char
    else:
        new_char = b.char

    if comes_before(a, b) is True:
        new_node = HuffmanNode(new_char, a.freq + b.freq)
        new_node.set_right(b)
        new_node.set_left(a)
    else:
        new_node = HuffmanNode(new_char, a.freq + b.freq)
        new_node.set_right(a)
        new_node.set_left(b)
    return new_node


def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    char_array = [0]*256            # create an array 256 in length
    convert_file = open(filename, 'r')      # open a file for reading
    convert_file_lines = convert_file.read()
    for char in convert_file_lines:            # gets every char in every row of file

        char_count = char_array[ord(char)]          # add to positions in array based on ascii values of chars in file
        char_count += 1
        char_array[ord(char)] = char_count

    convert_file.close()

    return char_array


def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    # adds all non-zero frequency characters to list
    node_list = []
    for char in range(0, len(char_freq) - 1):
        if char_freq[char] != 0:
            node = HuffmanNode(char, char_freq[char])
            node_list.append(node)

    if len(node_list) == 0:         # checks if there are no characters in file
        return None
    elif len(node_list) == 1:       # checks if only one character in file
        return node_list[0]

    # sort list initially least to greatest
    node_list.sort()

    # creates a binary search tree out of node list
    for node in range(len(node_list) - 1):
        while len(node_list) >= 2:
            # get first two nodes in list and combine into tree
            a_node = node_list[node]
            b_node = node_list[node + 1]
            node_list = node_list[2:]           # remove nodes just placed in new tree from list
            node_tree = combine(a_node, b_node)
            # add tree to list in proper position
            node_list.append(node_tree)
            node_list.sort()
    return node_list[0]    # change to node_list[0] after testing is complete


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    char_array = ['']*256            # create an array 256 in length
    return create_code_helper(node, char_array)


def create_code_helper(node, character_array, code=''):
    if node is not None:
        # checks if node is a leaf that contains a char and it's freq
        if (node.right is None) and (node.left is None):
            character_array[node.char] = code           # add code for character to ascii position of character in character array
        else:
            create_code_helper(node.left, character_array, code + str(0))           # adds 0 to code if in left sub tree
            create_code_helper(node.right, character_array, code + str(1))          # adds 1 to cod if in right sub tree
        return character_array


def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return '97 3 98 4 99 2' """
    header_string = ''
    for code in range(0, len(freqs)):
        if freqs[code] != 0:
            # adds ascii char and freq to header_string
            header_string += str(code) + ' ' + str(freqs[code]) + ' '
    return header_string[: -1]      # removes last space from header and returns header


def parse_header(header_string):
    """Input is the header of an encoded file. Creates a frequency list of length 256
    that will be used to recreate a huffman tree for the file"""
    frequency_list = [0]*256
    header_list = header_string.split(' ')          # places all characters and frequencies in a list
    pre_freq_list = []
    for i in range(0, len(header_list), 2):
        pre_freq_list.append(header_list[i:i+2])            # combines a character with a frequency [char, freq]
    for pair in pre_freq_list:
        frequency_list[int(pair[0])] = int(pair[1])          # inserts frequencies into corresponding character index
    return frequency_list


def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    try:
        # open both files for encoding
        initial_file = open(in_file, 'r')
        coded_file = open(out_file, 'w')

        freq_array = cnt_freq(in_file)         # create array of character frequencies in file

        # create code based off of in_file
        huff_tree_code = create_huff_tree(freq_array)

        if huff_tree_code is None:
            # returns empty file if input file is empty
            initial_file.close()
            coded_file.close()

        elif (huff_tree_code.right is None) and (huff_tree_code.left is None):
            # adds only header to coded file if all one character
            header = create_header(freq_array)
            coded_file.write(header)
            initial_file.close()
            coded_file.close()

        else:
            # add header to coded file
            header = create_header(freq_array)
            coded_file.write(header + '\n')

            code = create_code(huff_tree_code)

            # reads every character in every line of in_file
            initial_file_lines = initial_file.read()
            for character in initial_file_lines:
                coded_file.write(code[ord(character)])          # adds encoded character to coded file

            initial_file.close()
            coded_file.close()

    except IOError:
        raise IOError("enter a valid file name")        # catches non existent files


def huffman_decode(encoded_file, decoded_file):
    """Takes encoded_file name and decoded_file name as parameters
    Constructs huffman tree from header of encoded_file decodes encoded_file
    into decoded_file using huffman tree and code
    Takes into account empty file and files with only one character"""
    try:
        # open both files for encoding
        encoded = open(encoded_file, 'r')
        decoded = open(decoded_file, 'w')

        # read first line of file to create frequency list
        first_line = encoded.readline()

        # checks if file is empty
        if len(first_line) == 0:
            encoded.close()
            decoded.close()

        else:
            freq_list = parse_header(first_line)            # generates frequency list from header
            huffman_tree = create_huff_tree(freq_list)          # generate huffman tree from frequency list
            lines = encoded.readlines()         # reads second line of encoded file

            # checks if there is only one type of character in file
            if (huffman_tree.left is None) and (huffman_tree.right is None):
                for i in range(0, int(huffman_tree.freq)):
                    decoded.write(chr(huffman_tree.char))
                encoded.close()
                decoded.close()

            else:
                # establish root node
                char = huffman_tree
                for direction in lines[0]:
                    # go left
                    if direction == '0':
                        # check if you can move left
                        if (char.left is not None) and (char.right is not None):
                            char = char.left
                            # write to decoded_file if node is a leaf
                            if (char.left is None) and (char.right is None):
                                decoded.write(chr(char.char))
                                char = huffman_tree

                    # go right
                    elif direction == '1':
                        # check if you can move right
                        if (char.left is not None) and (char.right is not None):
                            char = char.right
                            # write to decoded_file if node is a leaf
                            if (char.left is None) and (char.right is None):
                                decoded.write(chr(char.char))
                                char = huffman_tree

                encoded.close()
                decoded.close()

    except FileNotFoundError:
        raise FileNotFoundError("[Errno 2] No such file or directory: " + str(decoded_file))        # catches non existent files
