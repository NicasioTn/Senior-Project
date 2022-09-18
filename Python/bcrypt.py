import bcrypt

password = b"padmin10!2a"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# if bcrypt.checkpw(password, hashed):
#     print("It Matches!")
# else:
#     print("It Does not Match :(")

print(hashed)