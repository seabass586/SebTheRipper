# SebTheRipper  
A **multi-threaded** password cracking tool that checks how easy it is to guess a password using a **wordlist-based brute-force attack**.  

## Features  
**Multi-threaded** for fast brute force  
**SHA-256 hashing** for security  
**Memory-efficient** – processes wordlist line-by-line  
**Custom & default wordlist support**  
**Execution time tracking**  

---

## Installation & Setup  

### Clone the Repository**  
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/SebTheRipper.git
cd SebTheRipper
```

### Install Required Dependencies**  
Ensure Python 3 is installed, then run:  
```sh
pip install -r requirements.txt
```
_(If `requests` is missing, install manually with: `pip install requests`)_

### Run the Script**  
```sh
python ripper.py
```

---

## Usage  

### **Basic Run**  
```sh
python ripper.py
```
- Enter a password to test  
- The script will hash and compare it against a **wordlist of common passwords**  
- If found, it warns you to change your password  

### **Example Run**
```
Enter a password to test its strength:
123456

[*] Fetching wordlist...
[*] Starting brute-force attack with 10 threads...

Password cracked: 123456
Change it immediately!

Execution Time: 2.45 seconds
```

### **Using a Custom Wordlist**  
You can provide a custom wordlist URL instead of the default:
```
[*] Press Enter to use the default wordlist or enter a custom wordlist URL:
https://example.com/my-wordlist.txt
```

---

## License  
This project is for **educational purposes only**. Do not use this tool for malicious activities.  

---

## Contributing  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature-name`)  
3. Commit your changes (`git commit -m "Added new feature"`)  
4. Push to your branch (`git push origin feature-name`)  
5. Open a pull request   

---

## Disclaimer  
SebTheRipper is intended **for security research and education**. Unauthorized use against systems you don’t own is illegal. **Use responsibly.**  

---

### Author  
**SebTheRipper** – A tool inspired by the need for better password security awareness!  

