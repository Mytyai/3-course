import cv2
import os

faceNet = cv2.dnn.readNet(
    "models/opencv_face_detector_uint8.pb",
    "models/opencv_face_detector.pbtxt"
)

genderNet = cv2.dnn.readNet(
    "models/gender_net.caffemodel",
    "models/gender_deploy.prototxt"
)

ageNet = cv2.dnn.readNet(
    "models/age_net.caffemodel",
    "models/age_deploy.prototxt"
)

GENDER_LIST = ['Male', 'Female']
AGE_LIST = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', 
            '(25-32)', '(38-43)', '(48-53)', '(60-100)']


def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300),
                                 [104, 117, 123], True, False)
    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * w)
            y1 = int(detections[0, 0, i, 4] * h)
            x2 = int(detections[0, 0, i, 5] * w)
            y2 = int(detections[0, 0, i, 6] * h)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2),
                          (0, 255, 0), 2)

    return frameOpencvDnn, faceBoxes


def predict_age_gender(frame, faceBoxes):
    for box in faceBoxes:
        face = frame[max(0, box[1]):min(box[3], frame.shape[0] - 1),
                     max(0, box[0]):min(box[2], frame.shape[1] - 1)]

        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227),
                                     [104, 117, 123], swapRB=False)

        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = GENDER_LIST[genderPreds[0].argmax()]

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = AGE_LIST[agePreds[0].argmax()]

        label = f"{gender}, {age}"
        cv2.putText(frame, label, (box[0], box[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    return frame


def process_image(path):
    frame = cv2.imread(path)
    if frame is None:
        raise FileNotFoundError(f"Изображение не найдено: {path}")

    result, faceBoxes = highlightFace(faceNet, frame)
    result = predict_age_gender(result, faceBoxes)
    return result


def process_camera():
    cap = cv2.VideoCapture(0)
    print("Нажмите ESC для выхода.")
    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            break
        result, faceBoxes = highlightFace(faceNet, frame)
        result = predict_age_gender(result, faceBoxes)
        cv2.imshow("Результат с камеры", result)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


print("Выберите режим работы:")
print("1 - Обработка изображения из файла (из папки input_images/)")
print("2 - Обработка видео с камеры")
choice = input("Введите 1 или 2: ")

if choice == '1':
    filename = input("Введите имя файла (например, img.jpg): ")
    input_path = os.path.join("input_images", filename)
    output_path = os.path.join("output_images", filename)

    try:
        result = process_image(input_path)
        cv2.imshow("Результат", result)
        cv2.imwrite(output_path, result)
        print(f"Изображение сохранено: {output_path}")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(f"Ошибка: {e}")

elif choice == '2':
    process_camera()
else:
    print("Неверный выбор.")
    