# Python Tools

Small collection of Python scripts for practical offensive security / penetration testing practice.  
Currently focused on lightweight port scanning and basic API fuzzing.

## Contents

- `cozyscan.py`  
  Simple TCP port scanner that checks one target for open ports using TCP connect attempts.

- `api_fuzzer.py`  
  Basic HTTP/API fuzzer that can send multiple requests with different payloads/parameters to discover interesting responses.

- `multiscan.py`
  Multithreaded TCP port scanner that checks one target for open ports using TCP connect attempts.

More tools may be added over time as the project grows.

## Requirements

- Python 3.10+ (recommended)
- OS: Linux, macOS, or Windows

Optional Python packages (mainly for `api_fuzzer.py`):

- `requests`

Install dependencies (if needed):

```bash
pip install -r requirements.txt
