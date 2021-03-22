import pkgutil

data = pkgutil.get_data(__package__, 'somedata.dat')
print(data)

data2 = pkgutil.get_data(__package__, 'subdir/otherdata.dat')
print(data2)

