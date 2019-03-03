#    Each line (splittet): ('line1', '::', 'value')
#                            ^1^     ^2^     ^3^
#    1 = Name    2 = Operator/Definer    3 = Value
#
#    Comment line (splittet): ('@ comment')
#    Check if the first char is ^ then we can conclude it's a comment
#
#    But first make sure the first char in the list is '[', then find
#    the closing ('];') and proceed!

# Keywords for boolean and define functions
boolwords = ['True', 'true', 'False', 'false']
definewords = ['Define', 'define', 'Quit', 'quit']

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
                            # Replace ' in the line to nothing
                            line = line.replace("'", '')

                            # Split the line into words and symbols
                            elements = line.split()

                            try:
                                # Try and set the result message
                                res = ("'" + ' '.join(elements[2:]) + "'", elements[1], elements[0])
                            except:
                                # Line is empty
                                continue

                            # Add the result text to the results list
                            results.append(res)

                        # Check if the line starts with a ?
                        ekif temp.startswith('$'):    # This is a definer
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
