import cv2
import dlib

# Инициализация детектора лиц
face_detector = dlib.get_frontal_face_detector()

# Инициализация распознавателя лиц
face_recognizer = dlib.face_recognition_model_v1("path/to/dlib/face_recognition_model.dat")

# Открытие камеры видеонаблюдения
cap = cv2.VideoCapture(0)

while True:
    # Захват кадра с камеры
    ret, frame = cap.read()

    # Обнаружение лиц на кадре
    faces = face_detector(frame, 1)

    # Для каждого обнаруженного лица
    for face in faces:
        # Получение координат лица
        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()

        # Извлечение дескриптора лица
        face_descriptor = face_recognizer.compute_face_descriptor(frame, face)

        # Отображение лица на кадре
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Отображение кадра
    cv2.imshow("Face Detection", frame)

    # Выход из программы по нажатию 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()