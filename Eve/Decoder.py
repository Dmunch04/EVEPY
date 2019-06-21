import os

from Eve.Helpers.Helper import CheckValue, Keywords, OptionWords

def load (_Path, **_Options):
    return Load (_Path, **_Options)

def loads (_Data, **_Options):
    return Loads (_Data, **_Options)

def Load (_Path, **_Options):
    with open (_Path, 'r') as File:
        return Loads (File.read (), **_Options)

def Loads (_Data, **_Options):
    if isinstance (_Data, str):
        Data = _Data.split ('\n')

    else:
        Data = _Data

    StartFound = False
    EndFound = False
    Content = []
    Sections = []
    SectionIndex = -1
    CurrentSectionData = {}
    ToApply = ''

    for Line in Data:
        if Line in ' \n\t':
            continue

        FixedLine = Line.replace (' ', '').replace ('\n', '').replace ('\t', '')

        if FixedLine.startswith ('@'):
            continue

        if FixedLine == '[' and StartFound == False and EndFound == False:
            StartFound = True

        elif FixedLine == '];' and StartFound == True and EndFound == False:
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

        if Splitted[0].startswith ("'") and Splitted[0].endswith ("'") or Splitted[0].startswith ('"') and Splitted[0].endswith ('"'):
            Key = Splitted[0][1 : len (Splitted[0]) - 1]
            Value = Splitted[1].split ('@')[0]

            if Value.startswith ('(') and Value.endswith (')'):
                Values = Value[1 : len (Value) - 1].split (',')

                FinishedValues = []
                for XValue in Values:
                    XValue = CheckValue (XValue, CurrentSectionData)

                    FinishedValues.append (XValue)

                if ToApply:
                    Apply = ToApply.lower ().split ('.')
                    if Apply[0] in Keywords:
                        if Apply[1] in OptionWords[Apply[0]]:
                            FinishedValues = OptionWords[Apply[0]][Apply[1]] (FinishedValues)
                            ToApply = ''

                CurrentSectionData[Key] = FinishedValues

            else:
                if ToApply:
                    Apply = ToApply.lower ().split ('.')
                    if Apply[0] in Keywords:
                        if Apply[1] in OptionWords[Apply[0]]:
                            Value = f"{OptionWords[Apply[0]][Apply[1]] (Value)}"
                            ToApply = ''

                Value = CheckValue (Value, CurrentSectionData)

                CurrentSectionData[Key] = Value

    if SectionIndex == -1:
        print ('No section detected! (\'[]\')')
        return

    elif SectionIndex == 0:
        return Sections[0]

    else:
        Content.append (Sections)
        return Content[0]
