class EVCalculation():
    def computeEV (ba, iv, ev, lvl, modi, stats):
        S=(((2*ba)+iv+(ev/4)) * ( lvl/100))
        StatsModify = stats/modi
        return (((((StatsModify - S) * 400 )) / lvl) / 4 ) * 4