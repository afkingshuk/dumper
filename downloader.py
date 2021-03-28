import urllib

baseURL = "https://img.yumpu.com/62710148/"
contentNumber = 1
contentResolution = "/5000x5000/"
contentName = "aima-3ed-solution-manual"
contentFormat = ".jpg"


for contentNumber in range(1,238):
    URL = baseURL + str(contentNumber) + contentResolution + contentName + contentFormat
    print("Trying to Download ... Number {} : Filename: {} from URL {} ".format(contentNumber, contentName+"-"+str(contentNumber)+contentFormat, URL))
    urllib.urlretrieve(URL, contentName+"-"+str(contentNumber)+contentFormat)
    print("Done ... Number {} : Filename: {} from URL {} ".format(contentNumber, contentName+"-"+str(contentNumber)+contentFormat, URL))


# https://img.yumpu.com/62710148/1/2400x2400/aima-3ed-solution-manual.jpg

#urllib.urlretrieve("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png", "local-filename.jpg")
