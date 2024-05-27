
#!/bin/bash

# Путь к исходной папке с файлами
source_dir="/your/source/dir"

# Путь к целевой папке, куда будут перемещены переименованные файлы
target_dir="/your/target/dir"

# Создаем целевую папку, если она не существует
mkdir -p "$target_dir"

# Цикл по всем файлам в каталоге
for file in "$source_dir"/*; do
    # Извлекаем имя файла без пути
    filename=$(basename "$file")
    
    # Переименовываем файл, добавляя точку в конец
    new_filename="$filename."
    
    # Перемещаем переименованный файл в целевую папку
    mv "$file" "$target_dir/$new_filename"
done

