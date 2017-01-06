'''this script was originally written to change a batch of files all in the same folder / directory with the
following names -   Gl.-013-gedenkteken-van-blauw-float-en-Azul-split.txt  the user wanted to remove the "."
and move the number to the end of the filename.'''

import os

''' asks user what directory or folder they want files renamed'''
directory = raw_input("Please Enter directory path. macOS - Drag folder (directory) into terminal: ")

'''changes to the user inputted directory'''
os.chdir(directory)

for f in os.listdir(directory):
    ''' f_name and f_ext are the front part of the file name and the extension, this splits them into two parts, nothing to change here'''
    f_name, f_ext = os.path.splitext(f)
    ''' the following splits the file name into more pieces so we can rearrange the order, remove unwanted white space and "." that are
    icluded in the text GI. which is referenced with f_gi .  each file part is split into a tuple. "f" just is my way of saying file
     we need the underscore for no spaces and "gi" - GI, "num" - number'''
    f_gi, f_num, f_ged, f_van, f_bla, f_float, f_en, f_azu, f_spl, = f_name.split('-')

    f_gi = f_gi.strip()[:2]
    f_num = f_num.strip()
    f_ged = f_ged.strip()
    f_van = f_van.strip()
    f_bla = f_bla.strip()
    f_float = f_float.strip()
    f_en = f_en.strip()
    f_azu = f_azu.strip()
    f_spl = f_spl.strip()

    re_named = '{}-{}-{}-{}-{}-{}-{}-{}-{}{}'.format(f_ged, f_van, f_bla, f_float, f_en, f_azu, f_spl, f_gi, f_num, f_ext)
    os.rename(f, re_named)
print("your files have been MFR!  Please check the resuts")
