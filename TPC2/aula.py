import re
import sys
entradas ="""
hello world
goodbye world
hi, hello there
h ello
Hello there! Uh, hi, it's me... Heyyy,? HELLO!
""".strip().splitlines()

def main():
    """ 
    for line in sys.stdin:
        #print(re.match("hello",line) is not None)
    """
    for line in entradas:
        #print(re.match(r"hello",line,flags=re.IGNORECASE) is not None)
        #print("linha: "+line+";")
        print(f'(line) \n ->',re.sub((r'hello'),r'<b>\1</b>',line,flags=re.IGNORECASE))
if __name__ == "__main__":
    main()