import os


root_dir = 'C:\Users\dant9'

file = os.path.join(root_dir, '../root_files.txt')

with open(file , 'w', encoding="utf-8") as f:
    f.write(str(os.listdir(root_dir)))
