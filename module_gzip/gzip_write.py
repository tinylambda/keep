import gzip
import io
import os


outfilename = '/tmp/example.txt.gz'
with gzip.open(outfilename, 'wb') as output:
    with io.TextIOWrapper(output, encoding='utf-8') as enc:
        enc.write('Contents of the example file goes here.\n')

print(outfilename, 'contains', os.stat(outfilename).st_size, 'bytes')
os.system('file -b -mime {}'.format(outfilename))

