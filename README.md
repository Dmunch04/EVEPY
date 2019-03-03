# EVE
EVE is an lightweight data-interchange format.



# Import
You can install it with pip (https://pypi.org/project/evepy/)

`pip install evepy`

Or clone the repo and use the python file (`eve.py`)

If none of them, you can also put the GitHub URL in your `requirements.txt` file (https://pip.pypa.io/en/stable/user_guide/#requirements-files)



# Example use
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
import evepy as eve

result = eve.load('example.eve')
print(result['Name']) # And so on
result['Age'] = '22'
eve.save(result, 'example.eve')
```



# ATOM grammar syntax highlighting
1. Copy the folder: `eve` in the `editors\atom` folder
2. Paste that to the `.atom` folder in `C:\Users\yourusername\.atom\packages`
3. Now restart ATOM and it should work
