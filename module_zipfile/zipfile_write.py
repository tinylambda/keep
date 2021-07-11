from zipfile_infolist import print_info
import zipfile

print('creating archive')
with zipfile.ZipFile('write.zip', mode='w') as zf:
    print('adding zipfile_write.py')
    zf.write('zipfile_write.py')
print()
print_info('write.zip')

