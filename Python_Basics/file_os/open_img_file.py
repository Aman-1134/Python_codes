with open('Files/test.txt', 'r') as rf:
    with open('Files/test.copy.txt', 'w') as wf:
        rc = rf.read()
        wf.write(rc)

with open('image.png' , 'rb') as rf:
    with open('image.copy.png' ,  'wb') as wf:
        rc = rf.read()
        wf.write(rc)