# encoding:utf-8

import urllib2  # mainly use rullib2
import re       

root_url = "http://mebook.cc/page/"  # initial website
f = open('Book.txt', 'w')

cnt = 0
for i in range(1, 11):
    website = set()  # empty website
    url = root_url + str(i)
    response = urllib2.urlopen(url)
    if (response.getcode() == 200):
        print "loading page %d" % i
    else:
        continue
    cont = response.read()
    pattern = re.compile("http://mebook.cc/\d\d\d\d\d.html")
    items = re.findall(pattern, cont)
    for item in items:
        item = item.replace("http://mebook.cc/",
                            "http://mebook.cc/download.php?id=")
        item = item.replace(".html", "")
        website.add(item)
        # print item;
    # print cont;

    for url in website:
        # print url;
        response = urllib2.urlopen(url)
        if (response.getcode() == 200):
            cnt = cnt + 1
            print "crawling book %d" % cnt
        else:
            continue
        cont = response.read()
        # print cont;

        pattern = re.compile('《.*》')
        if re.findall(pattern, cont):
            book_name = re.findall(pattern, cont)
            # print book_name[0];
            f.write(book_name[0])
            f.write("\n")

        pattern = re.compile(
            r"<a href=\"https://pan.baidu.com/s/.*\" target=\"_blank\">百度网盘</a>")
        if re.findall(pattern, cont):
            address = re.findall(pattern, cont)
            address = address[0][9:]
            new_address = ""
            for j in range(len(address)):
                if (address[j] == " " or address[j] == "\""):
                    break
                else:
                    new_address = new_address + address[j]
            # print new_address;
            f.write(new_address)
            f.write("\n")

        pattern = re.compile('百度网盘密码：.*;')
        if re.findall(pattern, cont):
            password = re.findall(pattern, cont)
            password = password[0]
            password.replace("\xa0", "")
            f.write(password[:25])
            f.write("\n\n")
            # print password;
            # print "\n";
    sleep(1)
f.close()
print "Done"
# https://pan.baidu.com/s/1qnB2pHehK3b8RIo68XYB5g
# http://mebook.cc/download.php?id=22560
# 百度网盘密码：engi
