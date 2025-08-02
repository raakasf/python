# Decimal is used for high-precision decimal arithmetic, avoiding float inaccuracies.
# getcontext() accesses the current decimal arithmetic settings, such as precision.
from decimal import Decimal, getcontext

# Sets the precision of decimal operations to 4 significant digits (not decimal places).
# This affects how many total digits (before + after decimal) the results can retain.
# Important: this doesn't round the final printed value like round() — it controls internal calculation precision.
getcontext().prec = 4
x = Decimal(1) / Decimal(7)
print(int(x * 1000))
