import requests, urllib.parse

url = 'https://notify-api.line.me/api/notify'
# token = '0JVZUXGetnFQV3CYZ0bZYpp1GAuE3MdJSVH9Tsm6ilR'
token = '9btZfWSP61xFB608ZyOrGOIGiLaDaJNLnXAVVsxA3JP'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}


# msg = 'Hello LINE Notify สวัสดีครับ'
Photourl = ('https://static.wikia.nocookie.net/marvelcinematicuniverse/images/b/b6/Amazing_Spider-Man_-_Profile_Pic.png')
stickerPackageId = "KAMEN RIDER SERIES 2016"
stickerId = 19

while(1):
    msg = input("Enter Msg : ")
    r = requests.post(url, headers=headers, data = {'message':msg})
    print (r.text)
    
# r = requests.post(url, headers=headers, data = {'message':msg})
# print (r.text)

    # r = requests.post(url, headers=headers, params = {'message':msg,
    #                                               'imageThumbnail': Photourl,
    #                                               'imageFullsize': Photourl,
    #                                               "stickerPackageId": stickerPackageId,
    #                                               "stickerId": stickerId}
    #                                                                         )
    
