import requests
import csv


def banner():
    print(r"""
                    _                           
                   / \   _ __ _ __   __ ___   __
                  / _ \ | '__| '_ \ / _` \ \ / /
                 / ___ \| |  | | | | (_| |\ V / 
                /_/   \_\_|  |_| |_|\__,_| \_/  
                                
                # Coded By Arnav Subudhi 
    """)


def get_ip_info(ip_address, filename):
    # IP Geolocation API
    geo_api_url = f"https://ipinfo.io/{ip_address}/json"
    geo_response = requests.get(geo_api_url)
    geo_info = geo_response.json()

    # Data to be written to CSV
    data = {
        "IP Address": ip_address,
        "City": geo_info.get('city', 'N/A'),
        "State": geo_info.get('region', 'N/A'),
        "Country": geo_info.get('country', 'N/A'),
        "Postal Code": geo_info.get('postal', 'N/A'),
        "Time Zone": geo_info.get('timezone', 'N/A'),
    }

    # Write data to CSV file
    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        
        # Write header only if the file is empty
        if file.tell() == 0:
            writer.writeheader()
        
        writer.writerow(data)

def main():
    banner()
    try:
        ip_address = input("Enter the IP address to scan: ")
        filename = input("Enter the filename to save the data (example: test.csv): ")
        get_ip_info(ip_address, filename)
        print(f"Information for IP address {ip_address} has been written to {filename}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
