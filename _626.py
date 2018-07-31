from math import floor, ceil
n=int(input(''))
for x in range(0,n):
    fighters,cookies=input('').split(" ")
    fighters=int(fighters)
    cookies=int(cookies)
    boxes=0
    for y in range(0,fighters):
        all_cookies=floor(24*3600/int(input('')))
        boxes+=all_cookies/cookies
    print(ceil(boxes))
    
