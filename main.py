# Kleines IP-Checker Python Script
import requests
import socket

public_ip4 = requests.get('https://www.wikipedia.org').headers['X-Client-IP']
hostname = socket.gethostname()
internal_ipv4 = socket.gethostbyname(hostname)

print("\n[+] Öffentliche IPv4: "+public_ip4)
print("[+] Interne IPv4: "+internal_ipv4)
print("[+] Hostname: "+hostname)