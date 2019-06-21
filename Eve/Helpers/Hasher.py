LowerLetters = 'abcdefghijklmnopqrstuvwxyz'
UpperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Letters = LowerLetters + UpperLetters
Numbers = '0123456789'
Combined = Letters + Numbers

def Move (_Data, _Salt = 3):
    NewString = ''

    for Char in _Data:
        if Char in LowerLetters:
            MovedChar = LowerLetters[(LowerLetters.index (Char) + 3) % len (LowerLetters)]
            NewString += MovedChar

        elif Char in UpperLetters:
            MovedChar = UpperLetters[(UpperLetters.index (Char) + 3) % len (UpperLetters)]
            NewString += MovedChar

        else:
            NewString += Char

    return NewString
