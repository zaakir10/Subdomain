import os
import subprocess

print("""
 ██████  ██████  ██████  ██████  ███    ██ ██████  ███████ 
██       ██   ██      ██      ██ ████   ██      ██      ██ 
██   ███ ██████   █████   █████  ██ ██  ██  █████      ██  
██    ██ ██   ██      ██      ██ ██  ██ ██      ██    ██   
 ██████  ██   ██ ██████  ██████  ██   ████ ██████     ██    
        https://github.com/zaakir10
        SUB-DOMAIN & HOST DISCOVERY TOOL                                                                                                          
""")

if not os.path.exists("/usr/bin/assetfinder"):
    print("\n\033[1;33m\t\t\t[+] installing asssetfinder on your system \033[0m\n")
    subprocess.run(["sudo", "apt", "install", "assetfinder", "-y"])
else:
    print("\n\033[1;33m[+] We are going to use asssetfinder installed on your system. \033[0m\n\n")

print("\033[1;33m\t\t\t[+] Harvesting subdomains\033[0m\n\n")

subdomain = input("Enter the domain to scan: ")

if not os.path.exists(subdomain):
    os.mkdir(subdomain)

def recon(directory):
    if not os.path.exists(f"{directory}/recon/"):
        print(f"creating a \033[1;34m {directory} \033[0m directory on your program location location\n\n")
        os.mkdir(f"{directory}/recon/")

recon(subdomain)

subprocess.run(["assetfinder", subdomain], stdout=open(f"{subdomain}/subdomains.txt", "w"))

if os.path.exists(f"{subdomain}/subdomains.txt"):
    print("\t\t\033[1;34mHarvesting hosts for the domains generated\033[0m\n\n")
    with open(f"{subdomain}/subdomains.txt", "r") as f:
        for host in f:
            host = host.strip()
            subprocess.run(["host", host], stdout=subprocess.PIPE, universal_newlines=True)
    with open(f"{subdomain}/subdomains-hosts.txt", "w") as f:
        for line in subprocess.check_output(["host", "-l", subdomain]).decode().split("\n"):
            if "has address" in line:
                f.write(line + "\n")

print(f"\t\033[1;32m[+]Done[+]\033[0m check \033[1;32m{subdomain}\033[0m/ recon for your \033[1;32mdata\033[0m")
