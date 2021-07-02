#!/usr/bin/python3
import os
import sys
def main():
    if sys.argv[1] == sys.argv[1]:
      host = sys.argv[1]
      packet = sys.argv[2]
      if sys.platform == 'linux':
        os.system(f"ping -w {packet} {host}")
      elif sys.platform == 'win32':
          os.system(f"ping -w {packet} {host}")
      elif sys.platform == 'Mac':
          os.system(f"ping -w {packet} {host}")
      else:
          print("\nThis Programm Run on Windows, Linux, MacOS\n")
          sys.exit()
if __name__ == '__main__':
  try:
     main()
  except IndexError:
      print("\npython3 sm.py host packet\n")
      sys.exit()
