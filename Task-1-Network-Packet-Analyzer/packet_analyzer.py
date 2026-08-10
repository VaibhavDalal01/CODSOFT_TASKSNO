from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def analyze_packet(packet):
    print("\n" + "=" * 60)
    print("PACKET CAPTURED")
    print("=" * 60)

    if IP in packet:
        ip_layer = packet[IP]

        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")

        if TCP in packet:
            print("Protocol       : TCP")
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print("Protocol       : UDP")
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif ICMP in packet:
            print("Protocol       : ICMP")

        else:
            print("Protocol       : Other")

        if Raw in packet:
            print(f"Payload        : {packet[Raw].load}")

    else:
        print("Non-IP Packet")
        print(packet.summary())


def main():
    print("Network Packet Analyzer")
    print("Starting packet capture...")
    print("Press Ctrl+C to stop.\n")

    try:
        sniff(prn=analyze_packet, count=20)

    except KeyboardInterrupt:
        print("\nPacket capture stopped.")

    except PermissionError:
        print("Permission denied. Run with administrator/root privileges.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
