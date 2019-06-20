from Eve.Models import Object

def Parse (_Data) -> Object.EveObject:
    EveData = Object.EveObject ()

    if isinstance (_Data, dict):
        for Key in _Data:
            Value = _Data.get (Key, None)

            setattr (EveData, Key, Value)

    elif isinstance (_Data, list):
        for Item in _Data:
            Name = f'Section{str (_Data.index (Item))}'
            setattr (EveData, Name, Object.EveObject ())

            for Key in Item:
                Value = Item.get (Key, None)

                Attribute = getattr (EveData, Name)
                setattr (Attribute, Key, Value)

    return EveData
