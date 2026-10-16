
import socket

HOST = "127.0.0.1"
PORT = 8888
BANNER = b"Demo Test Service v1.0\r\n"


def main():
    with socket.socket(
        socket.AF_INET, socket.SOCK_STREAM
    ) as server:
        server.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1
        )
        server.bind((HOST, PORT))
        server.listen(5)

        print(f"Test server running at {HOST}:{PORT}")
        print("Keep this terminal open while testing.")
        print("Press Ctrl+C to stop.")

        try:
            while True:
                connection, address = server.accept()

                with connection:
                    print(
                        f"Connection from {address[0]}:"
                        f"{address[1]}"
                    )
                    connection.sendall(BANNER)

        except KeyboardInterrupt:
            print("\nTest server stopped.")


if __name__ == "__main__":
    main()
