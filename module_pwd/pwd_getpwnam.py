import pwd
import sys


username = sys.argv[1]
user_info = pwd.getpwnam(username)

print('Username:', user_info.pw_name)
print('Password:', user_info.pw_passwd)
print('Comment :', user_info.pw_gecos)
print('UID/CID :', user_info.pw_uid, '/', user_info.pw_gid)
print('Home    :', user_info.pw_dir)
print('Shell   :', user_info.pw_shell)

