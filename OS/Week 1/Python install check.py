import subprocess
from apt.debfile import DebPackage
"""
Write a script that check whether a package is installed or not on a Debian based system.
Use the command line tool dpkg to execute this job.If the package is installed print a
message to the console that the package is already installed. If the package is not installed:
- check if the tool is started with root permission, if not, exit the script and tell the user that
root privileges are required to install the package
- install package
"""
# authorname : Thom Boer
# version : 0.1
# date : 10-01-2018

# you can run the deb install via dpkg or by a dedicated module that handles .deb packages

# variables i.e. packageName
app=input("Wich package do you want to check?")

# start a subporocess to execute a command
proc = subprocess.getoutput(["dpkg -l "+app])

#use the output from proc to determine whether the given package is installed or not
print("")
print(proc)

further = input("Do you want to install "+ app +"?")

#check root (if package not installed)
if further =="yes":
    print("Did you run this program as root?")
    root =input("if not, you need to restart the program with root rights")

#install package (if package not installed)
install = subprocess.getoutput("apt "+"install "+app)
print(install)