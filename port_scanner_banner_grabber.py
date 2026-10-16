
import argparse
import socket


def scan_port(target_ip, port, timeout=1.0):
    """Check whether a TCP port accepts a connection."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((target_ip, port)) == 0
    except OSError:
        return False


def grab_banner(target_ip, port, timeout=3.0):
    """Try to read the service's initial banner."""
    try:
        with socket.create_connection(
            (target_ip, port), timeout=timeout
        ) as sock:
            sock.settimeout(timeout)

            try:
                data = sock.recv(1024)
            except socket.timeout:
                return "No immediate banner received."

            if not data:
                return "Connected, but no banner was sent."

            return data.decode(
                "utf-8", errors="replace"
            ).strip()

    except OSError as error:
        return f"Banner grab failed: {error}"


def main():
    parser = argparse.ArgumentParser(
        description="Port Scanner and Service Banner Grabber"
    )

    parser.add_argument(
        "target",
        nargs="?",
        default="127.0.0.1",
        help="Authorized target IP or hostname"
    )

    parser.add_argument(
        "--start", type=int, default=1,
        help="Starting TCP port"
    )

    parser.add_argument(
        "--end", type=int, default=100,
        help="Ending TCP port"
    )

    parser.add_argument(
        "--timeout", type=float, default=1.0,
        help="Connection timeout in seconds"
    )

    parser.add_argument(
        "--no-banner", action="store_true",
        help="Skip banner grabbing"
    )

    args = parser.parse_args()

    if not 1 <= args.start <= args.end <= 65535:
        parser.error("Use a valid port range from 1 to 65535.")

    if args.timeout <= 0:
        parser.error("Timeout must be greater than zero.")

    try:
        target_ip = socket.gethostbyname(args.target)
    except socket.gaierror:
        parser.error("Unable to resolve target hostname.")

    print("=" * 55)
    print("PORT SCANNER AND SERVICE BANNER GRABBER")
    print("=" * 55)
    print(f"Target: {args.target} ({target_ip})")
    print(f"Port range: {args.start}-{args.end}")
    print("-" * 55)

    open_ports = []

    for port in range(args.start, args.end + 1):
        if scan_port(target_ip, port, args.timeout):
            print(f"[OPEN] TCP/{port}")
            open_ports.append(port)

    print("-" * 55)
    print(f"Scan complete. Open ports: {len(open_ports)}")

    if not open_ports:
        print("No open ports found in this range.")
        return

    if args.no_banner:
        return

    print("\nSERVICE BANNER RESULTS")
    print("-" * 55)

    for port in open_ports:
        print(f"\nTCP/{port}")
        print(grab_banner(target_ip, port))

    print("\nProject execution finished.")


if __name__ == "__main__":
    main()
