def lovefunc( flower1, flower2):
    ''' Opposites Attract '''
    return ((flower1 - flower2) % 2 ) != 0

def score(dice):
    ''' Greed is Good '''
    score = int(dice.count(1)/3)*1000 + int(dice.count(6)/3)*600 + int(dice.count(5)/3)*500 + int(dice.count(4)/3)*400 + int(dice.count(3)/3)*300 + int(dice.count(2)/3)*200
    score = score + 100*(dice.count(1) % 3) + 50*(dice.count(5) % 3)
    return int(score)

def increment_string(strng):
    ''' String incrementer '''
    def replacestr(m):
        orglen=len(str(m.group(0)))
        rtnstr=str(int(m.group(0))+1)
        if( len(rtnstr) < orglen ):
            return '0'*(orglen-len(rtnstr))+rtnstr
        else:
            return rtnstr
    import re
    strngout=re.sub('([0-9]+)$', replacestr, strng)
    if strngout == strng:
        return strng+"1"
    else:
        return strngout

def increment_string2(strng):
    ''' String incrementer '''
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

def isPP(n):
    ''' What's a Perfect Power anyway? '''
    import math
    for i in range(2,n+1):
        for j in range(2,int(math.sqrt(n)),1):
            if ( i % j == 0):
                return [i,j]
    return None

def minNum(n):
    import math
    if n<=2: return n
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return i

def usdcny(usd):
    return "{0:.2f}".format(usd*6.75)+" Chinese Yuan"

def kata_13_december(lst): 
    for i in range(len(lst)-1,-1,-1):
        if lst[i]%2==0: 
            lst.pop(i)
    return lst

def isDigit(string):
    print(string)
    dspace = string.rstrip().lstrip()
    if dspace=='' or dspace == None: return False
    dint = dspace.isdigit()
    f = dspace.split('.')
    if dint:
        return True
    if len(f)<=2 and len(f)>=1:
        if f[0][0]=="-":
            f[0]=f[0][1:]
        for fi in f:
            if not fi.isdigit():
                return False
        return True
    return False

def isDigit2(string):
    try:
        float(string)
        return True
    except:
        return False

def sum_str(a, b):
    if a!="":
        if b!="":
            return int(a)+int(b)
        return int(a)
    if a=="":
        if b!="":
            return int(b)
        return 0

def sum_str(a, b):
    return str(int(a or 0)+int(b or 0))

def human_years_cat_years_dog_years(human_years):
    return [human_years,
            15+(human_years>0)*9+(human_years>1)*(human_years-2)*4,
            15+(human_years>0)*9+(human_years>1)*(human_years-2)*5]


def get_drink_by_profession(param):
    dictd={"Jabroni":"Patron Tequila",
           "School Counselor":"Anything with Alcohol",
           "Programmer":"Hipster Craft Beer",
           "Bike Gang Member":"Moonshine",
           "Politician":"Your tax dollars",
           "Rapper":"Cristal"}
    import string
    cdict=string.capwords(param)
    print(cdict)
    if cdict not in dictd.keys(): 
        return "Beer"
    else:
        return dictd[cdict]

def truthy(): 
  print("True")
  
def falsey(): 
  print("False")

def _if(bool, func1, func2):
    if bool:
        func1()
    else:
        func2()

def merge_arrays(first, second): 
    return list(set(first.extend(second)))


def HQ9(code):
    if code[0]=='H':
        return 'Hello World!'
    elif code[0]=='Q':
        return code
    elif code[0]=='9':
        outstr=""
        for i in range(99,2,-1):
            outstr+="{} bottles of beer on the wall, {} bottles of beer.\nTake one down and pass it around, {} bottles of beer on the wall.\n".format(i,i,i-1)
        outstr+="2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        return outstr


def round_it(n):
    from math import ceil
    dot=str(n).index('.')
    if dot<len(str(n))-dot-1:
        return ceil(n)
    if dot>len(str(n))-dot-1:
        return int(n)
    return round(n)

def cal(s, ops):
    t=True
    f=False
    cals=''
    for i in range(len(ops)):
        cals=cals+s[i]+ops[i]
    cals=cals+s[-1]
    print('cals=', cals)
    return eval(cals)

def solve(s,ops):
    if len(ops)==1:
        return cals(s,ops)
    pass
    return solve(s1, ops)+cal(s,ops)
