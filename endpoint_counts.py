import re
from collections import Counter

# Путь к файлу логов Nginx
log_file_path = 'access.log'

# Путь к выходному файлу для записи результатов
output_file_path = 'endpoint_counts.txt'

# Регулярное выражение для извлечения эндпоинтов
log_pattern = re.compile(r'\"(?:GET|POST|PUT|DELETE|PATCH|HEAD) (.*?) HTTP')

# Счетчик для хранения количества повторений эндпоинтов
endpoint_counter = Counter()

# Чтение файла логов и извлечение эндпоинтов
with open(log_file_path, 'r') as log_file:
    for line in log_file:
        match = log_pattern.search(line)
        if match:
            endpoint = match.group(1)
            endpoint_counter[endpoint] += 1

# Запись результатов в выходной файл
with open(output_file_path, 'w') as output_file:
    for endpoint, count in endpoint_counter.most_common():
        output_file.write(f'{endpoint}: {count}\n')

print(f'Results have been written to {output_file_path}')

