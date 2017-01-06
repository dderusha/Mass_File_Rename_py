#import os
#[os.rename(f, f.replace('_', '-')) for f in os.listdir('.') if not f.startswith('.')]



import os

directory = raw_input("Please Enter directory path. macOS - Drag folder (directory) into terminal: ")
os.chdir(directory)

for f in os.listdir(directory):
    f_name, f_ext = os.path.splitext(f)
    #f_name.split('-')
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


'''paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk(directory)
        for filename in filenames)

for path in paths:
    # the '#' in the example below will be replaced by the '-' in the filenames in the directory
    newname = path.replace('.', '')
    if newname != path:
        os.rename(path, newname)
print ("done")'''
