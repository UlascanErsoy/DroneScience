from datetime import date

month = {"january":"1","february":"2","march":"3","april":"4","may":"5","june":"6","july":"7","august":"8","september":"9","october":"10","november":"11","december":"12"}
conds = {"Aries":[(321,419)],"Taurus":[(420,520)],"Gemini":[(521,620)],"Cancer":[(621,722)],"Leo":[(723,822)],"Virgo":[(823,922)],"Libra":[(923,1022)],"Scorpio":[(1023,1121)],"Sagittarius":[(1122,1221)],"Capricorn":[(1222,0),(0,119)],"Aquarius":[(120,218)],"Pisces":[(219,320)]}
if __name__ == "__main__":
    m , d = input("Month,Date:").split(",")
    inp = int(month[m]+d)
    for sign , cs in conds.items():
        for c in cs:
            if inp > c[0] and inp < c[1]:
                print(sign)
                exit(0)
