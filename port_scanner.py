import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

# Fixed color codes
RED = "\033[91m"    # Red for open ports
GREEN = "\033[92m"  # Green for banners
RESET = "\033[0m"


def get_banner(ip, port):
    """Attempt to grab banner from service"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))

        # Send basic requests for common services
        if port == 80:
            s.send(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
        elif port == 21:
            pass  # FTP usually sends banner immediately
        elif port == 22:
            pass  # SSH sends banner immediately
        elif port == 25:
            pass  # SMTP sends banner immediately
        else:
            # For other ports, try a generic request
            s.send(b"\r\n")

        banner = s.recv(1024).decode().strip()
        s.close()
        return banner[:100]  # Limit banner length
    except:
        return ''


def format_port_results(results):
    """Format and display scan results"""
    open_ports = [r for r in results if r[3]]  # Filter only open ports

    if not open_ports:
        return f"{RED}[-] No open ports found{RESET}\n"

    formatted_results = f"\n{GREEN}[+] Port Scan Results:{RESET}\n"
    formatted_results += f"{'-' * 60}\n"
    formatted_results += f"{'Port':<8} {'Service':<15} {'Status':<10} {'Banner':<20}\n"
    formatted_results += f"{'-' * 60}\n"

    # Sort by port number
    open_ports.sort(key=lambda x: x[0])

    for port, service, banner, status in open_ports:
        formatted_results += f"{RED}{port:<8}{RESET} {service:<15} {'Open':<10} "
        if banner:
            # Show first line of banner only
            banner_line = banner.split('\n')[0]
            formatted_results += f"{GREEN}{banner_line[:30]}{RESET}\n"
        else:
            formatted_results += "\n"

    formatted_results += f"{'-' * 60}\n"
    formatted_results += f"{GREEN}[+] Found {len(open_ports)} open ports{RESET}\n"

    return formatted_results


def scan_port(target_ip, port):
    """Scan a single port"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_ip, port))
        s.close()

        if result == 0:  # Port is open
            try:
                service = socket.getservbyport(port, 'tcp')
            except:
                service = 'Unknown'

            # Get banner for open ports
            banner = get_banner(target_ip, port)
            return port, service, banner, True
        else:
            return port, '', '', False
    except Exception as e:
        return port, '', '', False


def ports_scan(target_host, start_port, end_port):
    """Main scanning function"""
    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"{GREEN}[+] Starting scan on host: {target_ip}{RESET}")
        print(f"{GREEN}[+] Scanning ports {start_port}-{end_port}{RESET}")
    except socket.gaierror:
        print(f"{RED}[-] Error: Could not resolve hostname {target_host}{RESET}")
        return

    results = []
    open_count = 0

    with ThreadPoolExecutor(max_workers=400) as executor:  # Reduced workers
        futures = {executor.submit(scan_port, target_ip, port): port
                   for port in range(start_port, end_port + 1)}

        total_ports = end_port - start_port + 1

        for i, future in enumerate(as_completed(futures), start=1):
            port, service, banner, status = future.result()
            results.append((port, service, banner, status))

            if status:
                open_count += 1

            # Clean progress indicator - overwrite the line each time
            sys.stdout.write(
                f"\r{GREEN}[+] Progress: {i}/{total_ports} ports scanned, {open_count} open{RESET}")
            sys.stdout.flush()

    print(f"\n{format_port_results(results)}")


def main():
    """Main function with input validation"""
    print(f"{GREEN}{'='*50}")
    print("         PORT SCANNER")
    print(f"{'='*50}{RESET}")

    try:
        target_host = input(
            f"{GREEN}Enter target IP/hostname: {RESET}").strip()
        if not target_host:
            print(f"{RED}[-] Error: Please enter a valid target{RESET}")
            return

        start_port = int(input(f"{GREEN}Enter start port (1-65535): {RESET}"))
        end_port = int(input(f"{GREEN}Enter end port (1-65535): {RESET}"))

        # Validation
        if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
            print(f"{RED}[-] Error: Ports must be between 1-65535{RESET}")
            return

        if start_port > end_port:
            print(
                f"{RED}[-] Error: Start port must be less than end port{RESET}")
            return

        if end_port - start_port > 1000:
            confirm = input(
                f"{RED}Warning: Scanning {end_port - start_port + 1} ports. Continue? (y/N): {RESET}")
            if confirm.lower() != 'y':
                return

        ports_scan(target_host, start_port, end_port)

    except ValueError:
        print(f"{RED}[-] Error: Please enter valid port numbers{RESET}")
    except KeyboardInterrupt:
        print(f"\n{RED}[-] Scan interrupted by user{RESET}")
    except Exception as e:
        print(f"{RED}[-] Error: {str(e)}{RESET}")


if __name__ == '__main__':
    main()
