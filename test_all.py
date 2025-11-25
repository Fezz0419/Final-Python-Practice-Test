from unittest import TestCase
from io import StringIO
import sys
import all
from unittest.mock import patch

class TestFunctions(TestCase):
    def test_get_date_of_birth(self):
        self.assertEqual(all.get_date_of_birth('0004185035083'), '18/04/00')
        self.assertEqual(all.get_date_of_birth('0111224903088'), '22/11/01')
        self.assertEqual(all.get_date_of_birth('9809126723080'), '12/09/98')

    def test_get_gender(self):
        self.assertEqual(all.get_gender('9106236034082'), 'Male')
        self.assertEqual(all.get_gender('9402030894089'), 'Female')
        self.assertEqual(all.get_gender('0312264983083'), 'Female')

    @patch("sys.stdin", StringIO("Square\n"))
    def test_1_shape(self):

        text_capture = StringIO()
        sys.stdout = text_capture
        self.assertEqual(all.get_shape(),'square')

    def test_10_triangle_multiplication(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        all.draw_triangle_multiplication(6)

        self.assertEqual("""1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
""",text_capture.getvalue())
        
    def test_12_pyramid(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        all.draw_pyramid(3)

        self.assertEqual("""  *
 ***
*****
""",text_capture.getvalue())
        
    def test_fibonacci(self):
        self.assertEqual(all.fibonacci(0), 0)
        self.assertEqual(all.fibonacci(1), 1)
        self.assertEqual(all.fibonacci(5), 5)
        self.assertEqual(all.fibonacci(10), 55)
        self.assertEqual(all.fibonacci(15), 610)
    
    def test_fizz_buzz(self):
        self.assertEqual(all.fizz_buzz(3), "Fizz")
        self.assertEqual(all.fizz_buzz(5), "Buzz")
        self.assertEqual(all.fizz_buzz(15), "FizzBuzz")
        self.assertEqual(all.fizz_buzz(7), 7)

    def test_is_prime(self):
        self.assertTrue(all.is_prime(2))
        self.assertTrue(all.is_prime(3))
        self.assertFalse(all.is_prime(4))
        self.assertTrue(all.is_prime(13))
        self.assertFalse(all.is_prime(20))

    def test_factorial(self):
        self.assertEqual(all.factorial(0), 1)
        self.assertEqual(all.factorial(1), 1)
        self.assertEqual(all.factorial(5), 120)
        self.assertEqual(all.factorial(7), 5040)

    def test_prime_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        all.prime_triangle(5)

        self.assertEqual("""2 
3 5 
7 11 13 
17 19 23 29 
31 37 41 43 47 
""",text_capture.getvalue())
        
    def test_pascal_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        all.pascal_triangle(4)

        self.assertEqual("""1
1 1
1 2 1
1 3 3 1
""",text_capture.getvalue())