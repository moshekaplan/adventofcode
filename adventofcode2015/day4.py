import sys
from hashlib import md5
import itertools

def crack_secret(secret):
    for i in itertools.count():
        hash = md5(secret + str(i)).hexdigest()
        if hash.startswith("00000"):
            print i, hash
            return i

def crack_secret2(secret):
    for i in itertools.count():
        hash = md5(secret + str(i)).hexdigest()
        if hash.startswith("000000"):
            print i, hash
            return i
            
def main():
    crack_secret2(sys.argv[1])

if __name__ == "__main__":
    if sys.argv < 2:
        print "USAGE: python day6.py secret"
        sys.exit(1)
    main()