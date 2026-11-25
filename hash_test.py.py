from pwdlib import PasswordHash
p1=passwordHash.recommend()
password="soviet99"
hp=p1.hash(password)
print("your hash code is :",hp)