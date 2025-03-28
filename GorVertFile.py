import os
from PIL import Image

def classify_images(input_path, output_vertical, output_horizontal):
    """
    Классифицирует изображения на вертикальные и горизонтальные, обходя вложенные папки.

    :param input_path: Путь к папке с папками и изображениями
    :param output_vertical: Папка для вертикальных изображений
    :param output_horizontal: Папка для горизонтальных изображений
    """
    # Создаем папки, если их нет
    os.makedirs(output_vertical, exist_ok=True)
    os.makedirs(output_horizontal, exist_ok=True)
    
    # Рекурсивно проходим по всем папкам и файлам
    for root, _, files in os.walk(input_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):
                process_image(file_path, output_vertical, output_horizontal)

def process_image(image_path, output_vertical, output_horizontal):
    """
    Обрабатывает одно изображение и классифицирует его.

    :param image_path: Путь к изображению
    :param output_vertical: Папка для вертикальных изображений
    :param output_horizontal: Папка для горизонтальных изображений
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            if height > width:
                target_folder = output_vertical
            else:
                target_folder = output_horizontal
            
            # Перемещаем изображение в соответствующую папку
            image_name = os.path.basename(image_path)
            target_path = os.path.join(target_folder, image_name)
            img.save(target_path)
            print(f"Изображение {image_name} сохранено в {target_folder}")
    except Exception as e:
        print(f"Ошибка обработки файла {image_path}: {e}")
# Пример использования
input_path = "C:/Users/konst/OneDrive/Рабочий стол/work image"  # Укажите путь к изображению или папке
output_vertical = "C:/Users/konst/OneDrive/Рабочий стол/work image/вертикальные"          # Папка для вертикальных изображений
output_horizontal = "C:/Users/konst/OneDrive/Рабочий стол/work image/альбомные подходящие"      # Папка для горизонтальных изображений

classify_images(input_path, output_vertical, output_horizontal)