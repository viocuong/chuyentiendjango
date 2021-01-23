from django import template
register = template.Library()

def parseMoney(value):
    moneyS = str(value)
    res = ""
    cnt = 0
    for i in reversed(range(len(moneyS))):
        res+=moneyS[i]
        cnt+=1
        if cnt == 3:
            res+=","
            cnt = 0
    return res[::-1]
register.filter('parseMoney',parseMoney)
