import os

os.chdir('/home/shijin/py_works/files_exp/')

for f in os.listdir():
    #Separate file name and ext
    f_name,f_ext = os.path.splitext(f)
    f_title,f_func,f_num = f_name.split("_")

    #strip off any whitespaces
    f_title = f_title.strip()
    f_func = f_func.strip()
    #stripoff whitespaces, omit first letter # and zero pad for 2 digits eg 04
    f_num = f_num.strip()[1:].zfill(2)

    new_fname = '{}-{}-{}{}'.format(f_num,f_title,f_func,f_ext)
    #print(new_fname)
    os.rename(f, new_fname)



