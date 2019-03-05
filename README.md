# EVE

EVE is an lightweight data-interchange format.

### Getting Started

These instructions will help you get started using EVE

### Installing

You can install it with pip (https://pypi.org/project/evepy/)

```
pip install evepy
```

Another way is to clone the repo and import the python file (`eve.py`)
If none of them, you can also put the GitHub URL in your `requirements.txt` file (https://pip.pypa.io/en/stable/user_guide/#requirements-files)

### Upgrading Version

You can upgrade Eve with the following pip command:

```
pip install evepy -U
```

### Strict Grammer Rules

EVE currently have very strict grammar rules, to avoid errors. Please follow them:

1. Make a new line for every variable - Don't have mutliple on one line
2. Make sure the name of text variables have quotes around it - Ex: `'Parent/Name' :: 5`, not `Parent/Name = 5`
3. Make sure to have a **;** after the end bracket
4. Make sure to have spaces between parents, operators and values - Ex: `'Parent' :: 'Value'`, not `'Parent'::'Value'`. The same thing for other functions
5. Make sure to have the right define symbols in front - Ex: `$Define = 'Method'`, not `Define = 'Method'`
6. Don't make comment on lines with code - Ex: `@A new line for comments`, not `?bool = False @Don't do this!`
7. Of course also make sure to have the opening and closing brackets
8. Make sure you don't have any other math symbols in the specified type of equation
9. When making a definer, make sure the targeted line is right beneath
10. Make sure to use the right symbols in the different types

### Example use

Here are examples of how to use EVE

example.eve

```
[
  @ This is a comment

  @ Definers
  @ This is like a kind of title
  $Define = 'Test File'

  @ Defined variables
  @ This will make the 'uName' variable lowercase
  {String.Lower}
  'uName' :: 'Martin'
  @ This will make the 'uCity' variable uppercase
  {String.Upper}
  'uCity' :: 'New York'

  @ String variables
  'Name' :: 'Eric'
  'Age' :: '21'
  'Country' :: 'USA'
  'City' :: 'New York'

  @ Boolean variables
  ?hasGirlfriend = False
];
```
example.py

```python
import eve

# Load a file :: load(path)
result = eve.load('example.eve')

# Print variables
print(result['Name'])

# Change variables
result['Age'] = '22'

# Save to file :: save(content, path)
eve.save(result, 'example.eve')

# Create a file :: create(path, template)
eve.create('path/to/file.eve', 'default')
```

### ATOM grammar syntax highlighting

1. Copy the folder: `eve` from the `editors\atom` folder
2. Paste that to the `.atom` folder in `C:\Users\yourusername\.atom\packages`
3. Now restart ATOM and it should work

## Methods
### Load Method

The load method takes in a path to an eve file, and returns the content

```
load(path)
```

### Save Method

The save method saves changed content to a file. It takes in the new content and a path

```
save(changed_content, path)
```

### Create Method

The create method creates a new file at the given path. It also supports templates, but that's optional. Currently there's only the `default` template. Make sure to surround the template name with single quotes

```
create(path, template)
```

## Eve Features
### Structure

With the current build of Eve, it's important you follow this structure

Valid structure:

```
[

  @ Don't ever have comments on lines with code!

  $Define = 'MyFile'

  'Name' :: 'Martin'
  'Age' :: 21
  'City' :: 'New York'

  {String.Upper}
  'Country' :: 'usa'

  {Int.Add}
  'Sum' :: 1 + 2 + 100

];
```

Invalid structure:

```
[

  'Name' :: John
  'Age' :: 23
  'City' :: 'Berlin' @ He lives in Berlin
  Contry::'Germany'
  myBool = False

];
```

As you can see in the invalid structure example, that will give many errors. So please stick to the valid structure!

### Variables

You can make normal variables. To define these you need to use the `::` operator. Make sure to have space between the name, operator and value

Example:

```
[
  @ Will return 'string variable' when answer requested
  's_name' :: 'string variable'
  @ Will return 5 when answer requested
  'n_name' :: 5
];
```

### Booleans

You can of course also habe booleans. You can give them `True`, `true`, `False` or `false`.

Example:

```
[
@ Will return False when answer requested
  ?boolean = False
];
```

### Definers

You can use the definers `Define` & `Quit`. Define is the kind of title, and quit is not done yet.

Example:

```
[
@ Will return 'MyEveFile' when answer requested
  $Define = 'MyEveFile'
];
```

Or

```
[
  @ Will return None when answer requested
  $Define = None
];
```

### Variable Defining

The variable defining feature let's you control different variables

Supported definers:
- String (Has to be surrounded by single quotes)
  - Lower (Makes the string lowercase)
  - Upper (Makes the string uppercase)
  - Spaces (Seperates the string into letters)
- Float (Don't use commas, use dots)
  - Round (Rounds the float to nearest whole number)
- Int (Has to be an int)
  - Add (Adds up to multiple numbers and returns the sum)
  - Subtract (Subtracts up to multiple numbers and returns the sum)
  - Multiply (Multiplies up to multiple numbers and returns the sum)
  - Divide (Divides up to multiple numbers and returns the sum)

Examples:

```
[
  @ This here will always make the string uppercase (Return: 'MARTIN')
  {String.Upper}
  'Name' :: 'martin'

  @ This here will add the numbers (Return: 7)
  {Int.Add}
  'Number' :: 5 + 2

  @ This will round up the float (Return: 7)
  {Float.Round}
  'Float' :: 6.7
];
```

## Authors

* **Dmunch04** - **Initial Work** - [EVE] (https://github.com/Dmunch04)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
