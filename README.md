# Port Scanner 🔍

A fast and efficient Port-Scanner with multithreading support for network reconnaissance and security testing.

## ⚠️ Legal Disclaimer

**This tool is for educational and authorized testing purposes only.**

- Only scan networks and systems you own or have explicit permission to test
- Unauthorized port scanning may be illegal in your jurisdiction
- Users are responsible for compliance with local laws and regulations
- The developers assume no liability for misuse of this tool

## 🚀 Features

- 🏃 **Fast Multithreaded Scanning**: Concurrent port scanning with configurable thread count
- 🎯 **Service Detection**: Identifies services running on open ports
- 🏷️ **Banner Grabbing**: Attempts to capture service banners for identification
- 📊 **Real-time Progress**: Live progress bar showing scan status
- 🌐 **Hostname Support**: Accepts both IP addresses and hostnames
- 🎨 **Colored Output**: Easy-to-read results with color-coded information
- ⚡ **Efficient Resource Usage**: Optimized for speed without overwhelming targets
- 🛡️ **Input Validation**: Comprehensive error handling and validation

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses built-in libraries)

### Clone the Repository

```bash
git clone https://github.com/AkshayRane05/Port-Scanner.git
cd Port-Scanner
```

### Make it Executable (Optional)

```bash
chmod +x port_scanner.py
```

## 📖 Usage

### Basic Syntax

```bash
python port_scanner.py
```

### Interactive Mode

Port-Scanner will prompt you for:

- Target IP address or hostname
- Start port number (1-65535)
- End port number (1-65535)

### Example Session

```
==================================================
         PORT SCANNER
==================================================
Enter target IP/hostname: 192.168.1.1
Enter start port (1-65535): 1
Enter end port (1-65535): 1000
[+] Starting scan on host: 192.168.1.1
[+] Scanning ports 1-1000
[+] Progress: 1000/1000 ports scanned, 5 open

[+] Port Scan Results:
------------------------------------------------------------
Port     Service         Status     Banner
------------------------------------------------------------
22       ssh             Open       SSH-2.0-OpenSSH_8.2p1
80       http            Open       Apache/2.4.41 (Ubuntu)
443      https           Open
3306     mysql           Open       5.7.34-0ubuntu0.18.04.1
8080     http-alt        Open       Jetty/9.4.z-SNAPSHOT
------------------------------------------------------------
[+] Found 5 open ports
```

## 🎯 Common Use Cases

### 1. **Network Discovery**

```bash
# Scan common ports on local network
python port_scanner.py
# Target: 192.168.1.1
# Ports: 1-1000
```

### 2. **Web Server Analysis**

```bash
# Focus on web-related ports
python port_scanner.py
# Target: example.com
# Ports: 80-90
```

### 3. **Service Enumeration**

```bash
# Scan well-known service ports
python port_scanner.py
# Target: 10.0.0.1
# Ports: 1-1024
```

### 4. **Custom Port Range**

```bash
# Scan specific port range
python port_scanner.py
# Target: localhost
# Ports: 8000-9000
```

## 🔧 Technical Details

### **Multithreading**

- Uses `ThreadPoolExecutor` with 100 concurrent workers
- Optimized for balance between speed and resource usage
- Prevents overwhelming target systems

### **Service Detection**

- Leverages Python's `socket.getservbyport()` for service identification
- Covers standard IANA port assignments
- Falls back to "Unknown" for unregistered ports

### **Banner Grabbing**

- Attempts to capture service banners for identification
- Sends appropriate requests for common services (HTTP, FTP, SSH, etc.)
- Timeout protection to prevent hanging connections

### **Progress Tracking**

- Real-time progress bar using `\r` character for line overwriting
- Shows ports scanned and open ports found
- Clean, single-line progress indicator

## 📊 Performance

### **Speed Metrics**

- **Local Network**: 500-1000 ports/second
- **Internet Hosts**: 100-500 ports/second (depends on latency)
- **Large Ranges**: Efficiently handles 1000+ port scans

### **Resource Usage**

- **Memory**: ~10-20MB for typical scans
- **CPU**: Moderate usage, scales with thread count
- **Network**: Minimal bandwidth per connection

## 🛡️ Security Considerations

### **Ethical Usage**

- Always obtain proper authorization before scanning
- Respect rate limits and avoid aggressive scanning
- Use for legitimate security testing and research only

### **Detection Avoidance**

- Consider using smaller port ranges for stealth
- Add delays between connections if needed
- Be aware that port scanning can be logged by target systems

## 🔍 Testing

### **Create Test Environment**

```bash
# Start test servers on different ports
python -m http.server 8080 &
python -m http.server 8081 &
python -m http.server 8082 &

# Scan the test servers
python port_scanner.py
# Target: localhost
# Ports: 8000-8100
```

### **Test with Real Services**

```bash
# Test against common services
python port_scanner.py
# Target: google.com
# Ports: 80-443
```

## 🚨 Troubleshooting

### **Common Issues**

| Problem               | Solution                                                |
| --------------------- | ------------------------------------------------------- |
| `Permission denied`   | Run with appropriate privileges or use ports >1024      |
| `Connection timeout`  | Target may be firewalled or non-responsive              |
| `Host unreachable`    | Check network connectivity and DNS resolution           |
| `Too many open files` | Reduce concurrent connections or increase system limits |

### **Error Messages**

- **"Could not resolve hostname"**: Check DNS settings and hostname spelling
- **"Connection refused"**: Port is closed or filtered
- **"Network unreachable"**: Check routing and network configuration

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- **Custom timeout settings**
- **Output format options** (JSON, CSV, XML)
- **Steganographic scanning techniques**
- **Integration with vulnerability databases**
- **GUI interface development**

### **Development Setup**

```bash
git clone https://github.com/AkshayRane05/Port-Scanner.git
cd Port-Scanner
# Make your changes
python port_scanner.py  # Test your changes
```

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚖️ Ethical Guidelines

This tool is provided for:

- ✅ Educational purposes and learning network security
- ✅ Testing your own networks and systems
- ✅ Authorized penetration testing with proper permissions
- ✅ Security research and vulnerability assessment

**NOT for:**

- ❌ Unauthorized scanning of systems you don't own
- ❌ Malicious reconnaissance or attack preparation
- ❌ Violating terms of service or acceptable use policies
- ❌ Any illegal activities

## 🙏 Acknowledgments

- Python's `socket` library for networking capabilities
- `concurrent.futures` for efficient multithreading
- Security research community for best practices
- Open source community for inspiration and feedback

## 📞 Contact

- **GitHub**: [@AkshayRane05](https://github.com/AkshayRane05)
- **Issues**: [Report bugs or request features](https://github.com/AkshayRane05/Port-Scanner/issues)

---

⭐ **If this tool helped you learn about network security, please star the repository!**

## 🔗 Related Projects

- [Network Scanner](https://github.com/AkshayRane05/Network-Scanner) - Comprehensive network discovery tool
- [Network Monitor](https://github.com/AkshayRane05/Outbound-Network-Monitor) - Real-time network monitoring
