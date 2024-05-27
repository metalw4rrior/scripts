
import requests

# IP адреса для определения страны
ip_addresses = [
    'your_ip1', 'your_ip2'
]

# Функция для получения страны по IP-адресу
def get_country(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/country")
    if response.status_code == 200:
        return response.text.strip()
    else:
        return "Unknown"

# Получаем страну для каждого IP адреса
for ip in ip_addresses:
    country = get_country(ip)
    print(f"{ip}: {country}")

