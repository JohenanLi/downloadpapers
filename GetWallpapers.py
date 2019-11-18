#coding : gb2312
"""
一、内容
爬取壁纸并保存到本地
目标网站：http://desk.zol.com.cn/dongman/
二、要求
1.爬取目标网站上 “动漫” 类别下所有的壁纸。
2.壁纸必须保存到脚本运行目录下的的 IMAGES文件夹内。
3.保存的图片必须以对应标题名和分辨率来命名，如：秋田君的小漫画 - 1920x1200.jpg。
4.图片分辨率应该是可选分辨率中最高的。
5.要有提示信息，格式：正在下载 (下载数量)：(图片名字)。
 如，在下载第 20张图片 秋田君的小漫画 时，提示应为：正在下载 20：秋田君的小漫画。
6.要有错误处理并给出相应提示，如：图片下载失败、网络超时的处理等。
7.变量命名要规范：使用驼峰命名或下划线命名，如：myCourseTable或 my_course_table。
8.不要出现无意义的命名，如：课表
 正确：course_table, school_timetable, timetable, schoolTimetable等。
 错误：t, kb, k，kebiao等。
9.必要的注释，但不可太多，尤其是不要行行都有注释。
10.代码缩进要整齐、清晰。
三、注意
1.IMAGES文件夹由脚本自动创建，没有就创建，否则不创建。
2.只需下载每组图片中的第一张即可。
3.图片必须是高分辨率大图，不能是网页中的缩略图。
4.请在 11月 11日前完成，并打包发送至邮箱：1604890072@qq.com
四、相关库
•requests：https://requests.kennethreitz.org/en/master/
•xpath语法：https://www.cnblogs.com/songshu120/p/5182043.html
•sys：https://www.cnblogs.com/mufenglin/p/7676160.html
"""
def getHtmlText(url):#获取指定url下的源代码
    try:#使用try excpet捕捉错误
        r = requests.get(url,timeout = 10)
        r.raise_for_status()
        r.encoding = 'gb2312'#已知网页编码为gb2312
        return r.text
    except:
        return "获取url源代码时失败"

def makeIndexDirs():#创建主目录
    try:
        if os.path.exists("D:\\壁纸") == False:
            os.mkdir("D:\\壁纸")
            os.chdir("D:\\壁纸")
        print("当前壁纸下载存于D:\\壁纸")
    except:
        return "创建主目录时失败"

def makePageDirs(id):#创建每页目录
    try:
        filepath ="D:\\壁纸\\"+str(id)
        if os.path.exists(filepath) == False:
            os.mkdir(filepath)
            print("创建了"+id+"文件夹")
    except:
        return "创建每页目录时失败"

def makeSonDirs(id,imgName):#创建子目录
    try:
        imgFile = "D:\\壁纸\\"+str(id)+imgName
        if os.path.exists() == False:
            os.mkdir(imgFile)
            print("创建了"+imgName+"文件夹")
    except:
        print("创建套图文件夹失败")
def main():
    makeIndexDirs()
    for id in range(1,2):
        html = "http://desk.zol.com.cn/dongman/"+str(id)+".html"
        makePageDirs(id)
        htmlText = getHtmlText(html)
        soup =BeautifulSoup(htmlText,'html.parser')
        all_img=soup.find('div',class_='main').find('li').find_all("a",attrs={'href':re.compile('^((?!http).)*$'),'target':'_blank'})
        print(all_img)
        for img in all_img:
            title=img['title']
            print("title")
import requests,os,re,lxml
from bs4 import BeautifulSoup
main()



    