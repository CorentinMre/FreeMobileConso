import requests #line:1
from bs4 import BeautifulSoup #line:2
from .import dataClassification #line:3
class Client :#line:4
    def __init__ (OO00000000O00O00O ,OO0O0000O0OOOOO00 ,O00O0OO0OOO0OO0OO ):#line:5
        OO00000000O00O00O .identifiant =OO0O0000O0OOOOO00 #line:6
        OO00000000O00O00O .password =O00O0OO0OOO0OO0OO #line:7
        OO00000000O00O00O .payload ={"login-ident":OO00000000O00O00O .identifiant ,"login-pwd":OO00000000O00O00O .password ,"bt-login":"1"}#line:8
        OO00000000O00O00O .session =requests .Session ()#line:9
        OO00000000O00O00O .session .headers .update ({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"})#line:10
        OO00000000O00O00O .urlLogin ="https://mobile.free.fr/account/"#line:11
        OO00OOOOOO00O0OO0 =["conso","consoMax","remaining","excludingPackage","carbonFootprint"]#line:12
        O0OOO00O0OO0OOOO0 =["conso","consoMax","callToMyCountry","callToInternational","excludingPackage"]#line:13
        O0O0OOOOO0OOOO000 =["conso","consoMax","maxNbSMS","nbSMS","excludingPackage"]#line:14
        O00O0O00OO0OO0O00 =["conso","consoMax","maxNbMMS","nbMMS","excludingPackage"]#line:15
        OO00000000O00O00O .dictOfAllInformation ={"internet":OO00OOOOOO00O0OO0 ,"call":O0OOO00O0OO0OOOO0 ,"SMS":O0O0OOOOO0OOOO000 ,"MMS":O00O0O00OO0OO0O00 }#line:16
    def getConsoDict (O0O0OO00OO0OOO000 )->dict :#line:17
        O0OO00O000O000O0O =O0O0OO00OO0OOO000 .session .post (O0O0OO00OO0OOO000 .urlLogin ,data =O0O0OO00OO0OOO000 .payload )#line:18
        OOOOO0O000O0OOO00 =BeautifulSoup (O0OO00O000O000O0O .content ,"html.parser")#line:19
        O0OO000000OOOO000 =OOOOO0O000O0OOO00 .find ("div",{"class":"current-user__infos"})#line:20
        try :#line:21
            O0O0O0OO0O0OOO0OO =O0OO000000OOOO000 .find ("div",{"class":"identite_bis"}).text .strip ()#line:22
        except :#line:23
            raise Exception ("Identifiant or password is incorrect")#line:24
        O0O0O0OO0O0OOO0OO =O0OO000000OOOO000 .find ("div",{"class":"identite_bis"}).text .strip ()#line:25
        OOO0OOOOOO0O0OO0O =O0OO000000OOOO000 .findAll ("div",{"class":"smaller"})[0 ].text .strip ()#line:26
        OO00OO0O0OOOOO0OO =O0OO000000OOOO000 .findAll ("div",{"class":"smaller"})[1 ].text .strip ()#line:27
        OO000000OOOO00OOO =OOOOO0O000O0OOO00 .find ("div",{"class":"details"}).find ("div",{"class":"sub-title"}).text .strip ()#line:28
        O0OOO00000OO0O000 ={}#line:29
        for _OO0OOO0OOOOO00000 in range (2 ):#line:30
            O0O00O00000OO000O =OOOOO0O000O0OOO00 .find ("div",{"class":"conso-local"})if _OO0OOO0OOOOO00000 ==0 else OOOOO0O000O0OOO00 .find ("div",{"class":"conso-roaming"})#line:31
            O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]]={}#line:32
            for O0O0OO00O0O00O0OO ,O0OO0O0OOOOOO0O00 in O0O0OO00OO0OOO000 .dictOfAllInformation .items ():#line:33
                if O0O0OO00O0O00O0OO =="internet":OOOO00OOO00O0OO0O =0 #line:34
                elif O0O0OO00O0O00O0OO =="call":OOOO00OOO00O0OO0O =1 #line:35
                elif O0O0OO00O0O00O0OO =="SMS":OOOO00OOO00O0OO0O =2 #line:36
                elif O0O0OO00O0O00O0OO =="MMS":OOOO00OOO00O0OO0O =3 #line:37
                O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ]={}#line:38
                O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [0 ]]=O0O00O00000OO000O .findAll ("div",{"class":"number-circle"})[OOOO00OOO00O0OO0O ].find ("span").text .strip ().replace ("*","")#line:39
                OO0O0O0OO0OO000O0 =O0O00O00000OO000O .findAll ("div",{"class":"number-circle"})[OOOO00OOO00O0OO0O ].find ("p").text .strip ().replace ("*","")#line:40
                if "/"in OO0O0O0OO0OO000O0 :#line:41
                    O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [1 ]]=OO0O0O0OO0OO000O0 .split ("/")[1 ]#line:42
                else :#line:43
                    O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [1 ]]=OO0O0O0OO0OO000O0 #line:44
                if O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [1 ]]=="":#line:45
                    O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [1 ]]=O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [0 ]]#line:46
                O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [2 ]]=O0O00O00000OO000O .findAll ("div",{"class":"text-conso-content"})[OOOO00OOO00O0OO0O ].findAll ("p")[0 ].find ("span").text .replace ("/ ","").strip ().replace ("*","")#line:47
                O000O0OO00000OO00 =O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [3 ]]=O0O00O00000OO000O .findAll ("div",{"class":"text-conso-content"})[OOOO00OOO00O0OO0O ].findAll ("p")#line:48
                O000O0OOOOOO0OOOO =O0O00O00000OO000O .findAll ("div",{"class":"text-conso-content"})[OOOO00OOO00O0OO0O ].findAll ("p")#line:49
                OOOO0O00OO0O00000 =O0O00O00000OO000O .findAll ("div",{"class":"text-conso-content"})[OOOO00OOO00O0OO0O ].findAll ("p")[1 ].text .strip ().split (": ")[1 ].replace ("*","")#line:50
                if O0O0OO00O0O00O0OO =="internet":#line:51
                    O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [3 ]]=O000O0OO00000OO00 [1 ].text .strip ().split (": ")[1 ].replace ("*","")#line:52
                elif O0O0OO00O0O00O0OO =="call":#line:53
                    O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [3 ]]=O000O0OO00000OO00 [1 ].text .strip ().split (": ")[1 ].replace ("*","")#line:54
                    O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [4 ]]=O000O0OOOOOO0OOOO [2 ].text .strip ().split (": ")[1 ].replace ("*","")#line:55
                else :#line:56
                    O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [3 ]]=O000O0OO00000OO00 [0 ].text .strip ().split (" / ")[0 ].replace ("*","")#line:57
                    O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [4 ]]=OOOO0O00OO0O00000 #line:58
                if O0O0OO00O0O00O0OO =="internet"and O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]=="local":#line:59
                    O0OOO00000OO0O000 [O0O00O00000OO000O ["class"][1 ].split ("-")[1 ]][O0O0OO00O0O00O0OO ][O0OO0O0OOOOOO0O00 [4 ]]=O000O0OOOOOO0OOOO [2 ].text .strip ().split (": ")[1 ].replace ("*","")#line:60
        O0OOO00000OO0O000 ["totalExcludingPackage"]=0 #line:61
        for O0O0OO00O0O00O0OO ,O0OO0O0OOOOOO0O00 in O0OOO00000OO0O000 .items ():#line:62
            if O0O0OO00O0O00O0OO =="local"or O0O0OO00O0O00O0OO =="roaming":#line:63
                for OOOOO000O0O0000O0 ,O0O0OO00000O0OOOO in O0OO0O0OOOOOO0O00 .items ():#line:64
                    for OO0O0000O0OOO0000 ,O00OOOO0O0O0O0O00 in O0O0OO00000O0OOOO .items ():#line:65
                        if OO0O0000O0OOO0000 =="excludingPackage":#line:66
                            O0OOO00000OO0O000 ["totalExcludingPackage"]+=float (O00OOOO0O0O0O0O00 .replace ("€",""))#line:67
        O0OOO00000OO0O000 ["totalExcludingPackage"]=str (O0OOO00000OO0O000 ["totalExcludingPackage"])+"€"#line:68
        O0OOO00000OO0O000 ["nameAcount"]=O0O0O0OO0O0OOO0OO #line:69
        O0OOO00000OO0O000 ["identifier"]=OOO0OOOOOO0O0OO0O .split (" : ")[1 ]#line:70
        O0OOO00000OO0O000 ["number"]=OO00OO0O0OOOOO0OO .split (" : ")[1 ].replace (" ","")#line:71
        O0OOO00000OO0O000 ["date"]=OO000000OOOO00OOO #line:72
        return O0OOO00000OO0O000 #line:73
    def consommation (OO0OOO00OOOOO000O )->dict :#line:74
        return dataClassification .Classification (OO0OOO00OOOOO000O .getConsoDict ())#line:75
