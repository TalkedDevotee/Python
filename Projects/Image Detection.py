import cv2
import imutils

def detect_shape(img, cnt):
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    if len(approx) == 5:
        cv2.drawContours(img, [cnt], 0, 255, -1)
        return "pentagon"

    elif len(approx) == 3:
        cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)
        return "triangle"

    elif len(approx) == 4:  # если 4 прямых
        (x, y, w, h) = cv2.boundingRect(approx)  # получаем параметры
        ar = w / float(h)  # находим соотношение сторон

        if ar >= 0.95 and ar <= 1.05:
            cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
            return "square"  # если стороны почти равны, то это квадрат
        else:
            cv2.drawContours(img, [cnt], 0, (255, 255, 0), -1)
            return "rectangle"  # иначе прямоугольник

    elif len(approx) == 5:  # если шесть сторон
        cv2.drawContours(img, [cnt], 0, (255, 255, 100), -1)
        return "hexagon"  # то шестиугольник

    elif len(approx) == 5:  # если семь сторон
        cv2.drawContours(img, [cnt], 0, (255, 200, 0), -1)
        return "heptagon"  # то семиугольник

    elif len(approx) == 8:  # если восемь сторон
        cv2.drawContours(img, [cnt], 0, (255, 100, 0), -1)
        return "octagon"  # то восьмиугольник

    elif len(approx) == 10:  # если десять сторон
        cv2.drawContours(img, [cnt], 0, (100, 100, 100), -1)
        return "decaton"  # то десятиугольник

    else:
        cv2.drawContours(img, [cnt], 0, (0, 255, 255), -1)
        return "circle"

m = [] # массив окон с результатами
for i in range(3):
    if i == 0:
        image = cv2.imread('C:/1.jpg')
        m.append(image)

    elif i == 1:
        image = cv2.imread('C:/2.jpg')
        m.append(image)

    elif i == 2:
        image = cv2.imread('C:/3.jpg')
        m.append(image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 1)

    contours, h = cv2.findContours(thresh, 1, 2)

    resized = imutils.resize(cv2.bitwise_not(image), width=300)  # изменяем размер изображения
    ratio = image.shape[0] / resized.shape[0]  # находим соотношение сторон изображения

    thresh = cv2.threshold(cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY), 60, 255, cv2.THRESH_BINARY)[1]  # бинаризуем изображение

    # получаем контуры
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    print("Распознаны ", len(cnts), " фигур.")
    for c in cnts:
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)

        c = c.astype("float")
        c *= ratio
        c = c.astype("int")

        cv2.drawContours(image, [c], -1, (255, 0, 0), 2)  # рисуем найденный контур
        cv2.putText(image, detect_shape(image, c), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)  # рисуем название фигуры

cv2.imshow("Image 1", m[0])
cv2.imshow("Image 2", m[1])
cv2.imshow("Image 3", m[2])
cv2.waitKey(0)
cv2.destroyAllWindows()
