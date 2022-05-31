import grp
import os


gid = os.getgid()
group_info = grp.getgrgid(gid)
print("Currently running with GID={}, name={}".format(gid, group_info.gr_name))
