#import httplib, urllib
import ast
import json
import requests
responseMsg = ""
def WebClientApiCaller(host, path, jsonData): 
    params = urllib.urlencode(jsonData)
    #HTTP to bypass ssl
    conn = httplib.HTTPConnection(host) #establishing connection in entire function 
    conn.connect()
    conn.request("POST", path, params)
    response = conn.getresponse()

    responseMsg = response.read()
    #print response.status
    return responseMsg

def reverseString(str): 
    revStr = str[::-1] #reversing string using slicing 
    return "".join(revStr)
def excludePrefix(dictionary):
    finalList = []
    for value in dictionary["array"]:
        if(value[0:4] != dictionary["prefix"]):
            finalList.append(value)

    return finalList

path = "/api/prefix"
validPath = "/api/prefix/validate"
host = "challenge.code2040.org"
jsonData = {"token":"9e46e028f978939349e3fcd8d8a8c283"}

r = requests.post('http://challenge.code2040.org/api/prefix',jsonData) #using requests to post
print (r)
print (r.json())
myarray = excludePrefix(r.json())
print ('')

print (myarray)
payload =  {"token":"9e46e028f978939349e3fcd8d8a8c283","array":myarray}
print (payload)
headers = {'content-type':'application/json'}
j =requests.post('http://challenge.code2040.org/api/prefix/validate',data = json.dumps(payload),headers = headers)

print (j)
