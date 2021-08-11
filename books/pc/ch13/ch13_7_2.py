import shutil

try:
    shutil.rmtree('/tmp/tmpcopyied2')
except Exception as e:
    pass

try:
    shutil.rmtree('/tmp/tmpcopyied')
except Exception as e:
    pass

try:
    shutil.rmtree('/tmp/pyfiles')
except Exception as e:
    pass

try:
    shutil.rmtree('/tmp/pyfiles2')
except Exception as e:
    pass

# copy src to dest
shutil.copy('./ch13_7_2.py', '/tmp/abc')

# copy files, but preserve metadata (cp -p src dst)
shutil.copy2('./ch13_7_2.py', '/tmp/abc')

# copy directory tree (cp -R src dst)
shutil.copytree('tmp', '/tmp/tmpcopyied', symlinks=True)

# move src to dst (mv src dst)
shutil.move('/tmp/tmpcopyied', '/tmp/tmpcopyied2')

shutil.copytree('.', '/tmp/pyfiles',
                ignore=lambda dirname, filenames: [name for name in filenames if name.endswith('.py')], symlinks=True)

shutil.copytree('.', '/tmp/pyfiles2', ignore=shutil.ignore_patterns('*~', '*.txt'))
