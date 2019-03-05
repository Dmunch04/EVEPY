#    Each line (splittet): ('line1', '::', 'value')
#                            ^1^     ^2^     ^3^
#    1 = Name    2 = Operator/Definer    3 = Value
#
#    Comment line (splittet): ('@ comment')
#    Check if the first char is ^ then we can conclude it's a comment
#
#    But first make sure the first char in the list is '[', then find
#    the closing ('];') and proceed!

# Imports
import os

# Lists for checking
numbers = '0123456789'

# Keywords for boolean and define functions
boolwords = ['True', 'true', 'False', 'false']
definewords = ['Define', 'define', 'Quit', 'quit']

# File templates
template_default = "[\n\n  $Define = None\n\n  'Line1' :: 'Element1'\n\n  $Quit = Off\n\n];"

# Defining words
keywords = ['string', 'float', 'int']
stringwords = ['upper', 'lower', 'spaces']
floatwords = ['round']
intwords = ['add', 'subtract', 'multiply', 'divide']

# The load function :: Loads the given file, and returns a dictionary with results
def load (path):
    # Get the file contents and make it a list
    content = list(open(path, 'r'))

    # Loop through every line in the contents list
    for i, element in enumerate(content):
        # Replace new lines and tabs with nothing
        content[i] = content[i].replace('\n', '')
        content[i] = content[i].replace('\t', '')

    # Loop through all the lines again
    for ist, element in enumerate(content):
        # Check if the current line is an open bracket
        if content[ist] == '[':
            # If so, loop through the lines again. But this time so it will
            for ien, element in enumerate(content):
                # Check if the current line is an close bracket
                if content[ien] == '];':
                    # If so, check the text inside it

                    # Create variables
                    temp = ''
                    insides = []
                    elements = []
                    results = []

                    # Get all lines between the open and close bracket
                    for i, element in enumerate(content[ist : ien]):
                        # Set the temp variable to the current line, but with replace spaces
                        temp = content[i].replace(' ', '')

                        # Check if the current line/temp starts with @
                        if temp.startswith('@'):
                            # Ignore it/go to next line
                            continue

                        # Check if the current line/temp starts with /////
                        elif temp.startswith('/////'):
                            continue

                        # Check if the current line/temp starts with [
                        elif temp.startswith('['):
                            # Ignore it/go to next line
                            continue

                        # Check if the current line/temp starts with ]
                        elif temp.startswith(']'):
                            # Ignore it/go to next line
                            continue

                        # Check if the current line/temp is empty
                        elif temp == '':
                            # Ignore it/go to next line
                            continue

                        # Checks if the current line starts with {
                        elif temp.startswith('{'):
                            # If so, then loops through all lines from that line
                            for identifer, definer in enumerate(content[i : ]):
                                # Then checks if the current line's last char is }
                                if definer[-1:] == '}':
                                    # Creates the string variable define
                                    define = ''
                                    # Sets the define variable to definer but with replaced chars
                                    define = definer.replace(' ', '')
                                    define = define.replace('{', '')
                                    define = define.replace('}', '')
                                    define = define.replace('\n', '')
                                    define = define.replace('.', ' ')
                                    define = define.split(' ')

                                    # Creates a list called value that splits the content on spaces
                                    values = content[i + 1].split(' ')
                                    # Creates a string variable called value that's assigned to the
                                    # values list from fourth element and up
                                    value = ' '.join(values[4:])

                                    # Creates and empty list called result
                                    result = []
                                    # Appends the first four elements from the values list
                                    result.append(values[0:4])

                                    # --- TODO: Make comments ---

                                    # Checks if the first word inside the {} is a keyword
                                    if define[0].lower() in keywords:
                                        # If so, then checks if the second (after dot) is in string words
                                        if define[1].lower() in stringwords:
                                            # Checks if the second word is equal to lower
                                            if define[1].lower() == 'lower':
                                                # If so, then sets the value to lowercase
                                                value = value.lower()
                                            # Checks if the second word is equal to upper
                                            elif define[1].lower() == 'upper':
                                                # If so, then sets the value to uppercase
                                                value = value.upper()
                                            # Checks if the second word is equal to spaces
                                            elif define[1].lower() == 'spaces':
                                                # If so, then replaces the ' in the value
                                                val = value.replace("'", '')
                                                # Makes the lst variable to a list
                                                lst = list(val)
                                                # Then sets the value to the lst seperated with a ,
                                                value = ', '.join(lst)

                                        # If it's not in string words, then checks if it's in float words
                                        elif define[1].lower() in floatwords:
                                            # If so, then checks if the second word is equal to round
                                            if define[1].lower() == 'round':
                                                # If so, then sets the value variable to the value rounded
                                                value = str(round(float(value)))

                                        # If it's not in float words, then checks if it's in int words
                                        elif define[1].lower() in intwords:
                                            # If so, then checks if the second word is equal to add
                                            if define[1].lower() == 'add':
                                                nums = []
                                                vals = value.split('+')

                                                for val in vals:
                                                    val = val.replace(' ', '')
                                                    for num in val:
                                                        if not num in numbers:
                                                            continue

                                                    nums.append(int(val))

                                                value = str(sum(nums))
                                            # If so, then checks if the second word is equal to subtract
                                            elif define[1].lower() == 'subtract':
                                                nums = []
                                                vals = value.split('-')
                                                sub_from = None

                                                for val in vals:
                                                    val = val.replace(' ', '')
                                                    for num in val:
                                                        if not num in numbers:
                                                            continue

                                                    nums.append(int(val))

                                                for num in nums:
                                                    if sub_from is None:
                                                        sub_from = num
                                                    else:
                                                        sub_from -= num

                                                value = str(sub_from)
                                            # If so, then checks if the second word is equal to multiply
                                            elif define[1].lower() == 'multiply':
                                                nums = []
                                                vals = value.split('*')
                                                mul_from = None

                                                for val in vals:
                                                    val = val.replace(' ', '')
                                                    for num in val:
                                                        if not num in numbers:
                                                            continue

                                                    nums.append(int(val))

                                                for num in nums:
                                                    if mul_from is None:
                                                        mul_from = num
                                                    else:
                                                        mul_from *= num

                                                value = str(mul_from)
                                            # If so, then checks if the second word is equal to divide
                                            elif define[1].lower() == 'divide':
                                                nums = []
                                                vals = value.split('/')
                                                div_from = None

                                                for val in vals:
                                                    val = val.replace(' ', '')
                                                    for num in val:
                                                        if not num in numbers:
                                                            continue

                                                    nums.append(int(val))

                                                for num in nums:
                                                    if div_from is None:
                                                        div_from = num
                                                    else:
                                                        div_from /= num

                                                value = str(div_from)

                                    # Adds the result value to the result list
                                    result[0].append(value)
                                    # Sets the next line of content to the result line
                                    content[i + 1] = ' '.join(result[0])

                        # If the current line does not match any above,
                        # then add it to the insides list
                        insides.append(content[i])

                    # Loop through all lines in the insides list
                    for i, line in enumerate(insides):
                        # Set the temp variable to the current line, but with replace spaces
                        temp = insides[i].replace(' ', '')

                        # Check if the line starts with a ?
                        if temp.startswith('?'):    # This is a variable
                            # Replace ' and ? in the line to nothing
                            line = line.replace("'", '')
                            line = line.replace('?', '')

                            # Split the line into words and symbols
                            elements = line.split()

                            # Checks if the bool keyword is valid
                            if not ' '.join(elements[2:]) in boolwords:
                                print('Unknown bool answer')
                                continue

                            try:
                                # Try and set the result message
                                res = (' '.join(elements[2:]), elements[1], elements[0])
                            except:
                                # Line is empty
                                continue

                            # Add the result text to the results list
                            results.append(res)

                        # Check if the line starts with a '
                        elif temp.startswith("'"):   # This is a normal text var
                            # Split the line into words and symbols
                            elements = line.split()

                            # Remove the '' around the parent/name
                            parent = elements[0].replace("'", '')

                            try:
                                # Try and set the result message
                                res = (' '.join(elements[2:]), elements[1], parent)
                            except:
                                # Line is empty
                                continue

                            # Add the result text to the results list
                            results.append(res)

                        # Check if the line starts with a ?
                        elif temp.startswith('$'):  # This is a definer
                            # Replace ' and $ in the line to nothing
                            line = line.replace("'", '')
                            line = line.replace('$', '')

                            # Split the line into words and symbols
                            elements = line.split()

                            # Checks if the definer keyword is valid
                            if not elements[0] in definewords:
                                print('Unknown define keyword')
                                continue

                            try:
                                # Try and set the result message
                                res = ("'" + ' '.join(elements[2:]) + "'", elements[1], elements[0])
                            except:
                                # Line is empty
                                continue

                            # Add the result text to the results list
                            results.append(res)

                    # Make the results list to a dictionary, so we can get items by name
                    results = dict([i[:: - 2] for i in results])

                    #print(results)
                    return results

            # This means that it doesn't have a ] or ;
            else:
                # Print an error
                print('[Error -> 2] Missing closing tags')
                # Then goes to the next lines
                return

    # This means that it doesn't have a [
    else:
        # Print an error
        print('[Error -> 1] Missing open bracket')
        # Then goes to the next lines
        return

# The read function :: Should only be used for EVE development, or experienced EVE developers!
def read (path):
    # Gets the file contents and makes it to a list
    content = list(open(path, 'r'))

    # Loops through the elements in content
    for i, element in enumerate(content):
        # Replace new lines and tabs with nothing
        content[i] = content[i].replace('\n', '')
        content[i] = content[i].replace('\t', '')

    # Loops through the elements in content, after replaces
    for ist, element in enumerate(content):
        # Check if the current line is an open bracket
        if content[ist] == '[':
            # If so, loop through the lines again. But this time so it will
            for ien, element in enumerate(content):
                # Check if the current line is an close bracket
                if content[ien] == '];':
                    # If so, check the text inside it

                    # Create variables
                    temp = ''
                    insides = []
                    elements = []
                    results = []

                    # Get all lines between the open and close bracket
                    for i, element in enumerate(content[ist : ien]):
                        # Set the temp variable to the current line, but with replace spaces
                        temp = content[i].replace(' ', '')

                        # Check if the current line/temp starts with @
                        if temp.startswith('@'):
                            # Ignore it/go to next line
                            continue

                        # Check if the current line/temp starts with /////
                        elif temp.startswith('/////'):
                            continue

                        # Check if the current line/temp starts with [
                        elif temp.startswith('['):
                            # Ignore it/go to next line
                            continue

                        # Check if the current line/temp starts with ]
                        elif temp.startswith(']'):
                            # Ignore it/go to next line
                            continue

                        # Check if the current line/temp is empty
                        elif temp == '':
                            # Ignore it/go to next line
                            continue

                        # If the current line does not match any above,
                        # then add it to the insides list
                        insides.append(content[i])

                    # Loop through all lines in the insides list
                    for i, line in enumerate(insides):
                        # Set the temp variable to the current line, but with replace spaces
                        temp = insides[i].replace(' ', '')

                        # Check if the line starts with a ?
                        if temp.startswith('?'):    # This is a variable
                            # Replace ' and ? in the line to nothing
                            line = line.replace("'", '')
                            line = line.replace('?', '')

                            # Split the line into words and symbols
                            elements = line.split()

                            try:
                                # Try and set the result message
                                res = (' '.join(elements[2:]), elements[1], elements[0])
                            except:
                                # Line is empty
                                continue

                            # Add the result text to the results list
                            results.append(res)

                        # Check if the line starts with a '
                        elif temp.startswith("'"):   # This is a normal text var
                            # Split the line into words and symbols
                            elements = line.split()

                            # Remove the '' around the parent/name
                            parent = elements[0].replace("'", '')

                            try:
                                # Try and set the result message
                                res = (' '.join(elements[2:]), elements[1], parent)
                            except:
                                # Line is empty
                                continue

                            # Add the result text to the results list
                            results.append(res)

                        # Check if the line starts with a ?
                        elif temp.startswith('$'):    # This is a definer
                            # Replace ' and $ in the line to nothing
                            line = line.replace("'", '')
                            line = line.replace('$', '')

                            # Split the line into words and symbols
                            elements = line.split()

                            try:
                                # Try and set the result message
                                res = (' '.join(elements[2:]), elements[1], elements[0])
                            except:
                                # Line is empty
                                continue

                            # Add the result text to the results list
                            results.append(res)

                    # Returns the results
                    return results

                # This means that it doesn't have a ] or ;
                else:
                    # Print an error
                    print('[Error -> 2] Missing closing tags')
                    # Then goes to the next lines
                    continue

        # This means that it doesn't have a [
        else:
            # Print an error
            print('[Error -> 1] Missing open bracket')
            # Then goes to the next lines
            continue

# The save function :: Saves the changed data to the given file
def save (content, path):
    # Calls the read function to get the content of the old file
    before = read(path)

    # Gets the parents/names of the file
    parents = list(content.keys())
    # Gets the values of the file
    values = list(content.values())

    # Loops through all lines in before
    for ib, line in enumerate(before):
        # Loops through all items in parents
        for ip, item in enumerate(parents):
            # Checks if last line == the current item
            if line[-1] == item:
                # Then checks if the current value is not the same as the old value
                if values[ip] != line[0]:
                    # Creates a list for all the items in before
                    blist = [list(elem) for elem in before]
                    # Then assigns the value to the current value
                    blist[ib][0] = "'{}'".format(values[ip])
                    # Then converts it to a tuple again
                    before = [tuple(elem) for elem in blist]

    # Opens the given file
    file = open(path, 'r')
    # Sets the variable content to a list of all the files lines
    content = file.readlines()
    # Closes the file
    file.close()

    # Creates the variable temp and set it to nothing
    temp = ''

    # Loops through all lines in the content list
    for li, line in enumerate(content):
        # Replaces spaces, ' and new lines to nothing, in the current line
        temp = line.replace(' ', '')
        temp = line.replace("'", '')
        temp = line.replace('\n', '')

        # Splist the temp (line) into words and symbols
        words = temp.split()

        # Make it a list
        lst = list(words)

        # Checks if the current line is nothing/empty
        if len(lst) == 0:
            # Then ignore it and go to next line
            continue

        # Loop through all line in before
        for i, element in enumerate(before):
            # Checks if the parent/name is equals to the current lines parent/name
            if "'{0}'".format(before[i][2]) == lst[0]:
                # Checks if the operator is ::
                if before[i][1] == '::':
                    # Sets the current lines content to this message (  'parent' :: value)
                    content[li] = "  '{0}' :: {1}\n".format(before[i][2], before[i][0])
                # If not, then checks if the operator is a =
                elif before[i][1] == '=':
                    # Sets the current lines content to this message (  ?parent = value)
                    content[li] = "  {0} :: {1}\n".format(before[i][2], before[i][0])

    # Opens the file again, but in write mode
    file = open(path, 'w')
    # Loops through every line in the contents
    for line in content:
        # Writes that line to the file
        file.write(line)
    # Closes the file
    file.close()

# The create function :: Creates a new file with the given filename and template
def create (path, template = ''):
    # Checks if the given path doesn't ends with .eve to make sure the file is an eve file
    if not path.endswith('.eve'):
        # If it doesn't ends with .eve, then add it to the path
        path += '.eve'

    # Checks if the directory does not exist
    if not os.path.exists(path):
        # If it doesn't exist, then print an error
        print('[Error -> 3] Directory does not exist')
        # Then returns out
        return

    # Checks if there's already a file with that name in the location
    if os.path.isfile(path):
        # If so, prints an error
        print('[Error -> 4] File already exists')
        # Then returns out
        return

    # Creates the text variable 'content' that will store the content
    content = ''

    # Checks if the given template is named default
    if template.lower().strip() == 'default':
        # If so, sets the content to that template
        content = template_default

    # Creates the file and opens it
    file = open(path, 'w+')
    # Writes all the content to the file
    file.write(content)
    # Closes the file
    file.close()
