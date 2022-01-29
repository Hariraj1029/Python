# Create an empty list
the_list = []
# or
the_list = list()

# Multiplication
list_size = 3
the_list = [''] * list_size

# List comprehension
list_size = 3
the_list = ['' for _ in range(list_size)]

# itertools.repeat()
import itertools
list_size = 3
the_list = list(itertools.repeat('', list_size))

# [] is Python's index operator
# The key can be an integer or a slice!

# Retrieve a single item
the_list = [0, 1, 2]
result = the_list[1]

# Update a single item
the_list = [0, 1, 2]
the_list[1] = 42

# [] with an integer key can only update elements that already exist
the_list = []
# the_list[0] = 42  # Raises an IndexError

# [] is Python's index operator
# The key can be an integer or a slice!

# Retrieve mutliple items using a slice
the_list = [0, 1, 2, 3]
result = the_list[1:3]

# Slices are open on the right!
# This yields an empty list
the_list = [0, 1, 2, 3]
the_list[1:1]

# Set multiple items
the_list = [0, 1, 2, 3]
the_list[1:3] = [11, 22]

# Extend a list
the_list = [0, 1, 2, 3]
the_list[len(the_list):] = [11, 22]

# Can extend an empty list
the_list = []
the_list[0:] = [11, 22]

# Gotcha! Slice is too small
the_list = [0, 1, 2, 3]
the_list[1:2] = [11, 22]

# Gotcha! Slice is too large
the_list = [0, 1, 2, 3]
the_list[1:4] = [11, 22]

# insert(index, value)

# insert() with index = 0 always prepends to the list
the_list = [0, 1, 2]
the_list.insert(0, 42)

# insert() with index >= len(list) always appends to the list
the_list = [0, 1, 2]
the_list.insert(len(the_list), 42)
the_list.insert(999, 1000)

# In general, insert() inserts *before* the given index
the_list = [0, 1, 2]
the_list.insert(1, 42)

# It is safe to insert into an empty list
the_list = []
the_list.insert(0, 42)

the_list = []
the_list.insert(999, 42)