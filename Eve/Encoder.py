def dump (_Path, _Data, **_Options):
    return Dump (_Path, _Data **_Options)

def dumps (_Data, **_Options):
    return Dumps (_Data, **_Options)

def Dump (_Path, _Data, **_Options):
    with open (_Path, 'w+') as File:
        File.write (Dumps (_Data))

def Dumps (_Data, **_Options):
    if not isinstance (_Data, list):
        _Data = [_Data]

    Sections = []

    for I, Section in enumerate (_Data):
        Sections.append ('[')

        for Item in Section:
            Value = Section[Item]

            if isinstance (Value, str):
                Sections[I] += f'\n   \'{str (Item)}\' :: \'{str (Value)}\''

            elif isinstance (Value, list):
                Items = []
                for ListItem in Value:
                    Items.append (str (ListItem))

                Sections[I] += f'\n   \'{str (Item)}\' :: ({", ".join (Items)})'

            else:
                Sections[I] += f'\n   \'{str (Item)}\' :: {str (Value)}'

        Sections[I] += '\n];'

    Data = ''

    if len (Sections) <= 1:
        Data = ''.join (Sections)

    else:
        Data = '\n\n'.join (Sections)

    return str (Data)
