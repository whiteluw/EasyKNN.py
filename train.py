import os
import cv2
import numpy as np
import joblib
from sklearn.neighbors import KNeighborsClassifier
import argparse

def load_images_from_folder(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            img = cv2.resize(img, (100, 100))
            images.append(img.flatten())
            labels.append(label)
    return images, labels

def main():
    parser = argparse.ArgumentParser(description='训练图片分类器')
    parser.add_argument('folders_and_labels', type=str, nargs='+', help='文件夹和标签的对，如：<文件夹A> 标签A <文件夹B> 标签B')
    args = parser.parse_args()

    if len(args.folders_and_labels) % 2 != 0:
        print("请输入成对的文件夹和标签。")
        return

    images = []
    labels = []

    for i in range(0, len(args.folders_and_labels), 2):
        folder = args.folders_and_labels[i]
        label = args.folders_and_labels[i + 1]
        folder_images, folder_labels = load_images_from_folder(folder, label)
        images.extend(folder_images)
        labels.extend(folder_labels)

    if len(images) < 3:
        print("图片数量太少，至少需要3张图片进行训练。")
        return

    images = np.array(images)
    labels = np.array(labels)

    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(images, labels)

    model_filename = 'model_combined.pkl'
    joblib.dump(knn, model_filename)
    print(f"模型已保存为 {model_filename}")

if __name__ == "__main__":
    print ("正在执行训练...")
    main()
