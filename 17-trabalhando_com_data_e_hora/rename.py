import os

for arquivo in os.scandir():
    file_oldname = arquivo.name
    print(file_oldname)
    if file_oldname == 'rename.py':
        continue
    else:
        file_newname = 'aula' + file_oldname
        print(file_newname)
        os.rename(file_oldname, file_newname)
