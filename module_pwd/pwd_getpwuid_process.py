import pwd
import os


uid = os.getuid()
user_info = pwd.getpwuid(uid)
print("Currently running with UID={} username={}".format(uid, user_info.pw_name))
