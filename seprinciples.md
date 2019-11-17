# Demonstrate software engineering design understanding

Refactor or add to your code from iteration 2 to utilise good software engineering design to make your code more maintainable. Use a range of principles discussed in lectures.

As you modify your code, maintain a up to a 2 page markdown file that lists the key changes you've made in your code and why they've been made. 



## File organization


## Code Redesign

- Find categories of errors (eg id not found errors etc)
- Eg raise a value error for an invalid id, when trying to access dict with invalid id
- Make code more responsible for itself (But often this makes code harder to read, so must come with comments and docstrings)
- Single Responsibility Principle (Most Value errors moved into objects setters/getters.)
- File refactoring:
- Cleans up imports, splits code into logical pieces
- Files should import in a tree structure primarily
- Added update_messages function to update the state of the server before sending a message. Functionality used to be part of channel_messages function but was broken down. (Top Down)
- Move Value errors to setters/getters to remove repetitive error raising(DRY)
- Using global constants instead of literal value(DRY)

### Decorators:
To be able to both run the server with frontend and test using pytest, we needed to have separate functions that actually did the work, and the functions that interfaced with backend. Using an export decorator we only needed to write the main function, and this would be automatically wrapped to interface with frontend. Types were automatically inferred from variable names.
We also kept tokens invisible from the main implementation by passing the authorisation to the authorise decorator. Decorators made our funcions very short and simple.

### Code Responsibility


### Encapsulation:
We added getters and stopped using direct access to class fields. Also, for global variables we made python modules for server state and server constants which could be globally accessed via getters and setters.
 
Errors:

All errors would have a message describing that error, eg:
`raise ValueError(f"Message {mess.get_id()} '{mess.get_message()[:10]}...' is not pinned.")`


## Style guidelines:
For the most part, we referred to the google style guide, making docstrings for classes and non-trivial functions, but we
did make some documented changes.

## Naming:
Naming of variables followed a strict convention of sticking to the names given in the spec wherever possible. However when we had to come up with names we followed a number of principles:

- Names must have a clear indicator of their type, eg ending the name with id denotes that it is an integer.
- Variable and function names reflect usage and purpose (eg user_id instead of user.) 
- Function inputs match spec names exactly to avoid confusion
- Type suffixes and prefixes are to be standardised. We used a discord channel to track new prefixes that we would add to our standard.
- Functions that returned values would also follow this standard.
- Inner fields in objects start with an underscore as they are all meant to be private fields. 



 
We registered the following extra prefixes/suffixes:

```
name and name_: a string
_str: a string
_obj: an object
new_: a newly created object from a constructor
set_: a python set
```
## Comments

Comments are added in areas where functionality of code is unclear. This is generally recognised during the refactoring period. Whether or not comments need to be 
added is decided by whether or not they are any of the following:

- If not self evident
- If there are special cases to usage
- All errors for function

Docstrings were also implemented into all functions and classes, and some methods within the class for easier understanding of the functionalities within 
these functions etc. Docstrings follow a strict format of which includes Name, Description, Arguements, Return Values and Errors Raised.



Newlines:

- Grouping related elements together, or grouping single units of thought (generally anything that can be described by a one sentence comment)

Controversy:

- When do different principles conflict (eg. consistency/redundant lines)






