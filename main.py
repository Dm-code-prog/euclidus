import os, shutil, time, pyautogui, euclidus
from automatic_encoding import *

os.chdir('C:\\new_age_python\\2021')
all_files = []
for d,di,i in os.walk('C:\\new_age_python\\2021'):
    date = d.split('\\')[-1]
    if len(i)>1:
        for g in i:
            all_files.append(g)

files = []
i = len(all_files)
while i > 0:
    files.append([all_files[i-1],all_files[i-2]])
    i = i-2
print(files[160])
time.sleep(5)
# for id,iteration in enumerate(files):
#     for g in iteration:
#         os.chdir('C:\\new_age_python\\2021')
#         shutil.copy(g, 'C:\\new_age_python\\file_for_alignment')
#     euclidus.euclidus()
#     automatic_encoding()
#     dir = 'C:\\new_age_python\\file_for_alignment'
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))







