class Classification :#line:4
    def __init__ (OOO0OOO0O00OOO00O ,OOO000O00OO000000 :dict ):#line:5
        OOO0OOO0O00OOO00O .nameAcount =OOO000O00OO000000 ["nameAcount"]#line:6
        OOO0OOO0O00OOO00O .identifier =OOO000O00OO000000 ["identifier"]#line:7
        OOO0OOO0O00OOO00O .number =OOO000O00OO000000 ["number"]#line:8
        OOO0OOO0O00OOO00O .date =OOO000O00OO000000 ["date"]#line:9
        OOO0OOO0O00OOO00O .totalExcludingPackage =OOO000O00OO000000 ["totalExcludingPackage"]#line:10
        OOO0OOO0O00OOO00O .local =Local (OOO000O00OO000000 ["local"])#line:12
        OOO0OOO0O00OOO00O .roaming =Roaming (OOO000O00OO000000 ["roaming"])#line:13
class Local :#line:18
    def __init__ (OOO0O0OOO0000O0O0 ,OO000000000OOO0OO :dict ):#line:20
        OOO0O0OOO0000O0O0 .internet =Internet (OO000000000OOO0OO ["internet"],True )#line:21
        OOO0O0OOO0000O0O0 .call =Appel (OO000000000OOO0OO ["call"])#line:22
        OOO0O0OOO0000O0O0 .sms =SMS (OO000000000OOO0OO ["SMS"])#line:23
        OOO0O0OOO0000O0O0 .mms =MMS (OO000000000OOO0OO ["MMS"])#line:24
class Roaming :#line:27
    def __init__ (O0OO00OO0O0O0O0O0 ,OO0O00OOOO0OOO00O :dict ):#line:29
        O0OO00OO0O0O0O0O0 .internet =Internet (OO0O00OOOO0OOO00O ["internet"],False )#line:30
        O0OO00OO0O0O0O0O0 .call =Appel (OO0O00OOOO0OOO00O ["call"])#line:31
        O0OO00OO0O0O0O0O0 .sms =SMS (OO0O00OOOO0OOO00O ["SMS"])#line:32
        O0OO00OO0O0O0O0O0 .mms =MMS (OO0O00OOOO0OOO00O ["MMS"])#line:33
class Internet :#line:35
    def __init__ (O00OOOO0O0O000000 ,O0O00O0OO0000OO00 :dict ,OOOO0OO0O0O00O0O0 :bool ):#line:37
        O00OOOO0O0O000000 .conso =O0O00O0OO0000OO00 ["conso"]#line:38
        O00OOOO0O0O000000 .total =O0O00O0OO0000OO00 ["consoMax"]#line:39
        O00OOOO0O0O000000 .remaining =O0O00O0OO0000OO00 ["remaining"]#line:40
        O00OOOO0O0O000000 .excludingPackage =O0O00O0OO0000OO00 ["excludingPackage"]#line:41
        if OOOO0OO0O0O00O0O0 :O00OOOO0O0O000000 .carbonFootprint =O0O00O0OO0000OO00 ["carbonFootprint"]#line:43
class Appel :#line:45
    def __init__ (O00OO0OOO0OO00OOO ,O000O000O0OOO00OO :dict ):#line:47
        O00OO0OOO0OO00OOO .conso =O000O000O0OOO00OO ["conso"]#line:48
        O00OO0OOO0OO00OOO .total =O000O000O0OOO00OO ["consoMax"]#line:49
        O00OO0OOO0OO00OOO .callToMyCountry =O000O000O0OOO00OO ["callToMyCountry"]#line:50
        O00OO0OOO0OO00OOO .callToInternational =O000O000O0OOO00OO ["callToInternational"]#line:51
        O00OO0OOO0OO00OOO .excludingPackage =O000O000O0OOO00OO ["excludingPackage"]#line:52
class SMS :#line:54
    def __init__ (O00O00000OO000O00 ,OOO0000O000O0O000 :dict ):#line:56
        O00O00000OO000O00 .conso =OOO0000O000O0O000 ["conso"]#line:57
        O00O00000OO000O00 .total =OOO0000O000O0O000 ["consoMax"]#line:58
        O00O00000OO000O00 .maxNbSMS =OOO0000O000O0O000 ["maxNbSMS"]#line:59
        O00O00000OO000O00 .nbSMS =OOO0000O000O0O000 ["nbSMS"]#line:60
        O00O00000OO000O00 .excludingPackage =OOO0000O000O0O000 ["excludingPackage"]#line:61
class MMS :#line:64
    def __init__ (OO00O00O0O00OO00O ,O00OOO000OOOOOOO0 :dict ):#line:66
        OO00O00O0O00OO00O .conso =O00OOO000OOOOOOO0 ["conso"]#line:67
        OO00O00O0O00OO00O .total =O00OOO000OOOOOOO0 ["consoMax"]#line:68
        OO00O00O0O00OO00O .maxNbMMS =O00OOO000OOOOOOO0 ["maxNbMMS"]#line:69
        OO00O00O0O00OO00O .nbMMS =O00OOO000OOOOOOO0 ["nbMMS"]#line:70
        OO00O00O0O00OO00O .excludingPackage =O00OOO000OOOOOOO0 ["excludingPackage"]
