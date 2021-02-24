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
