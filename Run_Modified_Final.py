
try:
    import requests, re, json, time, random, string, os, datetime
    from requests_toolbelt.multipart.encoder import MultipartEncoder
    from rich.columns import Columns
    from rich.panel import Panel
    from rich.console import Console
    from rich import print as printf
    from requests.exceptions import RequestException
except (ModuleNotFoundError) as e:
    exit(f"[Error] {str(e).capitalize()}!")

LOOPING, TEXT, SUKSES, KOMENTAR, GAGAL, FOTO, POSTINGAN, LIKE = 0, {
    "TYPE": "DEFAULT"
}, [], {
    "STATUS": True
}, [], {
    "TYPE": "1"
}, [], {
    "STATUS": True
}

def PROMPT():
    return ([
        "1. Gambar pegunungan dengan matahari terbit di latar belakang.",
        "2. Hutan yang lebat dengan air terjun di tengahnya.",
        "3. Pantai berpasir putih dengan pohon kelapa yang menjulang tinggi.",
        "4. Danau tenang dengan pantulan langit biru.",
        "5. Lembah hijau dengan sungai yang mengalir di tengahnya."
    ])

def TAMPILKAN_BANNER():
    os.system('cls' if os.name == 'nt' else 'clear')
    printf(Panel(r'''[bold red]  _____ _           _  __                          
 |  ___| |__       | |/ /___  _ __ ___   ___ _ __  
 | |_  | '_ \ _____| ' // _ \| '_ ` _ \ / _ \ '_ \ 
 |  _| | |_) |_____| . \ (_) | | | | | |  __/ | | |
 |_|   |_.__/      |_|\_\___/|_| |_| |_|\___|_| |_|

[bold white]Facebook Comments Bot - Home Page Only''', width=57, style="bold light_slate_grey"))

def HEADERS(your_cookies):
    return({
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "{}".format(your_cookies),
        "dpr": "1.5",
        "Host": "m.facebook.com",
        "User-Agent": "Mozilla/5.0"
    })

class FACEBOOK:

    def __init__(self) -> None:
        pass

    def MENDAPATKAN_POSTINGAN_TERBARU(self, cookies):
        global POSTINGAN
        with requests.Session() as SESSION:
            SESSION.headers.update(
                HEADERS(your_cookies=cookies)
            )
            response = SESSION.get('https://m.facebook.com/home.php?hrc=1&paipv=0&eav=&_rdr')
            
            # Filter postingan hanya dari beranda
            self.FIND_POSTINGAN = re.findall(r'href="(/story\.php\?[^"]+)"', str(response.text))
            for POST in self.FIND_POSTINGAN:
                try:
                    self.FINAL_POSTINGAN = POST.replace('amp;', '')
                    if 'story_fbid=' in str(self.FINAL_POSTINGAN):
                        self.STORY_FBID = re.search(r'story_fbid=([^&]+)', str(self.FINAL_POSTINGAN)).group(1)
                        if str(self.STORY_FBID) not in str(POSTINGAN):
                            printf(f"Menambahkan Postingan: {str(self.STORY_FBID)}")
                            POSTINGAN.append(f'https://m.facebook.com{self.FINAL_POSTINGAN}')
                except:
                    continue
            return "Berhasil Mendapatkan Postingan Beranda"

# Anda dapat melanjutkan kode lainnya sesuai kebutuhan.
