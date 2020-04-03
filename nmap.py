#!/usr/bin/env python

import subprocess
import os
from cryptography.fernet import Fernet
import sys


def mainMenu():
  print('.' *108)
  print("\t\t\t=================>NMAP SCANNER BY JOKERS<===================")
  print('.' *108)
  print()
  print("\t\t\t\t1. ===========> DISCOVER THE HOST")
  print("\t\t\t\t2. ===========> DISCOVER THE OPEN PORT")
  print("\t\t\t\t3. ===========> DISCOVER THE OS")
  print("\t\t\t\t4. ===========> QUIT NMAP PROGRAM")

  choice = int(input(">>>>ENTER YOUR CHOICE: "))
  if choice == 1:
     host_discovery()
  elif choice == 2:
     port_discovery()
  elif choice == 3:
     os_discovery()
  elif choice == 4:
     clear()
  else:
     print("WRONG CHOICE")

def host_discovery():
 host = input("Enter Your Host:=> ")
 print('-' *50)
 print("C0D3D BY J0K3R5")
 print('-' *50)
 subprocess.check_call(["nmap","-V","-n","-Pn","-sn","-sL","-PE","-PP","-oN","host.txt",host])
 print('-' *50)

def port_discovery():
 prt_rng = input("Enter Your Host:=> ")
 print('-' *50)
 print("C0D3D BY J0K3R5")
 print('-' *50)
 subprocess.check_call(["nmap","-p","1-1000","-oN","prt_rng.txt",prt_rng])
 print('-' *50)

def os_discovery():
 os = input("Enter Your Host:=> ")
 print('-' *50)
 print("C0D3D BY J0K3R5")
 print('-' *50)
 subprocess.check_call(["nmap","-n","-F","-A","-Pn","-O","-sS","-oN","os.txt",os])
 print('-' *50)

def clear():
 os.system("cls || clear")

if __name__ == "__main__":
 mainMenu()

