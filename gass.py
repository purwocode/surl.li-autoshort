import requests

# Input URL dari pengguna hanya sekali
link = input("Masukin Link: ")

# Input jumlah looping dari pengguna
loop_count = int(input("Mau buat berapa short? : "))

url = "https://app.surl.li/cutUrl"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,id;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://app.surl.li",
    "referer": "https://app.surl.li/en/url/create",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-csrf-token": "0ZWKzEkNn3c0z5TLCH0P5Rqfb9r4IZspvgHaVHGm",  # <- Ganti jika expired
    "x-requested-with": "XMLHttpRequest",
    "cookie": "_clck=1amfclx%7C2%7Cfv7%7C0%7C1935; _clsk=1nj2oql%7C1745106785161%7C29%7C1%7Cb.clarity.ms%2Fcollect; XSRF-TOKEN=eyJpdiI6IjA2azFCNGkyUmJucVg0RUQrc01zaUE9PSIsInZhbHVlIjoia3hwZjEwWVVxOTVhTXpaM2Z1cEZIcVpFdHdrcm9QYmV6WEpGMWZveG9zanl2OHNOZHJSaVRIeXdnRzgvZ2J5V3BiOGZGZFg5U3E0b2hvbjR3U2ZqbVYvZlp6QWJXOTlmcVJmeXpuam9mQmpkSGFqUk95STdNZHFPaHUxc2Q0NUwiLCJtYWMiOiI4M2IyMGE5MGQ4ZmRiMTdhNzRiNWE3NjQ0MWJhNDkzNDdlN2RlZWEzMjRiNDViMDRmMzU4ZjlhZDM5OGE2YjAwIiwidGFnIjoiIn0%3D; surli_session=eyJpdiI6InBpRHptQkRtdjYrK01tTDZuc3YzMFE9PSIsInZhbHVlIjoiKzZJV2FxV0VVZ0NteWZLei9XRlBpU1UzWnNaRFVLRk4vS2lYS1BIQjB1RjBCaHY3OGQ3VUwyK2NWSW4yRnpEcGVzMFJQK3lIRlpQait0WnJ0UGtoLys2di9xeEhKeDliaEJEZ1lYU25UTDRzbFQ5R1cwSFdQckNxS1FGWUFRc3UiLCJtYWMiOiJjMWJhMzJjNzI3NzM0OTNlYmQxNDBlMDgzMGMxZjBlZTQyNWQ1ZThmYmQyOTNiMGY5Mzg5M2QwNjMyNGUyOTAzIiwidGFnIjoiIn0%3D"  # <- Ganti dengan cookie lengkap
}

data = {
    "url": link,
    "domain_id": "1",
    "url_alias": "",
    "url_title": ""
}

# Buka file hasil.txt dalam mode append
with open('hasil.txt', 'a') as file:
    # Loop sesuai dengan jumlah yang diinginkan
    for i in range(loop_count):
        response = requests.post(url, headers=headers, data=data)

        # Cek dan simpan hasil
        if response.status_code == 200:
            result = response.json()
            if result.get("result"):
                short_url = result.get('short_url', '')
                print(f"Short URL {i + 1}: {short_url}")
                # Simpan hasil ke file dengan format yang diinginkan
                file.write(f"'{short_url}',\n")
            else:
                print(f"Link gagal dipendekkan pada iterasi {i + 1}.")
                file.write(f"Link gagal dipendekkan pada iterasi {i + 1}.\n")
        else:
            print(f"Request error pada iterasi {i + 1}: {response.text}")
            file.write(f"Request error pada iterasi {i + 1}: {response.text}\n")
