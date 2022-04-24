import os
# os.rmdir('sort_demo')
if not os.path.exists('sort_demo'):
    os.mkdir('sort_demo')

folders = [f"day-{num}" for num in range(0, 21)]
print(folders)

for folder_name in folders:
    base_path = 'sort_demo'
    our_path = os.path.join('sort_demo', folder_name)

    if not os.path.exists(our_path):
        os.mkdir(our_path)
folders_2 = [f"day-{str(num).zfill(3)}" for num in range(0, 21)]
print(sorted(folders_2))
print(os.getcwd())
#print(list(map(lambda x,y: os.rename(x,y),folders,folders_2)))

os.chdir('sort_demo')
print(os.getcwd())
for i, name in enumerate(folders):

    os.rename(name, folders_2[i])
