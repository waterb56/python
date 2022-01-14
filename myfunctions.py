def NiceOutput(text):
    numchars = len(text)
    middle = 45 - int(numchars / 2)
    print('#' * 90)
    print(" " * middle + text)
    print('#' * 90)
