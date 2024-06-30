import os
import cv2
import numpy as np
import joblib
from tkinter import Tk, filedialog
from collections import Counter

def load_image(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"文件路径不存在：{filepath}")
    
    img = cv2.imdecode(np.fromfile(filepath, dtype=np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"无法读取图片文件：{filepath}")
    img = cv2.resize(img, (100, 100))
    return img.flatten()

def main():
    Tk().withdraw()
    model_files = filedialog.askopenfilenames(title='选择模型文件', filetypes=[('Pickle 文件', '*.pkl')])
    
    if not model_files:
        print("未选择任何模型文件。")
        return

    image_file = filedialog.askopenfilename(title='选择要分类的图片', filetypes=[('图片文件', '*.png;*.jpg;*.jpeg')])
    
    if not image_file:
        print("未选择任何图片文件。")
        return

    try:
        image = load_image(image_file)
        image = np.array(image).reshape(1, -1)
    except FileNotFoundError as e:
        print(e)
        return

    predictions = []
    for model_file in model_files:
        knn = joblib.load(model_file)
        label = knn.predict(image)
        predictions.append(label[0])
        print(f"模型 {model_file} 的预测结果：{label[0]}")

if __name__ == "__main__":
    main()
