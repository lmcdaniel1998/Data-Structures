import unittest
import perm_lex


class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex_0(self):
        self.assertEqual(perm_lex.perm_gen_lex('ab'), ['ab', 'ba'])

    def test_perm_gen_lex_1(self):
        self.assertEqual(perm_lex.perm_gen_lex('efg'), ['efg', 'egf', 'feg', 'fge', 'gef', 'gfe'])

    def test_perm_gen_lex_2(self):
        self.assertEqual(perm_lex.perm_gen_lex(''), [])

    def test_perm_gen_lex_3(self):
        self.assertEqual(perm_lex.perm_gen_lex('123'), ['123', '132', '213', '231', '312', '321'])

    def test_perm_gen_lex_4(self):
        self.assertEqual(perm_lex.perm_gen_lex('wxyz'), ['wxyz',
 'wxzy',
 'wyxz',
 'wyzx',
 'wzxy',
 'wzyx',
 'xwyz',
 'xwzy',
 'xywz',
 'xyzw',
 'xzwy',
 'xzyw',
 'ywxz',
 'ywzx',
 'yxwz',
 'yxzw',
 'yzwx',
 'yzxw',
 'zwxy',
 'zwyx',
 'zxwy',
 'zxyw',
 'zywx',
 'zyxw'])


if __name__ == "__main__":
        unittest.main()
