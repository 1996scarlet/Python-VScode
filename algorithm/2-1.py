import os, tarfile


def unpack_path_file(pathname):
    archive = tarfile.open(pathname, 'r:gz')
    for tarinfo in archive:
        if tarinfo.isfile() and tarinfo.name.endswith('gz'):
            archive.extract(tarinfo, os.getcwd())
            print('tarinfo', tarinfo.name)
            unpack_path_file(tarinfo.name)
    archive.close()


# def tarker(pathname):

# archive = tarfile.open('./00.tar.gz', 'r:gz')
# archive.extractall()
# archive.close()

# unpack_path_file('00.tar.gz')
unpack_path_file('00.tar.gz')
