# ZenTao Vulnerability Scanner

ZenTao Vulnerability Scanner is an automated security tool designed to detect and report potential vulnerabilities in ZenTao systems. It reads URLs from a file, checks each for specific vulnerabilities, and logs successful exploits to a CSV file.

## Features

- **Automated Scanning**: Automatically reads a list of URLs from a file and performs vulnerability scans.
- **Concurrency**: Supports concurrent scanning to improve efficiency.
- **Detailed Reporting**: Generates a CSV file with detailed results for further analysis.
- **Extensibility**: The codebase is structured for easy modifications and enhancements.

## Installation

This tool is written in Python and depends on the `requests` library. Ensure you have Python 3.6 or higher installed on your system before you start.

```bash
# Clone the repository
git clone https://github.com/yourgithubusername/zentao-vulnerability-scanner.git
cd zentao-vulnerability-scanner

# Install required libraries
pip install -r requirements.txt
```

## Usage

1. Save your list of target URLs in a text file, one URL per line.
2. Run the scanner using the command:

```bash
python zentao_vuln_scanner.py -f path/to/your/urls.txt
```

## File Structure

- `zentao_vuln_scanner.py`: The main script containing all the scanning logic.
- `requirements.txt`: Lists all the Python libraries that the project depends on.
- `result.csv`: The scan results will be logged to this CSV file.

## Contributing

Contributions are welcome, whether they add new features, improve existing ones, or fix bugs. Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is intended for educational and research purposes only. Ensure you have the proper authorization before scanning or testing networks using this tool. The developer assumes no liability for any misuse of this tool.

---

© 2024 [Your Name] - All Rights Reserved.
