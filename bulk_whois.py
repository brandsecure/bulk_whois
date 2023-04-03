# Import required libraries
import os
import csv
import whois
from datetime import datetime

# Generate a timestamp for the output file name
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_file = f'output_{timestamp}.csv'

# Read the list of domains from the 'domains.txt' file
with open('domains.txt', 'r') as file:
    domains = [line.strip() for line in file.readlines()]

# Open the output CSV file for writing
with open(output_file, 'w', newline='') as csvfile:
    # Define the CSV field names
    fieldnames = ['Domain', 'Registrar']
    
    # Create a CSV writer object and write the header row
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Iterate through the list of domains
    for domain in domains:
        print("Processing:", domain)
        try:
            # Perform a WHOIS query on the domain
            w = whois.whois(domain)
            registrar = w.registrar
            
            # Write the domain and registrar information to the CSV file
            if registrar is not None:
                writer.writerow({'Domain': domain, 'Registrar': registrar})
            else:
                writer.writerow({'Domain': domain, 'Registrar': '--ERROR QUERYING WHOIS SERVER--'})
        except Exception as e:
            # Handle exceptions and write an error entry to the CSV file
            print(f"Error processing {domain}: {e}")
            writer.writerow({'Domain': domain, 'Registrar': '--ERROR QUERYING WHOIS SERVER--'})
