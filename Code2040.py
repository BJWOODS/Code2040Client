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
def needle(dictionary):
    for value in dictionary["haystack"]:
        if(value == dictionary["needle"]):
            return dictionary["haystack"].index(value) #found the needle!


path = "/api/haystack?token=9e46e028f978939349e3fcd8d8a8c283&github=github.com/BJWOODS/Code2040Client"
validPath = "/api/haystack/validate"
host = "challenge.code2040.org"
jsonData = {"token":"9e46e028f978939349e3fcd8d8a8c283", "github":"github.com/BJWOODS/Code2040Client"}
responseMsg = WebClientApiCaller(host,path,jsonData)
dictionary = ast.literal_eval(responseMsg) 
#print dictionary
#print responseMsg
pos = needle(dictionary)

print pos

jsonDataNew = {"token":"9e46e028f978939349e3fcd8d8a8c283","needle":json.dumps(pos)} #explicitly converting to json

WebClientApiCaller(host, validPath, jsonDataNew)