# errors.py: Defines custom exception classes for the calculator

# Base error for calculator
class CalculatorError(Exception): pass
# Error during lexical analysis
class LexerError(CalculatorError): pass
# Error during parsing
class ParserError(CalculatorError): pass
# Error during evaluation
class EvaluationError(CalculatorError): pass
