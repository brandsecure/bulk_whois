import os
import csv
import whois
from datetime import datetime

# Name output file and append datestamp
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_file = f'bulk_whois_results_{timestamp}.csv'

# Specify the name/location of the text file containing a list of domains
with open('domains.txt', 'r') as file:
    domains = [line.strip() for line in file.readlines()]

# Add Columns for Domain and Registrar to the output file
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = ['Domain', 'Registrar']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
# Loop through the domains and perform the WHOIS lookup
    for domain in domains:
        print("Processing:", domain)
        try:
            w = whois.whois(domain)
            registrar = w.registrar
            if registrar is not None:
                writer.writerow({'Domain': domain, 'Registrar': registrar})
            else:
                writer.writerow({'Domain': domain, 'Registrar': 'ERROR: Unable to query whois database'})
        except Exception as e:
            print(f"Error processing {domain}: {e}")
            writer.writerow({'Domain': domain, 'Registrar': 'ERROR'})
