import hashlib

f = open('1511336521207_20171122_152252.png', 'rb')

sh = hashlib.sha512()
sh.update(f.read())
print sh.hexdigest() 

f.close()
