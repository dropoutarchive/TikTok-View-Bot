import os
import uuid
import yaml
import ctypes
import requests
from time import time
from random import choice
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor

os.system("cls")

class Log:

    def __init__(self):
        self.colours = {
            "reset": "\x1b[0m",
            "success": "\x1b[38;5;10m",
            "info": "\x1b[38;5;45m",
            "warn": "\x1b[38;5;11m",
            "error": "\x1b[38;5;9m"
        }

    def success(self, text: str):
        print("\x1b[0m \x1b[38;5;10mSUCCESS\x1b[0m | \x1b[38;5;10m%s" % (text))

    def info(self, text: str):
        print("\x1b[0m \x1b[38;5;45mINFO\x1b[0m | \x1b[38;5;45m%s" % (text))

    def warn(self, text: str):
        print("\x1b[0m \x1b[38;5;11mWARNING\x1b[0m | \x1b[38;5;11m%s" % (text))

    def error(self, text: str):
        print("\x1b[0m \x1b[38;5;9mERROR\x1b[0m | \x1b[38;5;9m%s" % (text))

class TikTok():

    def __init__(self):
        ctypes.windll.kernel32.SetConsoleTitleW("[TikTok View Bot] - Menu")
        self.logging = Log()

        with open("config.yml") as f:
            self.config = yaml.safe_load(f.read())

        with open("proxies.txt", encoding="utf-8") as f:
            self.proxies = [i.strip() for i in f]

        self.proxy = cycle(self.proxies)

        self.attempts = 0
        self.failed = 0

    def title_task(self):
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW("[TikTok View Bot] - Added Views (%s/%s)" % (self.attempts, (self.failed + self.attempts)))

    def get_session(self):
        install_id = "".join(choice("0123456789") for _ in range(19))

        session = requests.Session()

        session.proxies.update({
            "https": "%s://%s" % (self.config["proxy"]["type"], next(self.proxy))
        })

        session.headers.update({
            "accept-encoding": "gzip",
            "connection": "Keep-Alive",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "store-idc=maliva; store-country-code=nz; install_id=%s; ttreq=1$89458cf82d59e549ee892788022a7277cc0b959b; odin_tt=2447ae7a071218c33439ea84e060b4634974a0964332a7ba65e2331730f2218ac931d4ecb26dc10c517dc3bfb70fddaa5893ea28d4e8fc885c98a982d4618ca12113728ca79908e27cbe96bf39aa095b; msToken=UIgk_teoJf0cCB2NVSA_NCsJYppJDLKUHLf03YZ7PjrMqWZk9wFumLgOJlJs2-MUpA6Eno4PCCpK6R0DSB4TLtBQXF8dgjNYAWrO-qVHoug=" % (install_id),
            "host": "api19-core-c-alisg.tiktokv.com",
            "passport-sdk-version": "19",
            "sdk-version": "2",
            "user-agent": "com.zhiliaoapp.musically/2022305030 (Linux; U; Android 7.1.2; en; A5010; Build/N2G48H;tt-ok/3.10.0.2)",
            "x-argus": "kwzCxTxZbmMbSGCBd2GjQhon5qurvrs/ZVALl4w1HNs/d/ZPaDpqnP2eM2Z6K99/29uvPG5rlSyMGAYsYnzrF6yPZzoXs1PUbKYki3m8yQZAgX43KgJKEzlz/0tcN6nY3Bbg3r/VjBmUCPnQ7hRKhfv/yn6NMb36FL+nnE8CGIq2f/6BOm6ShtLRZpIXGv5OfN6lB2bJGnwcaaE7mvnyKxPxagJ6+nBhnXzwVFgaHhHygUJxD23hjhh8BVjjm5TJhl472afw6s2wuQR46atiMDJgBZdhI6vN57D3PDAe6Rcyng==",
            "x-gorgon": "040420f54000a93c491e5e37e7da680b3fadf4de0a1eb8738d02",
            "x-khronos": str(int(time())),
            "x-ladon": "jTRwDv3OaObvRQgVXTMvjkFeuwMtzyHDcUEcKe7fuCVWEQGP",
            "x-ss-req-ticket": str(int(time())),
            "x-ss-stub": "2E27DA79FFB13349A0B10EB986EE8805",
            "x-tt-dm-status": "login=0;ct=1;rt=6",
            "x-tt-store-region": "nz",
            "x-tt-store-region-src": "did",
            "x-vc-bdturing-sdk-version": "2.2.1.i18n"
        })

        return session

    def view(self):
        session = self.get_session()

        data = {
            "order": "",
            "first_install_time": -1,
            "request_id": "",
            "is_ad": "0",
            "follow_status": 0,
            "tab_type": 3,
            "aweme_type": 0,
            "item_id": int(self.video),
            "sync_origin": False,
            "pre_item_playtime": 1288,
            "follower_status": 0,
            "pre_hot_sentence": "",
            "play_delta": 1,
            "pre_item_id": int(self.video),
            "action_time": int(time()),
            "enter_from": "others_homepage"
        }

        params = {
            "iid": "7074009544619394821",
            "device_id": "".join(choice("0123456789") for _ in range(19)),
            "ac": "wifi",
            "channel": "googleplay",
            "aid": "1233",
            "app_name": "musical_ly",
            "version_code": "230503",
            "version_name": "23.5.3",
            "device_platform": "android",
            "ab_version": "23.5.3",
            "ssmix": "a",
            "device_type": "A5010",
            "device_brand": "OnePlus",
            "language": "en",
            "os_api": "25",
            "os_version": "7.1.2",
            "openudid": "06fd8ebe15af027f",
            "manifest_version_code": "2022305030",
            "resolution": "900*1600",
            "dpi": "300",
            "update_version_code": "2022305030",
            "_rticket": int(time()) - 3045,
            "current_region": "NZ",
            "app_type": "normal",
            "sys_region": "US",
            "mcc_mnc": "53003",
            "timezone_name": "America/Chicago",
            "residence": "NZ",
            "ts": int(time()),
            "timezone_offset": "-21600",
            "build_number": "23.5.3",
            "region": "US",
            "uoo": "0",
            "app_language": "en",
            "carrier_region": "NZ",
            "locale": "en",
            "op_region": "NZ",
            "ac2": "wifi",
            "host_abi": "x86",
            "cdid": str(uuid.uuid4())
        }

        try:
            response = session.post("https://api19-core-c-alisg.tiktokv.com/aweme/v1/aweme/stats/", data=data, params=params)
        except Exception:
            self.failed += 1
            return

        if response.status_code == 200:
            if response.text != "":
                impr_id = response.json()["log_pb"]["impr_id"]
                self.logging.success("Added view %s(%s%s%s)" % (self.logging.colours["reset"], self.logging.colours["success"], impr_id, self.logging.colours["reset"]))
                self.attempts += 1
                return

        self.failed += 1

    def run(self):
        self.video = input("\x1b[0m \x1b[38;5;11mVIDEO\x1b[0m | \x1b[38;5;11mhttps://www.tiktok.com/@user/video/\x1b[0m")
        os.system("cls")
        with ThreadPoolExecutor(max_workers=10_000) as self.executor:
            self.executor.submit(self.title_task)
            while True:
                self.executor.submit(self.view)

if __name__ == "__main__":
    client = TikTok()
    client.run()