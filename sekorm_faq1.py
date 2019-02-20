#!/usr/bin/env python
# coding=utf-8

import urllib.request
import time
import json
sekorm_faq_mian = "https://www.sekorm.com/faq"
url_waitReply_pre = "https://www.sekorm.com/faq/waitReplyList?currentPage="

num = 0

currentTimeMs = int(time.time()*1000)

#the formate is https://www.sekorm.com/faq/waitReplyList?currentPage=[num]&_=[currentTimeMs]

#url = url_waitReply_pre + num + '&_=' + currentTimeMs
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',\
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',\
    'Connection':'keep-alive',\
    'Cookie':'',\
    'Host':'www.sekorm.com',\
    'Referer':'https://www.sekorm.com/faq/',\
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',\
    'X-Requested-With': 'XMLHttpRequest'
}

#Cookie: waitReplyPageNum=136; _ga=GA1.2.2043198835.1517821185; mem_name=%E5%B0%8F%E7%BE%8A%E7%96%AF%E4%BA%86; zg_did=%7B%22did%22%3A%20%2216260e5be3064a-05d7018baefd94-b34356b-1fa400-16260e5be3121e%22%7D; erpdb01_prod=moVsKh_Cqvv9_FKvB1RdF90h:S; bdshare_firstime=1533572133371; sc1=k%2BDT7qkyaiOnUDT2yWuikbGaqgmhzAyB4orp0G7y9Fk%3D; Hm_lvt_67a4afdc6632a65a0228bd8a1746aaaa=1547430786,1547431049,1547431680,1547689557; JSESSIONID=71CF140853B2B614A659CBAC2289344F; rememberMe=7XwtNz4dzt6jjdUfD7jLu+P4O7a9wzQcgnIpmpxD2HW5BJtTsh3N5h0mCjxhUZpO3TSErxazWqt9ZoiWPmjuqzZwe7t0tZ+b83BtQ0kzXGCe4KkXRzzd/h82YDOsBMhKGHgWYBWOrvmWkowOODzR9P/xj3J/1MxOKTLudB2/G5QgUqN0WKFAz0uQ94VoTrmgqPUQSeHBwl/Ksve/OnRnkF/OIFQD3cFGiiH6AJAVePpCwjXfAkXj8K+WroTVLn7obnxOosB4cr4+LYfOrk5ATXOWCUPZAfEci7LjOFwu1qHCuS/Q6uYauDd1CAEKF60X5UJpriLuwGrFygCV9cxnQV+jaXT/bGVMtgc84TCPr4p84hL4kGRZo6Hm7R6tqVa2EfiCtronfMlqn6fK4J/64fQJqntiV9E6OU8cT1njOsAoC5sGGtw3M41LR7srncXvZw0iQJECUbZknhAJuNWiTHDRlxbNhaFNKmeXRGAwYrY=; Hm_lpvt_67a4afdc6632a65a0228bd8a1746aaaa=1547695793; zg_3433f988d1284213820d2baa69efd433=%7B%22sid%22%3A%201547694880353%2C%22updated%22%3A%201547695793027%2C%22info%22%3A%201547172859267%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.sekorm.com%22%2C%22cuid%22%3A%20%2235443487%22%7D

#get the first waitReply  

#open the file
file_name = 'faq_wait_reply' +  time.strftime("%Y-%m-%d-%H%M", time.localtime()) +'.html'
f = open(file_name,'w')

n = 1000
counter = 2
while counter < 300:
    print('Current Page:%d\n' % (counter-1))
    num = str(counter)
    counter += 1
    currentTime = str(currentTimeMs)
    currentTimeMs += 1
    url = url_waitReply_pre + num + '&_=' + currentTime 
    headers['Cookie'] = 'waitReplyPageNum='+str(int(num)-1)+'; _ga=GA1.2.2043198835.1517821185; mem_name=%E5%B0%8F%E7%BE%8A%E7%96%AF%E4%BA%86; zg_did=%7B%22did%22%3A%20%2216260e5be3064a-05d7018baefd94-b34356b-1fa400-16260e5be3121e%22%7D; erpdb01_prod=moVsKh_Cqvv9_FKvB1RdF90h:S; bdshare_firstime=1533572133371; sc1=k%2BDT7qkyaiOnUDT2yWuikbGaqgmhzAyB4orp0G7y9Fk%3D; Hm_lvt_67a4afdc6632a65a0228bd8a1746aaaa=1547430786,1547431049,1547431680,1547689557; JSESSIONID=71CF140853B2B614A659CBAC2289344F; rememberMe=7XwtNz4dzt6jjdUfD7jLu+P4O7a9wzQcgnIpmpxD2HW5BJtTsh3N5h0mCjxhUZpO3TSErxazWqt9ZoiWPmjuqzZwe7t0tZ+b83BtQ0kzXGCe4KkXRzzd/h82YDOsBMhKGHgWYBWOrvmWkowOODzR9P/xj3J/1MxOKTLudB2/G5QgUqN0WKFAz0uQ94VoTrmgqPUQSeHBwl/Ksve/OnRnkF/OIFQD3cFGiiH6AJAVePpCwjXfAkXj8K+WroTVLn7obnxOosB4cr4+LYfOrk5ATXOWCUPZAfEci7LjOFwu1qHCuS/Q6uYauDd1CAEKF60X5UJpriLuwGrFygCV9cxnQV+jaXT/bGVMtgc84TCPr4p84hL4kGRZo6Hm7R6tqVa2EfiCtronfMlqn6fK4J/64fQJqntiV9E6OU8cT1njOsAoC5sGGtw3M41LR7srncXvZw0iQJECUbZknhAJuNWiTHDRlxbNhaFNKmeXRGAwYrY=; Hm_lpvt_67a4afdc6632a65a0228bd8a1746aaaa=1547695793; zg_3433f988d1284213820d2baa69efd433=%7B%22sid%22%3A%201547694880353%2C%22updated%22%3A%201547695793027%2C%22info%22%3A%201547172859267%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.sekorm.com%22%2C%22cuid%22%3A%20%2235443487%22%7D'
    req = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    index = 0
    reponse_pagenumber = target['data']['pageNumber']
    list = target['data']['results']
    #<a target="_blank" href="https://www.sekorm.com/faq/74651.html">你改，现在我需要贴片电阻_8.2K_0201_1%_-_1/20W_碳膜_防硫，贴片电阻_160K_0201_1%_-_1/20W_碳膜_防硫，贵司是否有代理？急需要，谢谢！</a>
    while index <5 :
        current_faq_url = "https://www.sekorm.com/faq/"+str(list[index]['id'])+".html"
        data_tobe_write = '<a target="_blank" href="'+ current_faq_url + '">' + list[index]['fixedTitle'] + '</a> <br />'
        f.write(data_tobe_write + '\n')
        #print('faq_url: %s\n' % current_faq_url)
        #print('title: %s\n' % list[index]['fixedTitle'])
        index +=1
    #print('\n\n\n')
    if(reponse_pagenumber == 0):
        print('end\n')
        break
