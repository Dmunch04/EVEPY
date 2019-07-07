## EVE

EVE is an lightweight data-interchange format. This repo contains the EVE library for a lot of languages (Hopefully will soon). This means that if you want to contribute, then you need to follow the exact EVE syntax of how it should work.

<br>

### ToDo

This is the global ToDo list for EVE

- Make it be able to handle one-liners (Find something to split the variables)

<br>

### Example

You can find a good example of how EVE looks, in the [example file](/Examples/Example.eve)

<br>

### ATOM grammar syntax highlighting

You can find the syntax file which is named: `EVE.cson`, which is located in the [grammars folder](grammars).

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
  - Mover   : Moves every character in the string 3 characters up the alphabet
- List
  - Upper   : Makes all string values in the list uppercase
  - Lower   : Makes all string values in the list lowercase

Examples:

```eve
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

If you wanna create an EVE library in another language, or optimize an already existing library, then fork this repo and make a pull request. Do note that the library should follow the exact EVE syntax/way of working. You should add a new language the same way, as the Python one is added!

<br>

## Authors

- [Dmunch04](https://github.com/Dmunch04) - Initial Work & Python Version

<br>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
