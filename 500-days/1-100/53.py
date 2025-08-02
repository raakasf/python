# tokenize is used to break Python code into tokens.
import tokenize
# BytesIO allows byte strings to behave like file objects, which tokenize needs.
from io import BytesIO
# Defines the Python code as a byte string.
code = b"x = 1 + 2"
tokens = list(tokenize.tokenize(BytesIO(code).readline))
print(tokens[2].string)
