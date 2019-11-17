### Demonstrate software engineering design understanding

Refactor or add to your code from iteration 2 to utilise good software engineering design to make your code more maintainable. Use a range of principles discussed in lectures.

As you modify your code, maintain a up to a 2 page markdown file that lists the key changes you've made in your code and why they've been made. 

General Styling:

General:
- Consistency (spacing, order, etc)
- No redundant lines <^ (WE HAVE REDUNDANCIES)
- client_id = tokcheck(token) 
- new_<object name> = create_object()
- No literal values, use global constants.
- Function inputs match spec names exactly
- Variable AND function names reflect data types and usage (eg user_id instead of user.) exactly abide by data type table in specification.
- If desired suffix or prefix does not exist, we can make one and document it. (make sure that these “type hints” very obviously give away the type)-
- Private class fields (ie most of them) have an underscore before themselves (eg self._id)


## Naming:
Naming of variables followed a strict convention of sticking to the names given in the spec wherever possible. However when we had to come up with names we followed the protocol:


## Comments:

Our team has added in extra comments to functions, classes or methods where we figured that the functionality wasn't as clear. If any of the code meets
any of the following criterias, a comment would be added for that particular funciton.

- If not self evident
- If there are special cases to usage
- All errors for function

Code redesign:

- Find categories of errors (eg id not found errors etc)
- Eg raise a value error for an invalid id, when trying to access dict with invalid id
- Make code more responsible for itself (But often this makes code harder to read, so must come with comments and docstrings)
- Single Responsibility Principle (Most Value errors moved into objects setters/getters.)
- File refactoring:
- Cleans up imports, splits code into logical pieces
- Files should import in a tree structure primarily

Decorators:

- For generating repetitive wrappers, reduce function complexity (Export and authorise)

## Newlines:

New lines are added for some lines of code where the functionality of the code wasn't as clear. The code would be broken up into small chuncks
for better readability. Other lines where it wasn't as unclear, a comment would be added instead.

## Errors:

All Errors now follow a pattern, where the error would always raise a comment describing the type of error that occurred.

## Encapsulation:

Added getters and stopped using direct access to class field in order to ensure unintentional tampering of the attributes within a class. All attributes will now 
be accessed through methods within the class. 

Concrete tasks:

- get_channels(), get_users(), etc now take in an id, and output the object with that id, and raises an error if the id does not exist

- def get_channels(channel_id):
   try:
       return channels[channel_id]
   except(KeyError):
       raise ValueError("message")


## Style guidelines:
For the most part, we referred to the google style guide, making docstrings for classes and non-trivial functions, but we
did make some documented changes.


Controversy:

- When do different principles conflict (eg. consistency/redundant lines)






