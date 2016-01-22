#!/usr/bin/python3

import datetime

# undefined :: a
undefined = None

# main :: IO Int
def main():
    fmt = "%Y,%j,%H,%M,%S,%f"
    print(datetime.datetime.now().strftime(fmt))
    print(datetime.datetime.strptime(datetime.datetime.now().strftime(fmt), fmt))
    return 0

if __name__ == "__main__" :
  exit(main())

# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et fdm=indent fdl=0 fdn=1:
# vim:cinw=if,elif,else,for,while,try,except,finally,def,class:
