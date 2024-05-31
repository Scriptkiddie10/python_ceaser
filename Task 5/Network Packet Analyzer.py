from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[+] New Packet: {ip_layer.src} -> {ip_layer.dst}")
        print(f"    Protocol: {ip_layer.proto}")
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"    TCP Payload: {tcp_layer.payload}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"    UDP Payload: {udp_layer.payload}")

print("Starting packet sniffer...")
sniff(prn=packet_callback, store=0)

