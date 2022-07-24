import random
import time

a = "qwertyuiop"
b = "DEFAULT"
c = "012345678910"
d = "[]{}()*/'-"

all = a + b+ c+ d
length = 8
password = "".join(random.sample(all, length))
print("Відбувається генерація паролю зачекайте...")
time.sleep(3)
print("Ваш пароль готово:")
print(password)
print("Хорошого дня вам")
input()
