import requests
import csv

def get_ip_info(ip_address):
    # IP Geolocation API
    geo_api_url = f"https://ipinfo.io/{ip_address}/json"
    geo_response = requests.get(geo_api_url)
    geo_info = geo_response.json()
    print("Geolocation Info:", geo_info)  # Debug print

    # IPWHOIS API
    # whois_api_url = f"http://ipwho.is/{ip_address}"
    # whois_response = requests.get(whois_api_url)
    # whois_info = whois_response.json()
    # print("WHOIS Info:", whois_info)  # Debug print

    # IPAPI for additional WHOIS details
    #ipapi_url = f"https://api.ipapi.com/api/{ip_address}?access_key=238204528ed14f14b3fba5d1ae8c6133"
    # ipapi_response = requests.get(ipapi_url)
    # ipapi_info = ipapi_response.json()
    # print("IPAPI Info:", ipapi_info)  # Debug print

    # Data to be written to CSV
    data = {
        "IP Address": ip_address,
        "City": geo_info.get('city', 'N/A'),
        "State": geo_info.get('region', 'N/A'),
        "Country": geo_info.get('country', 'N/A'),
        "Postal Code": geo_info.get('postal', 'N/A'),
        "Time Zone": geo_info.get('timezone', 'N/A'),
        # "ISP": ipapi_info.get('isp', 'N/A'),
        # "Domain": ipapi_info.get('domain', 'N/A'),
        # "Network Speed": ipapi_info.get('network_speed', 'N/A'),
        # "Proxy Known": ipapi_info.get('proxy', 'N/A'),
        # "ASN": ipapi_info.get('asn', 'N/A'),
        # "Organization": ipapi_info.get('organization', 'N/A'),
        # "ASN IP Range": ipapi_info.get('asn_ip_range', 'N/A'),
       
    }

    # Write data to CSV file
    with open('ip_info.csv', 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        
        # Write header only if the file is empty
        if file.tell() == 0:
            writer.writeheader()
        
        writer.writerow(data)

def main():
    ip_address = input("Enter the IP address to scan: ")
    get_ip_info(ip_address)
    print(f"Information for IP address {ip_address} has been written to ip_info.csv")

if __name__ == "__main__":
    main()
