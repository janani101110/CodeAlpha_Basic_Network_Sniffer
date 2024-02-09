import scapy.all as scapy #interactive packet manipulation program written in python
from scapy.layers import http #access HTTP layer functionalities provided by Scapy

def sniffing(interface): #initiate packet sniffing on the specific network interface
    scapy.sniff(iface=interface,store=False,prn=process_packet)

def process_packet(packet): #called for each packet captured by the sniffer. processes HTTP packets and extract the HTTP host header field.
    if packet.haslayer(http.HTTPRequest):
        print(packet[http.HTTPRequest].Host)


sniffing("Wi-Fi")    
                
