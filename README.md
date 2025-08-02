# Parallel Username Enumerator with Progress Bar

This tool performs **username enumeration** on a target login page using a known password and a wordlist of usernames.  
It checks each username by analyzing the server's response, and reports valid usernames.

🧠 **Designed for:**
- CTFs (TryHackMe, HackTheBox, etc.)
- Pentesting login pages with username brute-force
- Speed + visibility (using multiprocessing and progress bar)

---

## 🚀 Features

- ✅ Uses `requests` for fast HTTP POST attempts
- ✅ Multi-core brute-forcing via `multiprocessing.Pool`
- ✅ Clean progress bar using `tqdm`
- ✅ Silent error handling and graceful exit

---

## 🔧 Requirements

Install the required modules:

```bash
pip install requests tqdm
