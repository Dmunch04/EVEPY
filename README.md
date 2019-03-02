# EVE
A lightweight data-interchange format.


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

```python
import eve

result = eve.load('example.eve')
print(result['Name']) # And so on
result['Age'] = '22'
eve.save(result, 'example.eve')
```
