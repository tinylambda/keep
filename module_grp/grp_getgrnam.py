import grp

name = "root"
info = grp.getgrnam(name)

print("Name: ", info.gr_name)
print("GID: ", info.gr_gid)
print("Password: ", info.gr_passwd)
print("Members: ", ", ".join(info.gr_mem))
