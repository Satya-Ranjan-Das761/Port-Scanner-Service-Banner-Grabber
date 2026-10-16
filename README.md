
# Port Scanner and Service Banner Grabber

## Project Overview
A Python cybersecurity project that scans TCP ports
and attempts to collect service banners from open ports.

## Features
- TCP port scanning
- Open port detection
- Service banner grabbing
- Configurable port ranges
- Connection timeouts
- Local testing server

## Technologies
- Python 3
- Socket programming
- TCP/IP networking

## Project Files
- port_scanner_banner_grabber.py
- banner_test_server.py
- requirements.txt
- README.md
- .gitignore

## How to Run

Scan your own computer:

    python port_scanner_banner_grabber.py 127.0.0.1 --start 1 --end 100

Test the banner grabber:

1. Start the local test server:

       python banner_test_server.py

2. In another terminal, run:

       python port_scanner_banner_grabber.py 127.0.0.1 --start 8888 --end 8888

3. Expected banner:

       Demo Test Service v1.0

## Limitations
Some services do not send a banner immediately.
A missing banner does not necessarily mean the service is absent.

## Disclaimer
Use this project only on localhost, systems you own,
or systems for which you have explicit permission.
