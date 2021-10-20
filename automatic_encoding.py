import re,os

def automatic_encoding():
    os.chdir('C:\\new_age_python\\file_for_alignment')
    for id,i in enumerate(os.listdir()):
        if i.endswith('.xml'):
            with open(i, encoding='utf-8') as file:
                reader = file.readlines()
                os.chdir('C:\\new_age_python\\finished_files')
                with open(f'{i.split(".")[0]}_result.para','a', encoding='ANSI') as parafile:
                    for i in reader:
                        i = re.sub('<se lang="" variant_id="0">', '<se lang="adyghe" variant_id="0">', i)
                        i = re.sub('<se lang="" variant_id="1">', '<se lang="russian" variant_id="1">', i)
                        if not i.startswith('  <unhandled '):
                            try:
                                parafile.write(i)
                            except UnicodeEncodeError:
                                pass

automatic_encoding()