def sublistByNum(ls, result, num):
    while(len(ls) > 0):
        if(len(ls) == num):
            result.append(ls)
        sub = ls[:num]
        sub.sort(key=lambda i: i["rating"], reverse=True)
        result.append(sub)
        nextsub = ls[num:]
        return sublistByNum(nextsub, result, num)
    return result


from datetime import datetime
# https://www.w3schools.com/python/python_datetime.asp
now = datetime.now()
# Turn obj to str
nowStr = now.strftime("%Y%m%d-%H-%M-%S")
# Turn str to obj
nowObject = datetime.strptime(nowStr, "%Y%m%d-%H-%M-%S")
