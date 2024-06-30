# EasyKNN.py  
基于Python的简易易上手傻瓜式KNN分类模型。  
### 运行环境  
* Windows  
* Python 3.8及以上
```sh
pip install opencv-python
pip install numpy
pip install scikit-learn
pip install joblib
pip install selenium
pip install requests
pip install beautifulsoup4
```

## 使用教程   
### **第一步 获取训练数据**  
您可以从Pexels、Pixabay、Unsplash下载要识别图片的训练数据。  
当然，该仓库已包含了一个爬取百度图片作为训练数据的程序`getimage.py`。  
1. 浏览器访问image.baidu.com，然后搜索您要训练数据的关键词。  
2. 复制下搜索后的链接。  
3. 直接运行`getimage.py`，将复制的链接输入进去，然后设置要爬取的图片数量。  
4. 在程序运行结束后打开image文件夹，里面是刚刚爬取的所有图片。  


### **第二步 训练模型**  
将不同要识别的对象分为两个文件夹，然后移动到程序目录下。  
之后在当前目录下打开终端，执行：
```sh
py train.py <分类对象A文件夹名> <分类标签A> <分类对象B文件夹名> <分类标签B>
```
训练完成后会在当前目录下生成`model_combined.pkl`，这是训练结果文件。  


### **第三步 使用模型**  
打开`start.bat`，在弹出的文件资源管理器选择刚刚训练完成的pkl文件。  
之后再选择要分类的图片，程序将会使用训练结果文件的模型进行判断，并输出设置的分类标签。


## 使用示例  
现在我想要实现让程序判断图片上是猫还是狗。  
### **第一步 获取训练数据**  
获取猫的训练数据：  
1. 浏览器访问image.baidu.com，然后搜索“猫”，然后复制链接  
2. 直接运行`getimage.py`，将复制的链接输入进去，然后设置要爬取的图片数量  
3. 在程序运行结束后打开image文件夹，把里面的图片文件复制到程序同目录下的`cats`文件夹  

获取狗的训练数据：    
1. 浏览器访问image.baidu.com，然后搜索“狗”，然后复制链接  
2. 直接运行`getimage.py`，将复制的链接输入进去，然后设置要爬取的图片数量  
3. 在程序运行结束后打开image文件夹，把里面的图片文件复制到程序同目录下的`dogs`文件夹  

### **第二步 训练模型**  
刚刚已经把猫和狗的训练数据图片都给复制到程序同目录下了，因此只需要在程序目录下终端执行：
```sh
py train.py cats cat dogs dog
```
等待训练完成，获取`model_combined.pkl`训练结果文件。

### **第三步 使用模型**  
打开`start.bat`，在弹出的文件资源管理器选择刚刚训练完成的pkl文件。  
之后再选择要分类的图片（猫/狗），程序会根据你刚刚在终端下设置的标签进行输出。  
即：程序识别为`dogs`文件夹训练的数据，那么就输出`dog`，程序识别为`cats`文件夹训练的数据，那么就输出`cat`。  










