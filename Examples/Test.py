import Eve

Result = Eve.Parse (Eve.Load ('Test.eve'))

print (dir (Result))

"""
If the file only has 1 section, you can access variables like this:
print (Result.MyVar1)
print (Result.MyVar2)
print (Result.MyVar3)
"""

"""
If the file contaions more than one section, you'll need to access them like this:
print (Result.Section0.MyVar1)
print (Result.Section0.MyVar2)
print (Result.Section0.MyVar3)
print (Result.Section1.MyVar4)
"""
