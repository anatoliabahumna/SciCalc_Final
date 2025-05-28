# tests.py: Unit tests for the scientific calculator
import unittest
from scicalc.main import run
from scicalc.evaluator import Evaluator

class CalcTests(unittest.TestCase):
    def once(self,expr,exp,ev=None):
        # Helper to run a single expression and check the result
        r=run(expr+"\n",ev)
        self.assertAlmostEqual(r[0],exp)

    def test_basic_ops(self):
        # Test basic arithmetic operations
        self.once("3+4*2",11)
        self.once("(3+4)*2",14)

    def test_unary(self):
        # Test unary minus and plus
        self.once("-2+5",3)

    def test_power(self):
        # Test exponentiation and right associativity
        self.once("2^3^2",512)

    def test_variables(self):
        # Test variable assignment and usage
        ev=Evaluator()
        run("x=10\n",ev)
        self.once("x/2",5,ev)

    def test_builtins(self):
        # Test built-in functions
        self.once("sin(0)",0)
        self.once("abs(-3)+sqrt(4)",5)

    def test_root_func(self):
        # Test custom root function
        self.once("root(27,3)",3)

    def test_div_zero_error(self):
        # Test division by zero error handling
        self.assertTrue("div0" in run("1/0\n")[0])

    def test_syntax_error(self):
        # Test syntax error handling
        self.assertTrue("ERROR" in run("(3+4\n")[0])

if __name__=='__main__':
    unittest.main()
