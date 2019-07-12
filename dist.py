from geopy import distance
from decimal import Decimal

from geopy import Nominatim

print ("|￣￣￣￣￣￣￣￣￣￣￣|")
print ("|  WELCOME TO       |")
print ("|  DISTANCEBOT      |")
print ("|___________________|")
print ("  (\__/)|| ")
print ("  (•ㅅ•)|| ")
print ("  / 　 づ  ")
X = 0
while (X < 5):
    d = distance.distance
    g = Nominatim(user_agent="DistanceBot")
    x = input("Enter location: ")
    y = input("Enter another location: ")
    _, wa = g.geocode(x)
    _, pa = g.geocode(y)
    m = d(wa, pa).miles
    n = round (m,2)
    print("The distance between " , x," and ",y," is " ,n, "miles")
    X =+ 1
    
    print ("＼＼ ＿")
    print ("　　 ＼(　•_•) F")
    print ("　　　 <　⌒ヽ A")
    print ("　　　/ 　 へ＼ B")
    print ("　　 /　　/　＼＼ U")
    print ("　　 |　ノ　　 ヽ_つ L")
    print ("　　/　/ O")
    print ("　 /　/| U")
    print ("　(　(ヽ S")
    print ("　|　|、＼")
    print ("　| 丿 ＼ ⌒)")
    print ("　| |　　) /")
    print ("`ノ )　　Lﾉ")