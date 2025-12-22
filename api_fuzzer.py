
import requests
import sys
import argparse


#------------Parser-------------
parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url",
                    required=True,
                    help="URL with FUZZ-Keyword:http:apiweb/FUZZ")


parser.add_argument("-w", "--wordlist",
                    required=True,
                    help="Path to wordlist: /home/user/wordlist/wordlist.txt")


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

print(f"[+] URL: {args.url}")
print(f"[+] Wordlist: {args.wordlist}")

target_url = args.url
wordlist = args.wordlist

#----------End Parser-------------




def wordlist_load(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
          print(f"File not found in: {path}")
          sys.exit(1)


file = wordlist_load(wordlist)




if "FUZZ" not in target_url.upper():
    print(f"[-] ERROR: FUZZ must be in the URL")
    sys.exit(1)

start_pos = target_url.upper().index("FUZZ")
prefix = target_url[:start_pos]
suffix = target_url[start_pos+4:]



stat_code = [200, 301, 402]


for endpoints in file:
    final_url = prefix + endpoints + suffix
    try:
        res = requests.get(final_url, timeout=7)
        if res.status_code in stat_code:
            print(f"[+] API FOUND!: {endpoints} -------| {final_url}")
    except requests.exceptions.RequestException:
         pass
    except KeyboardInterrupt:
         print("\n[!] Interrupted")
         sys.exit(0)
              
