IP Range Scanner

The IP Range Scanner is a Python script that scans a specified IP range and returns the available public-facing IP addresses along with their corresponding domain names. This can be useful for discovering the domain names associated with internal IP addresses in a local network.
Prerequisites

    Python 3.x installed on your system
    The socket module, which is included in the Python standard library

Usage

    Clone or download the script from the GitHub repository.

    Open a terminal or command prompt and navigate to the directory where the script is located.

    Modify the start_ip and end_ip variables in the script to define the IP range you want to scan. For example, if you want to scan the IP range 10.1.3.1 to 10.1.3.255, set start_ip = 1 and end_ip = 255.

    Run the script using the following command:

    bash

    python ip_range_scanner.py

    The script will scan the specified IP range and display the available public-facing IP addresses along with their corresponding domain names.

Example Output

less

IP Address: 10.1.3.10     Domain Name: example.com
IP Address: 10.1.3.23     Domain Name: example2.com
IP Address: 10.1.3.67     Domain Name: example3.com

Notes

    This script relies on the socket.gethostbyaddr() function from the socket module to retrieve the domain name associated with each IP address. It may not always be able to retrieve the domain name due to DNS configuration or other factors.

    Scanning IP addresses without proper authorization may violate the acceptable use policies or terms of service of your network or the networks you are scanning. Always ensure you have the necessary permissions and legal rights before performing any network scans.

    It's important to keep in mind that IP addresses and domain names can change over time. The script provides a snapshot of the domain names associated with IP addresses at the time of execution. Regularly updating and verifying the mappings is recommended.

License

This project is licensed under the MIT License.
Contributing

Contributions to this project are welcome. Feel free to open issues or submit pull requests to suggest improvements or fixes.