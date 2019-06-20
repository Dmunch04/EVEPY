# EVE

EVE is an lightweight data-interchange format.

<br>

### Getting Started

These instructions will help you get started using EVE

<br>

### Installing

You can install it with pip (https://pypi.org/project/evepy/)

```
pip install evepy
```

Another way is to clone the repo and import the python file (`Eve.py`)
If none of them, you can also put the GitHub URL in your `requirements.txt` file (https://pip.pypa.io/en/stable/user_guide/#requirements-files)

<br>

### Upgrading Version

You can upgrade Eve with the following pip command:

```
pip install evepy -U
```

<br>

### Example use

Here are examples of how to use EVE

Example.eve

```
[
  @ Simple Stuff
  'String' :: 'Hello, World!'     @ A simple string : Hello, World
  'Int' :: 5                      @ A simple int    : 5
  'Float' :: 6.9                  @ A simple float  : 6.9
  'Bool' :: False                 @ A simple bool   : False
  'List' :: ('a', 1, False)       @ A simple list   : ['a', 1, False]

  @ Advanced Stuff
  {String.Upper}
  'Advanced_String' :: 'Hello, World!'      @ An advanced string    : HELLO, WORLD!
  {Math.Eval}
  'Advanced_Math' :: (5 + 2) * 3            @ Doing math            : 21
  {Math.Round}
  'Advanced_Float' :: 6.9                   @ Float rounding        : 7
  {Hash.MD5}
  'Advanced_Hashing' :: 'Hello, World!'     @ Hashing strings       : 65a8e27d8879283831b664bd8b7f0ad4
  {List.Lower}
  'Advanced_List' :: ('A', 'B', 'C')        @ Changing list values  : ['a', 'b', 'c']

  'Math_List' :: (10 + 10, (5 + 2) * 3)     @ Doing math in list    : [20, 21]

  @ And much more!
];

[
  @ Btw, you can have multiple sections.
  'IsGonnaUseEVE?' :: True
];
```

<br>
Example.py

```py
import Eve

# Load a file :: load(path)
Data = Eve.Load ('Example.eve')

# Print variables (Prints: Hello, World!)
print (Result[0]['String'])
```

Parsing:
```py
import Eve

Data = Eve.Parse (Eve.Load ('Test.eve'))

print (dir (Data))

"""
If the file only has 1 section, you can access variables like this:
print (Data.MyVar1)
print (Data.MyVar2)
print (Data.MyVar3)
"""

"""
If the file contaions more than one section, you'll need to access them like this:
print (Data.Section0.MyVar1)
print (Data.Section0.MyVar2)
print (Data.Section0.MyVar3)
print (Data.Section1.MyVar4)
"""
```

<br>

### ATOM grammar syntax highlighting

You can find the syntax file which is named: `EVE.cson`

<br>

## Methods
### Load Method

The load method takes in a path to an eve file, and returns the content

```
Load (Path)
```

### Loads Method

The loads method takes in EVE data and returns a dict of the content

```
Loads (Data)
```

<br>

## Features
### Variable Marking

The variable defining feature let's you control different variables

Supported definers:
- String
  - Upper   : Makes the string uppercase
  - Lower   : Makes the string lowercase
- Math
  - Eval    : Calculates the variable value
  - Round   : Rounds up a float to nearest 1
- Hash
  - MD5     : Hashes the variable value with MD5
- List
  - Upper   : Makes all string values in the list uppercase
  - Lower   : Makes all string values in the list lowercase

Examples:

```
[
  @ This here will always make the string uppercase (Return: 'MARTIN')
  {String.Upper}
  'Name' :: 'martin'

  @ This here will add the numbers (Return: 7)
  {Math.Eval}
  'Number' :: 5 + 2

  @ This will round up the float (Return: 7)
  {Math.Round}
  'Float' :: 6.7
];
```

<br>

## Contribute

Feel free to make a pull request, so you can help create Eve!
And also feel free to create Eve in other languages!

## Authors

* **Dmunch04** - **Initial Work** - [EVE] (https://github.com/Dmunch04)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
