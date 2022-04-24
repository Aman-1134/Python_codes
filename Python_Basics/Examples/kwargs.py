def num(**kwargs):
    #print(f"my name is {kwargs[0].key()} {kwargs[1].}")
    #for i in kwargs.keys():
     #   print(i)
    #for i in kwargs.values():
     #   print(i)
    #for i in kwargs.items():
     #   print(i)
   print(f"my name is {kwargs['lname']} {kwargs['fname']}")
   print(f"my name is {kwargs.get('lname')} {kwargs.get('fname')}")
num(lname='aman',fname='ansari')