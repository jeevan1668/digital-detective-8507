# Mission 7 - How Computers Communicate

## 1. Task / objective
Explain common network concepts, observe a connectivity test and DNS lookup, and describe what happens when a website opens.

## 2. Work completed
- Summarized LAN, MAN, WAN, DNS, routers, protocols, packet switching and client-server communication.
- Checked connectivity to `example.com` with `ping`.
- Looked up `example.com` with `nslookup`.
- Described the browser-to-server steps.

## 3. Commands / tools used
- `ping -c 4 example.com` - sent four connectivity-test packets to the example domain.
- `nslookup example.com` - queried DNS for the domain's address records.

## 4. My understanding

### Task 7.1 - Network concepts

| Concept | Explanation | Example |
| :--- | :--- | :--- |
| LAN | A network in a small area | Home or school network |
| MAN | A network covering a city or large campus | A city-wide public network |
| WAN | A network covering a large geographic area | The Internet |
| DNS | Finds the IP address associated with a domain name | Looking up `example.com` |
| Router | Forwards data between networks | A home router connecting devices to an Internet service |
| Protocol | A set of rules devices use to communicate | HTTP for web requests; DNS for name lookups |
| Packet switching | Splits data into packets that can travel across networks and be reassembled | A web page's data sent in network packets |
| Client-server | A client requests a service and a server responds | A browser requests a page from a web server |

### Task 7.2 - Connectivity and DNS observations

- `ping -c 4 example.com`: 4 packets transmitted, 4 received, 0% packet loss; average round-trip time was about 13.4 ms.
- `nslookup example.com`: the configured DNS server responded with addresses `104.20.23.154` and `172.66.147.243`.
- A connectivity test checks whether a destination responds over the network and gives an indication of delay or packet loss.
- A DNS lookup asks a DNS server to find the address records associated with a domain name. The browser uses DNS results to find the server to contact.
- The returned addresses may change over time or vary by resolver and location.

### Task 7.3 - What happens when a website opens?

1. The user enters a website name in the browser, which acts as the client.
2. The client asks DNS for an address associated with that name.
3. DNS returns one or more IP addresses.
4. The browser connects to the server through the local network and router, using network protocols.
5. The browser sends an HTTP request to the server; the data travels in packets.
6. The server sends a response, and the browser assembles and displays the page.

## 5. Difficulties faced
No major difficulties were recorded during the connectivity and DNS checks.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- This README with the privacy-safe command results

## 8. Commit details
Committed as `Explain networking concepts and website communication` and pushed to `update-about`.
