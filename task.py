import string
import random
import hashlib
import argparse

def str_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size)).encode('utf-8')

def hash_generator(n, byte=None):
    gen_str = str_generator(n)
    a = hashlib.md5(gen_str).hexdigest()
    if byte is None:
        return a, gen_str
    else:
        while True:
            if a[0:2] != byte:
                gen_str = str_generator(n)
                a = hashlib.md5(gen_str).hexdigest()
            else: 
                return a, gen_str

def save_to_file(hash):
    filename=args.filename
    file = open(filename, 'a')
    file.seek(0)
    file.write(hash)
    file.close
    return

def get_arg_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--md5_first_byte", dest = "md5_first_byte", help="md5_first_byte", type=str)
    parser.add_argument("-n", "--number", dest = "number", default = 10, help="number", type=int)
    parser.add_argument("-f", "--filename",dest ="filename", help="filename", default = "randomfile.txt", type=str)

    return parser.parse_args()

args = get_arg_parser()
hash = hash_generator(args.number, args.md5_first_byte) 
string_to_write = 'Generated string: ' + str(hash[1].decode()) + '  MD5: ' + str(hash[0])
save_to_file(string_to_write + '\n')
print(string_to_write)