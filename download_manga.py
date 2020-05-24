import socket
import socks
import os
import requests
import re
from urllib.request import urlretrieve

# global variable define
DOWNLOAD_LOCATION = "/home/wngg/PycharmProjects/testProject"
ROOT_OF_WEB = "http://www.hentai2012.com"
TYPT_OF_BOOK = "hentai_manga"
#TYPT_OF_BOOK = "hentai_doujin"

def main():

    # socks5 proxy setting
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket

    # download
    fileName = "result_manga.txt"
    #fileName = "result_doujin.txt"
    file = open(fileName)

    while True:

        if not file.readline() :

            break

        cadification = file.readline()[13:-1]
        file.readline()
        file.readline()
        numberOfPages = file.readline()[6:-1]
        file.readline()
        downloadBook(TYPT_OF_BOOK,cadification,numberOfPages)

    file.close()

def downloadBook(typeOfBook,cadification,numberOfPages) :

    #提示
    print("Download : " + cadification)

    #检测是否已经下载了
    if os.path.exists(DOWNLOAD_LOCATION + "/" + cadification) :

        if os.path.exists(DOWNLOAD_LOCATION + "/" + cadification + "/" + "%03d" %int(numberOfPages) + ".jpg") :

            return

    else :

        os.makedirs(DOWNLOAD_LOCATION + "/" + cadification)

    #获取下载链接
    urlOfDownload = re.search('class="thumbnail"><img src="(.*)/\d*.jpg" alt=""></a>', requests.get(ROOT_OF_WEB + "/" + typeOfBook + "/" + cadification).text).group(1)

    for i in range(1,int(numberOfPages) + 1) :

        urlretrieve(ROOT_OF_WEB + urlOfDownload + "/" + "%03d" %i + ".jpg" , DOWNLOAD_LOCATION + "/" + cadification + "/" + "%03d" %i + ".jpg")




if __name__ == '__main__':

    main()