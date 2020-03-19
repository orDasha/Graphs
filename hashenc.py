import hashlib
# import unicodedata
# from sys import getdefaultencoding

# hx = hashlib.sha1()
# hy = hashlib.sha1()

def my_func_onesix(x, y):
    x.encode('utf-8')
    y.encode('utf-8')
    print(x.encode('utf-8'), y.encode('utf-8'))
    hx = hashlib.sha1(x.encode('utf-8')).hexdigest()
    hy = hashlib.sha1(y.encode('utf-8')).hexdigest()
    print(hx, hy)
    return hx == hy

x_str = 'Привет'
y_str = 'Привет!'

my_func_onesix(x_str, y_str)
print(my_func_onesix(x_str, y_str))