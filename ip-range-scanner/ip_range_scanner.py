import socket


def get_public_ip_domain(ip_address):

    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name

    except socket.herror:
        return None


def scan_ip_range(start_ip, end_ip):
    available_ips = []
    for i in range(start_ip, end_ip + 1):
        ip_address = f"192.168.0.{i}"
        domain_name = get_public_ip_domain(ip_address)
        if domain_name:
            available_ips.append((ip_address, domain_name))
    return available_ips


start_ip = 1
end_ip = 255
results = scan_ip_range(start_ip, end_ip)
for ip, domain in results:
    print(f"IP Address: {ip}\tDomain Name: {domain}")