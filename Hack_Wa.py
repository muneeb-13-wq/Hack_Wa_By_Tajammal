import os, sys
os.system("git pull")
try:
    __import__("Tajammal").menu()
except Exception as e:
    exit(str(e))
vjm