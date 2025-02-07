def function_with_closed_file(filename):
    try:
        file = open(filename, 'w')
        file.write('some text')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        file.close() # ensures the file is always closed, even if errors occur
    return