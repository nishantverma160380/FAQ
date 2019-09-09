#!/usr/bin/python
"""
This encryption file uses pycrypto python library. which can be installed by doing
pip install pycrypto.
"""
import base64
import random, string
import hashlib
import sys
import getopt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
BLOCK_SIZE = 16

#key = get_random_bytes(16)
#initialization_vector = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
key = b'1122334455667788'
initialization_vector = b'1122334455667788'

def _pad(s):
    return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def encrypt(input_file, output_file):

    with open(input_file, 'r') as file:
        everything = file.read()
        lines = everything.split('\n')

    print "encrypting file... "
    output = generate(lines)

    f = open(output_file, 'w')
    f.write(output)
    f.close()

    k = open('secret-'+output_file, 'w')
    k.write(base64.b64encode(key)+','+initialization_vector)
    k.close()

    print "done"


def generate(lines):
    output = ''
    for line in lines:
        data_array = line.split(',')
        if len(data_array) > 4:
            state = data_array[0]
            raw_data = line.strip()
            # print(raw_data[-3:-1])
            cipher = AES.new(key, AES.MODE_CBC, initialization_vector)
            print("---------------state-----------------")
            print(state)
            print(hashlib.sha256(state).hexdigest())
            print("---------------raw_data-----------------")
            print(raw_data)
            print(hashlib.sha256(raw_data).hexdigest())
            print("---------------hashed_data-----------------")
            hashed_data = hashlib.sha256(state + raw_data).hexdigest()
            # print((state + raw_data).encode('utf-8'))
            print(hashed_data)
            print("--------------encrypted_data-------------------------")
            print(_pad(raw_data))
            encrypted_data = base64.b64encode(cipher.encrypt(_pad(raw_data)))
            print(encrypted_data)
            print("---------------------------------------")
            new_row = ("%s,%s,%s" % (state, encrypted_data, hashed_data)) + "\n"
            output += new_row

    return output


if __name__ == "__main__":
    argv = sys.argv[1:]
    input_file = ''
    output_file = ''
    count = None

    def usage():
        print 'encrypt.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

    if input_file == '' or output_file == '':
        usage()

    encrypt(input_file, output_file)
