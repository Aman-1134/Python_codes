with open('Files/test.txt', 'r') as names_file:
    with open('Files/test.copy.txt', 'w') as name5_files:
        names = names_file.readlines()

        for name in names:
            name = name[:-1]
            try:
                if len(name) > 5:
                    raise Exception('Name length greater than 5')
                else:
                    name5_files.write(name + '   ')
            except Exception as e:
                print(e)
            else:
                print(f"Wrote {name} to new file")
