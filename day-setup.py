
from pathlib import Path
from functools import cache
import logging
import urllib3

import datetime, os, re
import requests
import pytz

from cryptography.hazmat.primitives.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers import modes

log = logging.getLogger(__name__)

config_dir = Path("~/.everybody.codes/").expanduser()
config_dir.mkdir(parents=True, exist_ok=True)


url_post = "https://everybody.codes/api/event/{event}/quest/{quest}/part/{part}/answer"

@cache
def get_token():
    path = config_dir / "token.txt"
    if not path.is_file():
        raise Exception(f"Your everybody-codes token is expected to be in {path}")
    return path.read_text(encoding='utf-16').split()[0]

@cache
def get_http():
    headers = {
        "User-Agent": "github.com/albertominetti/everybody-codes",
        "Cookie": f"everybody-codes={get_token()}",
    }

    http = urllib3.PoolManager(headers=headers)
    return http

@cache
def get_seed():
    path = config_dir / "seed.txt"
    if path.is_file():
        seed = int(path.read_text())
        log.debug("got seed %d from memo %s", seed, path)
    else:
        url_user = "https://everybody.codes/api/user/me"
        resp = get_http().request("GET", url_user)
        if resp.status != 200:
            raise Exception(f"HTTP {resp.status} from {url_user}")
        seed = resp.json()["seed"]
        path.write_text(str(seed))
        log.debug("wrote seed %d to memo %s", seed, path)
    return seed

print(get_token())
print(get_seed())

def get_enc_inputs(event, story, seed):
    http = get_http()
    url_data = "https://everybody-codes.b-cdn.net/assets/{event}/{story}/input/{seed}.json"
    url = url_data.format(event=event, story=story, seed=seed)
    resp = http.request("GET", url)
    if resp.status != 200:
        raise Exception(f"HTTP {resp.status} from {url}")
    data = resp.json()
    return data


def get_keys(event, quest):
    http = get_http()
    url_keys = "https://everybody.codes/api/event/{event}/quest/{quest}"
    url = url_keys.format(event=event, quest=quest)
    resp = http.request("GET", url)
    if resp.status != 200:
        raise Exception(f"HTTP {resp.status} from {url}")
    data = resp.json()
    if "key1" not in data:
        log.warning("unexpected response from %s:\n%s", url, data)
        raise Exception("failed to get keys")
    return data

def decrypt(input_hex, key):
    key_bytes = key.encode()
    iv = key_bytes[:16]
    cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv))
    decryptor = cipher.decryptor()
    input_bytes = bytes.fromhex(input_hex)
    decrypted_bytes = decryptor.update(input_bytes) + decryptor.finalize()
    pad_length = decrypted_bytes[-1]
    result = decrypted_bytes[:-pad_length].decode()
    return result




current_time = datetime.datetime.now(pytz.timezone('Europe/Zurich'))
print("Time is " + current_time.strftime("%Y-%m-%d %H:%M:%S"))
year = current_time.year
day = current_time.day - 1  # started on November Tuesday, the 4th


year_dir = Path(str(year))
year_dir.mkdir(parents=True, exist_ok=True)
day_dir = year_dir /"day-{:02d}".format(day)
day_dir.mkdir(parents=True, exist_ok=True)


day_code_dir = day_dir /"day-{:02d}.py".format(day)

if not day_code_dir.exists():
    day_code_dir.touch(exist_ok=True)

inputs = get_enc_inputs(year, day, get_seed())
keys = get_keys(year, day)
for i in [1,2,3]:
    key = f"key{i}"
    if key in keys:
        content = decrypt(inputs[str(i)], keys[key])
        test_path = day_dir / "test-input-{:02d}-{:02d}.txt".format(day, i)
        print(test_path)
        test_path.touch(exist_ok=True)
        test_path.write_text(content)

