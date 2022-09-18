# python version 2.6.15 and less than

import bcrypt

my_password = bcrypt.hashpw('peter110!', bcrypt.gensalt)
print(my_password)
decrypt = bcrypt.hashpw('peter110!', my_password)
print(decrypt)
# if bcrypt.checkpw(password, hashed):
#     print("It Matches!")
# else:
#     print("It Does not Match :(")

