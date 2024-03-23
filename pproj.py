#!/bin/python3

import sys
import os

try:
    if(sys.argv[1] == "-new"):
        os.mkdir(sys.argv[2])
        os.chdir(sys.argv[2])
        os.mkdir("build")
        os.mkdir("src")
        os.chdir("..")
        with open(sys.argv[2] + "/Packages.list", "w") as c:
            c.write("")
        with open(sys.argv[2] + "/src/main.py", "w") as f:
            f.write("print(\"Hello world!\")")
    elif(sys.argv[1] == "-build"):
        with open("./Packages.list", "r") as d:
            k = d.read().split("\n")
            for kitem in k:
                os.system("pip install " + kitem)
        os.system("python3 ./src/main.py")
    elif(sys.argv[1] == "-add"):
        with open("./Packages.list", "a") as g:
            g.write(sys.argv[2] + "\n")
except:
    print("SOMETHING WENT WRONG!")
