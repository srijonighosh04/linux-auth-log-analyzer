import sys

failed_ips = []

if len(sys.argv) < 2:
    print("Usage: python analyzer.py <logfile>")
    sys.exit(1)

logfile = sys.argv[1]

with open(logfile, "r") as f:
    lines = f.readlines()

for line in lines:
    if "Failed password" in line:
        parts = line.split()
        ip = parts[10]
        failed_ips.append(ip)

print("=== Suspicious IPs ===")
for ip in set(failed_ips):
    count = failed_ips.count(ip)
    if count >= 3:
        print(f"[!] {ip} -> {count} failed attempts")
