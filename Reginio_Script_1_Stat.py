class StatCalculation():
    def Health (ba, ev, lvl, iv):
        return ((((2*ba+iv+(ev/4))*lvl)/100))+lvl+10
        
    def OtherStat(ba, iv, ev, lvl, ntr):
        return ((((((2 * ba) + iv + (ev /4) ) * lvl)) / 100 ) + 5 ) * ntr