import socket
import socks
import requests
import re

# global variable define
ROOT_OF_WEB = "http://www.hentai2012.com"

# class define
class Book():

    def __init__(self):

        self.bookNumber = ""
        self.bookName = ""
        self.bookLabel = ""
        self.bookPagesNumber = 0

# main
def main():

    # socks5 proxy setting
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
    socket.socket = socks.socksocket

    file = open('result_manga.txt', 'a')

    #文件最后一个的序号
    number = 0

    #for page in range(1,3):
    for page in range(1, 1587 + 1):

        print("Page:" + str(page))

        # get web
        url = ROOT_OF_WEB + "/hentai_manga/page_" + str(page) + ".html"
        webResp = requests.get(url)

        # analyse
        # 抽离出折页的所有书
        regex = '<div class="col-md-3 resent-grid recommended-grid">[\n|\t]*(.*?)</ul>\n[\t]*</div>\n[\t]*</div>'
        BooksOfThePage = re.findall(regex,webResp.text,re.S)

        for i in range(0,len(BooksOfThePage)) :

            number = number + 1
            file.write("NUMBER:" + str(number) + "\n")
            file.write("CODIFICATION:" + re.search('<a href="/hentai_manga/(\d*)/" class="thumbnail">',BooksOfThePage[i]).group(1) + "\n")
            file.write("NAME:" + re.search('/" class="title">(.*)</a></h5>',BooksOfThePage[i]).group(1) + "\n")
            file.write("LABEL:" + re.search('<div class="time small-time">\n\t*<p>(.*)</p>',BooksOfThePage[i]).group(1) + "\n")
            file.write("PAGES:" + re.search('<li class="right-list"><p class="views views-info">(.*) 頁</p></li>',BooksOfThePage[i]).group(1) + "\n\n")

    file.close()

if __name__ == '__main__':

    main()
