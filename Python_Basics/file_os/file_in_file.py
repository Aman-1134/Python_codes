import os
import datetime as dt

base_path = '../Course_Name'
if not os.path.exists(base_path):
    os.mkdir(base_path)

folders = [f"day-{num}" for num in range(0, 21)]
#print(folders)

for i, folder_name in enumerate(folders):

    our_path = os.path.join(base_path, folder_name)

    if not os.path.exists(our_path):
        os.mkdir(our_path)

    with open(f"{our_path}/Notes.note",'w') as f:
        today = dt.datetime.now() + dt.timedelta(days = i)
        today = today.strftime('%B - %d - %Y ')
        f.write(f"Date : {today}")