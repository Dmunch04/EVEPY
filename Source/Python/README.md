## EVE - Python

This is the Python version (Original) of EVE.

### Installing

You can install it with pip (https://pypi.org/project/evepy/)

```
  pip install evepy
```

Another way is to clone the repo and import the Eve folder.
If none of them, you can also put the GitHub URL in your `requirements.txt` file (https://pip.pypa.io/en/stable/user_guide/#requirements-files)

<br>

### Upgrading Version

You can upgrade Eve with the following pip command:

```
  pip install evepy -U
```

<br>

### Example use

If you wanna see an example of how to use the EVE Python library, then check in the Examples folder.

<br>

## Methods
### Load Method (Alias: `load`)

The load method takes in a path to an Eve file, and returns the content.

```
  Load (Path)
```

### Loads Method (Alias: `loads`)

The loads method takes in an Eve data string and returns a dict of the content.

```
  Loads (Data)
```

### Dump Method (Alias: `dump`)

The dump method takes in a path and a dict of data, and then transforms the dict into Eve code and writes it to the file at the path.

```
  Dump (Path, Data)
```

### Dumps Method (Alias: `dumps`)

The dumps method takes in a dict of data and returns a string of Eve data.

```
  Dumps (Data)
```

### Parse Method (Alias: `parse`)

The Parse method takes in a dict of content and returns a `EveObject` class with the dict's keys as attributes, and their value to them.

```
  Parse (Data)
```
