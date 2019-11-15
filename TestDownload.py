import requests
import os
url = "https://desk-fd.zol-img.com.cn/t_s960x600c5/g2/M00/05/04/ChMlWV3BOhKIHYbqAAG88I_lzlYAANKiwGrLh4AAb0I144.jpg"
root = "D://pics//"
filename =  url.split("/")[-1]
path = root + filename
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        print("无文件")
        GetRequest = requests.get(url)
        with open (path,'wb') as f:
            f.write(GetRequest.content)
            f.close()
            print(filename + "保存成功")
    #else:
       #print("文件已经存在")
except:
    print("文件爬取失败")

