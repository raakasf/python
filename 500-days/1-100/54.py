from argparse import Namespace
# This line creates a new Namespace object called args with two attributes: debug and level.
# So, args now behaves like a simple object with these two properties.
args = Namespace(debug=True, level=2)
print(args.level)

# Even though it comes from argparse, Namespace can be useful in other contexts, such as:
# Creating quick configuration objects in scripts or tests
# Simulating parsed command-line arguments when testing
# Replacing small custom classes or dictionaries when you want dot-access (e.g., args.level instead of args['level'])
