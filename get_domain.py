# Find Domain Name From DNS Pointer (PTR) Records Using IP Address
# Write a function that takes an IP address and returns the domain name using PTR DNS records.

# Example
# get_domain("8.8.8.8") ➞ "dns.google"

# get_domain("8.8.4.4") ➞ "dns.google"
# Notes
# You may want to import socket.
# Don't cheat and just print the domain name, you need to make a real DNS request.
# Return as a string.

import socket

# def get_domain(ip_address):
#     try:
#         # Reverse the IP address for the PTR lookup
#         reversed_ip = '.'.join(reversed(ip_address.split('.')))
#         # Perform the PTR lookup by appending '.in-addr.arpa' to the reversed IP
#         domain = socket.gethostbyaddr(ip_address)[0]
#         return domain
#     except socket.herror:
#         return "Domain name not found"

# # Examples
# print(get_domain("8.8.8.8"))
# print(get_domain("208.67.222.222"))
# print(get_domain("1.1.1.1"))   # Should return "dns.google"
# print(get_domain("8.8.4.4"))  # Should return "dns.google"


# class Domain:
    
#     def __init__(self,ip_address ):
#         self.ip_address = ip_address

#     def get_domain(self):
#         try:
#         # Reverse the IP address for the PTR lookup
            
#         # Perform the PTR lookup by appending '.in-addr.arpa' to the reversed IP
#             domain = socket.gethostbyaddr(self.ip_address)[0]
#             return domain
#         except socket.herror:
#             return "Domain name not found"



import socket

class Domain:
    
    def __init__(self, ip_address):
        self.ip_address = ip_address
    
    def get_domain(self):
        try:
            # Perform the PTR lookup
            domain = socket.gethostbyaddr(self.ip_address)[0]
            return domain
        except socket.herror:
            return "Domain name not found"
mydomain =Domain("8.8.8.8")

print(mydomain.get_domain())