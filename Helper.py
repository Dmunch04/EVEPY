from hashlib import md5

Keywords = ['string', 'math', 'hash', 'list']
OptionWords = {
    'string': {
        'upper': lambda X: str (X.upper ()),
        'lower': lambda X: str (X.lower ())
    },

    'math': {
        'eval': lambda X: str (eval (X)),
        'round': lambda X: int (round (float (X)))
    },

    'hash': {
        'md5': lambda X: str (md5 (X.encode ()).hexdigest ())
    },

    'list': {
        'upper': lambda List: ListChanger (List, 'upper'),
        'lower': lambda List: ListChanger (List, 'lower')
    }
}

def ListChanger (_List, _Change):
    if _Change.lower () == 'upper':
        for I in range (len (_List) - 1):
            if isinstance (_List[I], str):
                _List[I] = _List[I].upper ()

    elif _Change.lower () == 'lower':
        for I in range (len (_List)):
            if isinstance (_List[I], str):
                _List[I] = _List[I].lower ()

    return _List

def CheckValue (_Value, _CurrentSectionData):
    Value = _Value
    CurrentSectionData = _CurrentSectionData

    if not (Value.startswith ("'") and Value.endswith ("'") or Value.startswith ('"') and Value.endswith ('"')):
        try:
            Value = int (Value)
        except:
            try:
                Value = float (Value)
            except:
                try:
                    Value = eval (Value)
                except:
                    if not Value.lower () in ['true', 'false']:
                        if Value in CurrentSectionData:
                            Value = f"'{CurrentSectionData[Value]}'"

                        else:
                            print ('No key found:', Value)
                            return

    if not (isinstance (Value, int) or isinstance (Value, float) or Value.lower () in ['true', 'false']):
        Value = Value[1 : len (Value) - 1]

    if isinstance (Value, str) and Value.lower () in ['true', 'false']:
        if Value.lower () == 'true':
            Value = True

        elif Value.lower () == 'false':
            Value = False

    return Value
