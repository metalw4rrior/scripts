import re
from collections import Counter

# Путь к файлу журнала доступа
log_file_path = "access.log"
# Путь к файлу для записи IP-адресов
output_file_path = "filtered_ips.txt"

# Паттерн для поиска IP-адресов в строке
ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

# Создаем пустой счетчик IP-адресов
ip_counter = Counter()

# Читаем файл построчно и обрабатываем каждую строку
with open(log_file_path, 'r') as file:
    for line in file:
        # Проверяем, что строка содержит "403", не содержит "200" и не содержит адрес "85.15.145.66"
        if "403" in line and "200" not in line and "85.15.145.66" not in line:
            # Находим все IP-адреса в строке
            ips_in_line = re.findall(ip_pattern, line)
            # Обновляем счетчик IP-адресов
            ip_counter.update(ips_in_line)

# Сортируем IP адреса по убыванию количества повторений
sorted_ips = sorted(ip_counter.items(), key=lambda x: x[1], reverse=True)

# Записываем отсортированные IP адреса в отдельный файл
with open(output_file_path, 'w') as output_file:
    output_file.write("IP адреса и количество повторений (отсортированные по убыванию):\n")
    for ip, count in sorted_ips:
        output_file.write(f"{ip}: {count}\n")

print(f"Отсортированные IP адреса были записаны в файл: {output_file_path}")
