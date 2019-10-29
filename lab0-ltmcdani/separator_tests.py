import unittest
import io, sys
from sys import argv
from separator import *


# Run this unittest file without passing any command-line arguments
# other than ones you want to pass to unittest such as -values


class Test_Seperator(unittest.TestCase):

    def setUp(self):
        # Add a spot to argv that we can use to pass command-line 
        # arguments to the main function in the separator module
        sys.argv.append(None)

    def test_01(self):
        argv[1] = 6  # Simulates passing 6 on the command line
        sys.stdout = student_output = io.StringIO()        
        sys.stdin = io.StringIO("1 2 1.2 2.3\n3\n4\n7.8 garbage, 12\n")
        expected_out = "Integers: 1 2 3 4 \nFloats: 1.2 2.3 7.8"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_02(self):
        argv[1] = 4  # Simulates passing 4 on the command line
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 2 3\n4 5 6\n")
        expected_out = "Integers: 1 2 3 4 \nFloats:"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_03(self):
        argv[1] = 2  # Simulates passing 4 on the command line
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("3 4.5 3.2\nhello 5\n")
        expected_out = "Integers: 3 \nFloats: 4.5 3.2"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_04(self):
        argv[1] = 7  # Simulates passing 4 on the command line
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("why 4 5.5\n4 5 6\n")
        expected_out = "Integers:  \nFloats:"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_05(self):
        argv[1] = 0  # Simulates passing 4 on the command line
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("3 2 1.4\n8.8 5 6\n")
        expected_out = "Integers:  \nFloats:"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_06(self):
        argv[1] = 2  # Simulates passing 4 on the command line
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("3 3 3 3 3\n3.3 3 3 3 3\n")
        expected_out = "Integers: 3 3 \nFloats: 3.3"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_07(self):
        argv[1] = 6  # Simulates passing 4 on the command line
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("\n")
        expected_out = "Integers:  \nFloats:"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())

    def test_08(self):
        argv[1] = 3  # Simulates passing 4 on the command line
        sys.stdout = student_output = io.StringIO()
        sys.stdin = io.StringIO("1 2.2 3 4.4\n5 6.6 7 8.8\n9 10.1 11")
        expected_out = "Integers: 1 3 5 \nFloats: 2.2 4.4 6.6"
        main()
        self.assertEqual(expected_out, student_output.getvalue().strip())


if __name__ == "__main__":
        unittest.main()
