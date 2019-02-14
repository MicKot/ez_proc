import cv2
import albumentations as albu
import os


def open_gray(path):
    return cv2.imread(path, 0)


def open_rgb(path):
    return cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)


def resize_with_padding(image, new_shape, padding_color=(128, 128, 128), method=None):
    ih, iw = image.shape[:2]
    h, w = new_shape
    scale = min(w/iw, h/ih)
    nw = int(iw*scale)
    nh = int(ih*scale)
    delta_w = w - nw
    delta_h = h - nh
    if method == 'nn':
        method = cv2.INTER_NEAREST
    elif scale < 1:
        method = cv2.INTER_AREA
    else:
        method = cv2.INTER_LINEAR
    image = cv2.resize(image, (nw, nh), interpolation=method)
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=padding_color)
    return image