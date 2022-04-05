import time
from functools import lru_cache
@lru_cache(maxsize=32)
def tim(n):
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now Starting")
    tim(5)
    print("Once done. Going Once again........")
    tim(3)
    print("Done. Going Once again........")
    tim(2)
    print("Done. Going Once again........")
    tim(4)
    print("Done")