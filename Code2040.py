import httplib, urllib
responseMsg = ""
def WebClientApiCaller(host, path, jsonData): 
    params = urllib.urlencode(jsonData)
    #HTTP to bypass ssl
    conn = httplib.HTTPConnection(host) #establishing connection
    conn.connect()
    conn.request("POST", path, params)
    response = conn.getresponse()

    responseMsg = list(response.read())
    print response.status
    return responseMsg


def reverseString(str): 
    revStr = str[::-1] #reversing string using slicing 
    return "".join(revStr)

path = "/api/reverse?token=9e46e028f978939349e3fcd8d8a8c283&github=github.com/BJWOODS/Code2040Client"
validPath = "/api/reverse/validate?token=9e46e028f978939349e3fcd8d8a8c283&github=github.com/BJWOODS/Code2040Client"
host = "challenge.code2040.org"
jsonData = {"token":"9e46e028f978939349e3fcd8d8a8c283", "github":"github.com/BJWOODS/Code2040Client"}
responseMsg = WebClientApiCaller(host,path,jsonData)

#print reverseString(responseMsg)
jsonDataNew = {"token":"9e46e028f978939349e3fcd8d8a8c283","string":reverseString(responseMsg)}

WebClientApiCaller(host, validPath, jsonDataNew)
