import nmap
import sys

def fast_comprehensive_scan(target_ip):
    print(f"\n[+] Starting Fast & Comprehensive Scan on: {target_ip}")
    print("[+] Running Default Scripts (-sC) and Version Detection (-sV)...")
    print("[+] Please wait, gathering data...\n")
    
    scanner = nmap.PortScanner()
    
    try:
        # Arguments: 
        # -sC : Run default Nmap scripts
        # -sV : Detect service versions
        # -T4 : Aggressive timing for faster execution
        # -Pn : Treat all hosts as online (skip ping sweep to save time)
        scan_args = '-sC -sV -T4 -Pn'
        
        # We are scanning top 1000 ports by default to save time. 
        # You can specify ports e.g., ports='1-10000'
        scanner.scan(hosts=target_ip, arguments=scan_args)
        
        if not scanner.all_hosts():
            print("[-] No response from the host.")
            return

        for host in scanner.all_hosts():
            print(f"--- Results for Host: {host} ---")
            print(f"State: {scanner[host].state()}")
            
            for proto in scanner[host].all_protocols():
                print(f"\nProtocol: {proto.upper()}")
                
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    state = scanner[host][proto][port]['state']
                    service = scanner[host][proto][port].get('name', 'unknown')
                    version = scanner[host][proto][port].get('version', '')
                    
                    print(f"[+] Port: {port}\tState: {state}\tService: {service} {version}")
                    
                    # Agar Nmap script ne kuch extra info nikaali hai
                    if 'script' in scanner[host][proto][port]:
                        for script_name, script_output in scanner[host][proto][port]['script'].items():
                            print(f"    -> {script_name}: {script_output.strip()}")
                            
    except nmap.PortScannerError as e:
        print(f"[-] Nmap error: {e}")
    except KeyboardInterrupt:
        print("\n[-] Scan cancelled by user.")
        sys.exit()
    except Exception as e:
        print(f"[-] Unexpected error: {e}")

if __name__ == "__main__":
    target = input("Enter the target IP or Domain: ")
    fast_comprehensive_scan(target)