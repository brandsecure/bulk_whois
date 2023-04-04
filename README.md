# Bulk WHOIS Lookup Script

This simple Python script performs bulk WHOIS lookups for domain names listed in a `domains.txt` file and outputs the results to a CSV file named `output_YYYY-MM-DD.csv`. The output file includes the following columns: Domain, Registrar, and Registrar Email. If the script encounters an error while querying WHOIS data, the corresponding field will be replaced with `--ERROR--`.

## Prerequisites

- Python 3.6 or higher
- `whois` Python library

## Installation

1. Clone the repository or download the script files.
```
git clone https://github.com/brandsecure/bulk_whois.git
```
2. Install the required Python library.
```
pip install python-whois
```

## Usage

1. Add the list of domain names you want to lookup in the `domains.txt` file, with one domain per line.
2. Run the Python script:
```
python bulk_whois.py
```
3. The script will create a CSV file named `output_YYYY-MM-DD.csv` in the same directory, containing the Domain, Registrar, and Registrar Email columns. If there's an error while querying the WHOIS data, the corresponding field will be replaced with `--ERROR--`.

## Note

Please be aware of the rate limiting policies of WHOIS servers when using this script for bulk lookups. Running a large number of queries in a short period of time may lead to temporary or permanent IP blocking by the WHOIS servers.



