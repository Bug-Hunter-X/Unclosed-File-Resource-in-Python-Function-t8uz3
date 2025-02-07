def function_with_unclosed_file(filename):
    file = open(filename, 'w')
    file.write('some text') # forgot to close the file
    # ... more code ...
    return