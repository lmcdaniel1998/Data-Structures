import unittest
import filecmp
from huffman import *


class TestList(unittest.TestCase):
    def test_comes_before_0(self):
        node1 = HuffmanNode(97, 8)
        node2 = HuffmanNode(99, 7)
        self.assertFalse(comes_before(node1, node2))

    def test_comes_before_1(self):
        node1 = HuffmanNode(97, 8)
        node2 = HuffmanNode(99, 1)
        self.assertTrue(comes_before(node2, node1))

    def test_comes_before_2(self):
        node1 = HuffmanNode(99, 8)
        node2 = HuffmanNode(99, 7)
        self.assertFalse(comes_before(node1, node2))

    def test_comes_before_3(self):
        node1 = HuffmanNode(97, 1)
        node2 = HuffmanNode(97, 7)
        self.assertTrue(comes_before(node1, node2))

    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_cnt_freq_0(self):
        freqlist = cnt_freq("multiline.txt")
        anslist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 5, 2, 0, 2, 7, 0, 0, 5, 2, 4, 1, 3, 0, 0, 3, 3, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(freqlist, anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_huff_tree_0(self):
        freqlist = cnt_freq("multiline.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 56)
        self.assertEqual(hufftree.char, 10)
        self.assertEqual(hufftree.right.freq, 32)
        self.assertEqual(hufftree.right.char, 32)
        self.assertEqual(hufftree.left.freq, 24)
        self.assertEqual(hufftree.left.char, 10)

    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_header_0(self):
        freqlist = cnt_freq("declaration.txt")
        header = create_header(freqlist)
        answer = "10 166 32 1225 38 1 39 1 44 109 45 3 46 36 49 1 52 1 54 1 55 2 58 10 59 10 65 22 66 7 67 19 68 5 69 3 70 17 71 15 72 24 73 8 74 5 75 1 76 15 77 3 78 8 79 6 80 23 82 9 83 23 84 15 85 3 87 13 97 466 98 88 99 171 100 253 101 875 102 169 103 116 104 331 105 451 106 12 107 13 108 216 109 144 110 487 111 518 112 116 113 6 114 420 115 460 116 640 117 211 118 74 119 84 120 9 121 82 122 4"
        self.assertEqual(header, answer)

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_create_code_0(self):
        freqlist = cnt_freq("multiline.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('\n')], '00101')
        self.assertEqual(codes[ord(' ')], '101')

    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'filecmp' on your encoded file with a *known* solution file
        self.assertTrue(filecmp.cmp("file1_out.txt", "file1_soln.txt"))

    def test_02_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'filecmp' on your encoded file with a *known* solution file
        self.assertTrue(filecmp.cmp("file2_out.txt", "file2_soln.txt"))

    def test_03_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'filecmp' on your encoded file with a *known* solution file
        self.assertTrue(filecmp.cmp("multiline_out.txt", "multiline_soln.txt"))

    def test_04_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'filecmp' on your encoded file with a *known* solution file
        self.assertTrue(filecmp.cmp("declaration_out.txt", "declaration_soln.txt"))
        huffman_decode("declaration_out.txt", "declaration_decode.txt")
        self.assertTrue(filecmp.cmp("declaration.txt", "declaration_decode.txt"))

    def test_no_file(self):
        self.assertRaises(FileNotFoundError, lambda: huffman_encode("f1.txt", "file1_out.txt"))

    def test_empty_file(self):
        huffman_encode("blank_file.txt", "blank_file_out.txt")
        self.assertTrue(filecmp.cmp("blank_file_out.txt", "blank_file_soln.txt"))

    def test_single_char_file(self):
        huffman_encode("single_char.txt", "single_char_out.txt")
        self.assertTrue(filecmp.cmp("single_char_out.txt", "single_char_soln.txt"))

    def test_parse_header_0(self):
        know_freq_list = cnt_freq("file1.txt")
        header = create_header(know_freq_list)
        reconstructed_freq_list = parse_header(header)
        self.assertEqual(know_freq_list, reconstructed_freq_list)

    def test_parse_header_1(self):
        know_freq_list = cnt_freq("declaration.txt")
        header = create_header(know_freq_list)
        reconstructed_freq_list = parse_header(header)
        self.assertEqual(know_freq_list, reconstructed_freq_list)

    def test_huffman_decode_0(self):
        huffman_decode("file1_soln.txt", "file1_out.txt")
        self.assertTrue(filecmp.cmp("file1_out.txt", "file1.txt"))

    def test_huffman_decode_1(self):
        huffman_decode("file2_soln.txt", "file2_out.txt")
        self.assertTrue(filecmp.cmp("file2_out.txt", "file2.txt"))

    def test_huffman_decode_3(self):
        huffman_decode("multiline_soln.txt", "multiline_out.txt")
        self.assertTrue(filecmp.cmp("multiline_out.txt", "multiline.txt"))

    def test_huffman_decode_no_file(self):
        self.assertRaises(IOError, lambda: huffman_decode("f1_soln.txt", "file1_out.txt"))

    def test_huffman_decode_empty_file(self):
        huffman_decode("blank_file_soln.txt", "blank_file_out.txt")
        self.assertTrue(filecmp.cmp("blank_file_out.txt", "blank_file.txt"))

    def test_huffman_decode_single_char_file(self):
        huffman_decode("single_char_soln.txt", "single_char_out.txt")
        self.assertTrue(filecmp.cmp("single_char_out.txt", "single_char.txt"))


if __name__ == '__main__': 
    unittest.main()
