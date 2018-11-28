import os, tarfile


def unpack_path_file(pathname,mdir):
    archive = tarfile.open(pathname, 'r:gz')
    adir = ''
    for tarinfo in archive:
        if tarinfo.isfile() and tarinfo.name.endswith('gz'):
            print('tarinfo', mdir + '/' + tarinfo.name, adir)
            archive.extract(tarinfo, mdir)
            unpack_path_file(mdir + '/' + tarinfo.name, mdir + '/' + adir)
        elif tarinfo.isdir():
            adir = tarinfo.name
        else:
            archive.extract(tarinfo, './ojbk/' + mdir)
            # archive.extract(tarinfo, './ojbk')
    archive.close()

# unpack_path_file('00.tar.gz', '.')
counter = 0
summer = 0
for root, dirs, files in os.walk("./ojbk", topdown=False):
    for name in files:
        with open(os.path.join(root, name)) as f:
            print(os.path.join(root, name))
            ss = f.readline()
            if(ss != ''):
                print(ss)
                summer += int(ss)
            counter += 1

print (counter, summer)
    # for name in dirs:
        # print(os.path.join(root, name))
