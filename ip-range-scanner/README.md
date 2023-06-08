# IP Range Scanner
<p align="center">
<div style="display: flex; justify-content: center; align-items: center; width: 100%; height: 100vh;">
  <img align="center" src="https://www.wikitechy.com/technology/wp-content/uploads/2022/01/active-network-scanning.jpg" alt="Schedule screenshot" height="325" width="890" align="center">
</div>
<h1> </h1>
The IP Range Scanner is a Python script that scans a specified IP range and returns the available public-facing IP addresses along with their corresponding domain names. This can be useful for discovering the domain names associated with internal IP addresses in a local network.
<h1> </h1>

## Prerequisites

    Python 3.x installed on your system
    The socket module, which is included in the Python standard library

## Usage

    Clone or download the script from the GitHub repository.

    Open a terminal or command prompt and navigate to the directory where the script is located.

    Modify the start_ip and end_ip variables in the script to define the IP range you want to scan. 
    For example, if you want to scan the IP range 10.1.3.1 to 10.1.3.255, set start_ip = 1 and end_ip = 255.

    Run the script using the following command:

    bash

    python ip_range_scanner.py

    The script will scan the specified IP range and display the available public-facing IP addresses 
    along with their corresponding domain names.

## Example Output

less

    IP Address: 10.1.3.10     Domain Name: example.com
    IP Address: 10.1.3.23     Domain Name: example2.com
    IP Address: 10.1.3.67     Domain Name: example3.com

## Notes

    This script relies on the socket.gethostbyaddr() function from the socket module 
    to retrieve the domain name associated with each IP address. 
    It may not always be able to retrieve the domain
    name due to DNS configuration or other factors.

    Scanning IP addresses without proper authorization may violate the acceptable use
    policies or terms of service of your network or the networks you are scanning.
    Always ensure you have the necessary permissions and legal rights before performing
    any network scans.

    It's important to keep in mind that IP addresses and domain names can change over time. 
    The script provides a snapshot of the domain names associated with IP addresses at the time of execution
    Regularly updating and verifying the mappings is recommended.

### License

```
MIT License

Copyright (c) 2023 Mike Oduor Husein

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
## Contributing

    Contributions to this project are welcome. Feel free to open issues or submit pull requests to suggest improvements or fixes.
