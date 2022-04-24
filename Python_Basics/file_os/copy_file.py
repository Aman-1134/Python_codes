with open('Files/test.txt', 'r') as rf:
    with open('Files/test.copy.txt', 'w') as wf:
        rc = rf.read()
        wf.write(rc)