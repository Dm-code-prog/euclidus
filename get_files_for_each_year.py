import os
os.chdir('C:\\new_age_python\\2021')

for d,dc,i in os.walk('C:\\new_age_python\\2021'):
    date = d.split('\\')[-1]
    for file in i:
        if file.endswith('.txt'):
            print(d + '\\' + file)
            os.rename(d+'\\'+file,date+'_'+file)
