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

### Example use

Here are examples of how to use EVE

example.eve

```
[
  @ This is a comment

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

result = eve.load('example.eve')
print(result['Name'])
result['Age'] = '22'
eve.save(result, 'example.eve')
```

### ATOM grammar syntax highlighting

1. Copy the folder: `eve` from the `editors\atom` folder
2. Paste that to the `.atom` folder in `C:\Users\yourusername\.atom\packages`
3. Now restart ATOM and it should work

## Authors

* **Dmunch04** - **Initial Work** - [EVE] (https://github.com/Dmunch04)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
