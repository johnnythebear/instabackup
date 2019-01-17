#!python3
#Tool for downloading photos and videos from instagram
from bs4 import BeautifulSoup
import requests, time, urllib.request, sys

class Content:
    def __init__(self, url):
        self.url = url
        self.req = requests.get(self.url, stream=True)
        self.soup = BeautifulSoup(self.req.content, "html.parser")

    def download(self, contentType):
        if contentType == "p":
            ogType = "image"
            fileStart = "img_"
            fileEnd = ".jpg"
        elif contentType == "v":
            ogType = "video"
            fileStart = "vid_"
            fileEnd = ".mp4"            
        photo_url = self.soup.find_all("meta", {"property": "og:"+ogType})
        for i in photo_url:
            content = i["content"]
            print("Downloading " +ogType+ "...")
            name = fileStart +str(time.time()) +fileEnd
            urllib.request.urlretrieve(url=content, filename=name)

class Main:
    def __init__(self):
        print("*"*36+"\nInstagram photo and video downloader\n"+"*"*36)
        contentType = input("Enter p for photo, v for video: ")
        if len(sys.argv) == 1:
            print("\nTip: you can download more photos or videos\n"\
            "put the links into a file and type:\n"\
            "insta_download.py [yourfile.txt]\n")
            url = input("Enter URL: ")
            obj = Content(url)
            obj.download(contentType)
        else:
            with open(sys.argv[1]) as f:
                for url in f:
                    obj = Content(url)
                    obj.download(contentType)

if __name__ == "__main__":
    Main()
