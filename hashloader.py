import hashlib

file = None
try:
    file = open("passwords.txt","r")
except:
    print("file not found")
    exit()
    
for password in file:
    md5_hash = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    print(md5_hash)
