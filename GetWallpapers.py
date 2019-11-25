def getHtmlText(url):#获取指定url下的源代码
    try:#使用try excpet捕捉错误
        r = requests.get(url,timeout = 10)#超过10s返回错误代码
        r.raise_for_status()
        r.encoding = 'gb2312'#已知网页编码为gb2312
        return r.text
    except:
        return "获取url源代码时失败"

def makeIndexDirs():#创建主目录，并判断是否成功
    try:
        if os.path.exists("D:\\IMAGES") == False:
            os.mkdir("D:\\IMAGES")
            os.chdir("D:\\IMAGES")
        print("当前壁纸下载存于D:\\IMAGES")
    except:
        return "创建主目录时失败"

def makePageDirs(id):#创建每页目录，并判断是否成功
    try:
        filepath ="D:\\IMAGES\\"+str(id)
        if os.path.exists(filepath) == False:
            os.mkdir(filepath)
            print("创建了"+id+"文件夹")
    except:
        return "创建每页目录时失败"

def makeSonDirs(id,imgName):#创建子目录，并判断是否成功
    try:
        imgFile = "D:\\IMAGES\\"+str(id)+"\\"+imgName
        if os.path.exists(imgFile) == False:
            os.mkdir(imgFile)
            print("创建了"+imgName+"文件夹")
        return imgFile
    except:
        print("创建套图文件夹失败")
def main():
    makeIndexDirs()
    for id in range(1,34):#偷懒，因为发现动漫类目下面只有33页
        html = "http://desk.zol.com.cn/dongman/"+str(id)+".html"
        makePageDirs(id)#创建每个id网页文件夹
        htmlText = getHtmlText(html)#调用函数获取源码
        soup =BeautifulSoup(htmlText,'html.parser')
        all_ImgTitle=soup.find('ul',class_='pic-list2').find_all("img")#使用bs4获取所有img tag
        titleList = []
        hrefList = []
        imgFileList = []#建立三个list变量，之后用于储存和传递
        for imgTitle in all_ImgTitle:#利用bs得到title并存于数组中
            title = imgTitle['title']
            titleList.append(title)
            imgFile = makeSonDirs(id,title)
            imgFileList.append(imgFile)
        all_ImgHref=soup.find('ul',class_='pic-list2').find_all("a",class_="pic",attrs={'href':re.compile('^((?!http).)*$'),'target':'_blank'})
        for imgHref in all_ImgHref:#通过观察源码，利用代码进行多次筛选得到href
            href = imgHref['href']
            hrefList.append(href)
        pageInAndDownload(hrefList,titleList,imgFileList)#调用函数传递列表，类c语言指针

def pageInAndDownload(hrefList=[],titleList=[],imgFileList=[]):#进入具体页面并下载
    DetailHrefList = []
    ResolutionRatioList = []
    for i in range(len(hrefList)):#进入二级页面得到具体href
        DetailImgHref = "http://desk.zol.com.cn/"+hrefList[i]
        DetailImgText = getHtmlText(DetailImgHref)
        DetailSoup = BeautifulSoup(DetailImgText,"html.parser")
        DetailHref = DetailSoup.find('div',class_="wrapper mt15").find('dd',id='tagfbl').find('a',target="_blank")
        
        if "class" in str(DetailHref):#发现有几张特殊图片无法得到链接，原因在于缺少分辨率，因此直接转化为img的src
            WrongTurnHref = DetailSoup.find('div',class_='photo').find('img')
            DetailHrefList.append(WrongTurnHref['src'])
        else:
            DetailHrefList.append('http://desk.zol.com.cn'+DetailHref['href'])
    for m in range(len(DetailHrefList)):#进入三级页面得到剩余img的src
        if 'showpic' in DetailHrefList[m]:
            DeDetailImgText = getHtmlText(DetailHrefList[m])
            DeDetailSoup = BeautifulSoup(DeDetailImgText,"html.parser")
            DetailHrefList[m] = DeDetailSoup.img['src']
        ResolutionRatioList.append(re.findall(r"t_s(.+?)c5",DetailHrefList[m]))#观察发现它们的分辨率都在这两个字符串中间，利用正则表达式
    for j in range(len(DetailHrefList)):#利用python的存储文件方式存储，使用requests库的get得到content，给出相应的提示信息
        imgUrl = DetailHrefList[j]
        root = imgFileList[j]
        fileName = str(titleList[j])+str(ResolutionRatioList[j])+".jpg"
        path = root+"\\"+fileName
        try:
            GetRequest = requests.get(imgUrl)
            with open (path,'wb') as f:
                print("正在下载"+path)
                f.write(GetRequest.content)
                f.close()
                print(path + "保存成功")
        except:
            print("文件爬取失败,源文件可能有问题")
import requests,os,re,lxml,webbrowser
from bs4 import BeautifulSoup
main()
print("下载完毕")
print("增加套图下载")


    