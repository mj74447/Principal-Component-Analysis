import urllib.request

def main():
    webUrl= urllib.request.urlopen("http://www.google.com")
    print("result code" + str(webUrl.getcode()) )
    
    data = webUrl.read() # reading data file
    print(data)#giving html code for google.
if __name__ == '__main__':
        main()