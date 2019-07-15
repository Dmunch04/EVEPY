import os
from DavesLogger import Logs

from Eve.Helpers.Helper import CheckValue, Keywords, OptionWords

def load (_Path: str, **_Options) -> dict:
    return Load (_Path, **_Options)

def loads (_Data: str, **_Options) -> dict:
    return Loads (_Data, **_Options)

def Load (_Path: str, **_Options) -> dict:
    with open (_Path, 'r') as File:
        return Loads (File.read (), **_Options)

def Loads (_Data: str, **_Options) -> dict:
    Data = _Data.split ('\n') if isinstance (_Data, str) else _Data

    StartFound = False
    EndFound = False
    Content = []
    Sections = []
    SectionIndex = -1
    CurrentSectionData = {}
    ToApply = ''

    for Line in Data:
        if Line.strip () in ' \n\t':
            continue

        FixedLine = Line.replace (' ', '').replace ('\n', '').replace ('\t', '').strip ()

        if FixedLine.startswith ('@'):
            continue

        if FixedLine.startswith ('[') and not (StartFound and EndFound):
            StartFound = True

        elif FixedLine.endswith ('];') and StartFound and not EndFound:
            EndFound = True

        if StartFound and EndFound:
            SectionIndex += 1

            Sections.append (CurrentSectionData)

            CurrentSectionData = {}

            StartFound = False
            EndFound = False

        if FixedLine.startswith ('{') and FixedLine.endswith ('}'):
            ToApply = FixedLine[1 : len (FixedLine) - 1]

        Splitted = FixedLine.split ('::')

        if Splitted[0].startswith ('\'') and Splitted[0].endswith ('\'') or Splitted[0].startswith ('"') and Splitted[0].endswith ('"'):
            Key = Splitted[0][1 : len (Splitted[0]) - 1]
            Value = Splitted[1].split ('@')[0]

            # It's a list
            if Value.startswith ('(') and Value.endswith (')'):
                Values = Value[1 : len (Value) - 1].split (',')

                Elements = []
                for Element in Values:
                    Element = CheckValue (Element, CurrentSectionData)

                    Elements.append (Element)

                if ToApply:
                    Apply = ToApply.lower ().split ('.')
                    if Apply[0] in Keywords and Apply[1] in OptionWords[Apply[0]]:
                        Elements = OptionWords[Apply[0]][Apply[1]] (Elements)
                        ToApply = ''

                CurrentSectionData[Key] = Elements

            # It's not a list
            else:
                if ToApply:
                    Apply = ToApply.lower ().split ('.')

                    if Apply[0] in Keywords and Apply[1] in OptionWords[Apply[0]]:
                        Value = str ({OptionWords[Apply[0]][Apply[1]] (Value)})
                        ToApply = ''

                Value = CheckValue (Value, CurrentSectionData)

                CurrentSectionData[Key] = Value

    if SectionIndex == -1:
        Logs.Error ('No section detected! (\'[]\')')

        return

    elif SectionIndex == 0:
        return Sections[0]

    else:
        Content.append (Sections)

        return Content[0]
