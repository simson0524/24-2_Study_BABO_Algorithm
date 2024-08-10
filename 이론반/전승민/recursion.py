#백준 4779
def calc(n):
    if n == 1:
         return "-"
    bar = calc(n//3)
    last = bar+" "*(n//3)+bar
    return last
         

while True:
    try:
         n = int(input())
         print(calc(3**n))
    except:
         break

#백준 1182

count = 0
temp = []
def calc(k):
    # 내부쓸때 gloabl!!!!! 계속 까먹음;;;
    global count
    if len(temp)>0 and sum(temp) == S:
        count +=1
    for i in range(k,N):
        temp.append(arr[i])
        calc(i+1)
        temp.pop()
        


N,S = map(int,input().split())
arr = list(map(int,input().split()))
calc(0)
print(count)




# 백준 1759

L,C = map(int,input().split())
li = sorted(input().split())
#acistw
#L = 4
#C = 6
#li = ['a','c','i','s','t','w']
#조합시킨거 넣어야함
arr = []


def system(nowlen,pos):
    if nowlen == L:
        mo = 0
        ja = 0
        for k in arr:
            if k in 'aeiou':
                mo+=1
            else:
                ja +=1

        if mo >= 1 and ja >=2:
          # 출력할때 반복문 돌리지말고, 이렇게 햐는게 더 좋은듯
            print("".join(arr))
        return
    for i in range(pos,C):
        arr.append(li[i])
        system(nowlen+1,i+1)
        arr.pop()
            
system(0,0)
