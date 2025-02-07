# Python Helper Guide

## Imports

To use objects or functions defined in file A in file B the following can be used. If all of A is needed use the first line. If only part is needed use the second line

```
import A
from A import part
```

## Configs

The above section can be used to create configs which are just standalone dictionaries defined in a file. This can be seen in the config.py file and the following line can be used to add config to any other python file as long as they exist in the same folder.

```
from config import config
```

## Main Functions

Every file that is created for the most part should have a main function of the form below. This should not contain much at all and should not contain any code critical to someone repurposing your code in other files because there is no way to use the import function on it. The most common case for putting code in this block is for testing purposes while developing. It will allow you to add testing pieces that are not relevant to someone else using your code. This block should almost always be at the very bottom of any file it is in. 

```
if __name__ == "__main__":
    # Code to be executed when the script is run directly
    pass
```

## Function Definitions

Every function that is defined for the most part should be defined in the following format. This indicates the data types of the inputs and outputs of the functions and makes it easier for others to implement your functions.

```
def function_name(argument1: type1, argument2: type2) -> return_type:
    # Function body

```

## Example 1

example1.py includes examples of everything mentioned up until this point.