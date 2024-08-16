import requests
import csv

def get_ip_info(ip_address):
    # IP Geolocation API
    geo_api_url = f"https://ipinfo.io/{ip_address}/json"
    geo_response = requests.get(geo_api_url)
    geo_info = geo_response.json()

    # Data to be written to CSV
    return {
        "IP Address": ip_address,
        "City": geo_info.get('city', 'N/A'),
        "State": geo_info.get('region', 'N/A'),
        "Country": geo_info.get('country', 'N/A'),
        "Postal Code": geo_info.get('postal', 'N/A'),
        "Time Zone": geo_info.get('timezone', 'N/A'),
    }

def process_bulk_ips(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8-sig') as infile:
            reader = csv.reader(infile)
            ip_addresses = [row[0] for row in reader]  # Assumes IP addresses are in the first column
        
        with open(output_filename, 'a', newline='', encoding='utf-8') as outfile:
            fieldnames = ["IP Address", "City", "State", "Country", "Postal Code", "Time Zone"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            
            # Write header only if the file is empty
            if outfile.tell() == 0:
                writer.writeheader()
            
            for ip_address in ip_addresses:
                ip_address = ip_address.strip()  # Remove any extra whitespace/newlines
                if ip_address:  # Check if the IP address is not empty
                    data = get_ip_info(ip_address)
                    writer.writerow(data)
                    print(f"Information for IP address {ip_address} has been written to {output_filename}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    input_filename = input("Enter the input filename containing IP addresses (e.g., ips.csv): ")
    output_filename = input("Enter the output filename to save the data (e.g., ip_info.csv): ")
    process_bulk_ips(input_filename, output_filename)

if __name__ == "__main__":
    main()
