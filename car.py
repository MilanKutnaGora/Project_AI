import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recognize_license_plate(image_path):
    # Загружаем изображение
    image = cv2.imread(image_path)

    # Преобразуем изображение в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применяем адаптивную пороговую обработку для выделения номерного знака
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # Находим контуры на изображении
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Перебираем контуры и ищем наиболее вероятный номерной знак
    for cnt in contours:
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # Вычисляем ширину и высоту прямоугольника
        width, height = rect[1]

        # Проверяем, что размеры прямоугольника соответствуют размерам номерного знака
        if 80 < width < 200 and 20 < height < 40:
            # Извлекаем номерной знак из изображения
            roi = cv2.getRectSubPix(gray, (int(width), int(height)), tuple(map(int, rect[0])))

            # Распознаем текст на номерном знаке с помощью Tesseract OCR
            license_plate = pytesseract.image_to_string(roi, lang='eng')
            license_plate = ''.join(c for c in license_plate if c.isalnum())

            return license_plate

    return None

license_plate = recognize_license_plate('path/to/image.jpg')
if license_plate:
    print(f'Номерной знак: {license_plate}')
else:
    print('Не удалось распознать номерной знак')