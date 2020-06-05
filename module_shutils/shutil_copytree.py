import glob
import pprint
import shutil


print('BEFORE: ')
pprint.pprint(glob.glob('/tmp/example/*'))

# The symlinks argument controls whether symbolic links are copied as links or as files. The default is to copy the
# contents to new files. If the option is true, new symlinks are created within the destination tree.
shutil.copytree('../module_shutils', '/tmp/example')

print('\nAFTER:')
pprint.pprint(glob.glob('/tmp/example/*'))

