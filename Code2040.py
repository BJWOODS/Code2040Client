import httplib, urllib
import ast
import json
responseMsg = ""
def WebClientApiCaller(host, path, jsonData): 
    params = urllib.urlencode(jsonData)
    #HTTP to bypass ssl
    conn = httplib.HTTPConnection(host) #establishing connection
    conn.connect()
    conn.request("POST", path, params)
    response = conn.getresponse()

    responseMsg = response.read()
    print response.status
    return responseMsg

def reverseString(str): 
    revStr = str[::-1] #reversing string using slicing 
    return "".join(revStr)
def excludePrefix(dictionary):
    finalList = []
    for value in dictionary["array"]:
        if(value[0:4] != dictionary["prefix"]):
            finalList.append(value)

    print finalList
    return finalList
path = "/api/prefix"
validPath = "/api/prefix/validate"
host = "challenge.code2040.org"
jsonData = {"token":"9e46e028f978939349e3fcd8d8a8c283"}
responseMsg = WebClientApiCaller(host,path,jsonData)
dictionary = ast.literal_eval(responseMsg) #Converting string to dictionary
print dictionary["prefix"]
print dictionary

newArray = excludePrefix(dictionary)
print newArray
jsonDataNew = json.dumps({"token":"9e46e028f978939349e3fcd8d8a8c283", "array":newArray})
WebClientApiCaller(host,validPath,jsonDataNew)