import urllib.request
import json
#print Results data----->function
def printResults(data):
    #loading string data into the dictionary
    theJson = json.loads(data)

    if "title" in theJson["metadata"]:
        print(theJson["metadata"]["title"])

    #output number of events    
    count = theJson["metadata"]["count"]
    print(str(count) + " events recorded")#past Hour

    #place where it occured 
    for i in theJson["features"]:
        print(i["properties"]["place"])
    print("---------------\n")       

    for i in theJson["features"]:
        if i["properties"]["mag"] > 4.0 :
         print("%2.1f" % i["properties"]["mag"],i["properties"]["place"])

    print("events that where felt:")
    for i in theJson["features"]:
         feltReports = i["properties"]["felt"]
         if feltReports != None:
                if feltReports > 0:
                    print("%2.1f" % i["properties"]["mag"],i["properties"]["place"],"reported" + str(feltReports)+"times")
def main():
    #data regarding the erthquake more than 2.5 mag.
    urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_hour.geojson"
    webUrl= urllib.request.urlopen(urlData)
    print("result code" + str(webUrl.getcode()) )
    
   # data = webUrl.read() # reading data file
    #print(data)#giving html code for google.
    if(webUrl.getcode()==200):
            data = webUrl.read()
            printResults(data)
    else:
        print("receive error cannot parse reuslts/data")        

if __name__ == '__main__':
        main()