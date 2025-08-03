import subprocess
import os
from colorama import Fore,init
init(autoreset=True)




def zphisher():
    phish_repo = "https://github.com/htr-tech/zphisher.git"
    phish_clone = ["git", "clone", phish_repo]
    subprocess.run(phish_clone)
    print(Fore.RED + "[+] Zphisher Installation Complete")

def update():
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
    print(Fore.RED + "[+] Updated Successfully")


def camphish():
    cam_repo = "https://github.com/techchipnet/CamPhish.git"
    cam_clone = ["git", "clone", cam_repo]
    subprocess.run(cam_clone)
    print(Fore.RED + "[+] Camphish Installation Complete")


def geo():
    geolocator_repo = "https://github.com/Simit6155/GeoLocator.git"
    geolocator_clone = ("git", "clone", geolocator_repo)
    subprocess.run(geolocator_clone)
    print(Fore.RED + "[+] Geolocator Installation Complete")


def spam():
    spam_repo = "https://github.com/Simit6155/RedSpam.git"
    spam_clone = ["git", "clone", spam_repo]
    subprocess.run(spam_clone)
    print(Fore.RED + "[+] Spammbot Installation Complete")


def install_angry_ip_scanner():
    print("[+] Downloading Angry IP Scanner...")
    url = "https://github.com/angryip/ipscan/releases/download/3.9.1/ipscan_3.9.1_arm64.deb"
    subprocess.run(["wget", url, "-O", "ipscan.deb"], check=True)
    print(Fore.RED + "[+] Ip scanner Installation Complete")


    print("[+] Installing .deb package...")
    try:
        subprocess.run(["sudo", "dpkg", "-i", "ipscan.deb"], check=True)
    except subprocess.CalledProcessError:
        print("[!] dpkg failed, fixing broken dependencies...")
        subprocess.run(["sudo", "apt", "--fix-broken", "install", "-y"], check=True)

    print("[+] Cleaning up...")
    os.remove("ipscan.deb")

    print("[✓] Angry IP Scanner installed successfully.")


def install_nmap():
    print("[+] Installing Nmap...")
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "install", "-y", "nmap"], check=True)
    print("[✓] Nmap installed successfully.")


def install_tshark():
    print("[+] Installing tshark (command-line Wireshark)...")
    subprocess.run(["sudo", "apt", "update"], check=True)
    subprocess.run(["sudo", "apt", "install", "-y", "tshark"], check=True)
    print("[✓] tshark installed successfully.")



update()
install_nmap()
install_tshark()
spam()
camphish()
geo()
zphisher()
