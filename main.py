import hashlib

file = None
md5_pass = "f9fa10ba956cacf91d7878861139efb9";

try:
    file = open("passwords.txt","r")
except:
    print("file not found")
    exit()

for password in file:
    hashobj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()

    if hashobj == md5_pass:
        print("%s is the password" % (password))
