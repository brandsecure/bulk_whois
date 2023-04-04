import os
import csv
import whois
from datetime import datetime

def find_registrar_abuse_email(raw_data):
    if not raw_data:
        return None
    lines = raw_data.split('\n')
    for line in lines:
        if 'Registrar Abuse Contact Email:' in line:
            return line.split(': ')[1].strip()
    return None

timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_file = f'output_{timestamp}.csv'

with open('domains.txt', 'r') as file:
    domains = [line.strip() for line in file.readlines()]

with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Domain', 'Registrar', 'Registrar Abuse Email']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for domain in domains:
        print("Processing:", domain)
        try:
            w = whois.whois(domain)
            registrar = w.registrar
            registrar_abuse_email = find_registrar_abuse_email(w.text)

            writer.writerow({
                'Domain': domain,
                'Registrar': registrar if registrar else '--ERROR QUERYING WHOIS SERVER--',
                'Registrar Abuse Email': registrar_abuse_email if registrar_abuse_email else '--ERROR QUERYING WHOIS SERVER--',
            })
        except Exception as e:
            print(f"Error processing {domain}: {e}")
            writer.writerow({
                'Domain': domain,
                'Registrar': '--ERROR QUERYING WHOIS SERVER--',
                'Registrar Abuse Email': '--ERROR QUERYING WHOIS SERVER--',
            })
