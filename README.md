# DramaCome
Get lasted Japanese drama from website.

## Example

### code
```
crawler = JPDramaCrawler()
crawler.retrieve_url()
dramas = crawler.get_dramas()
print(DramaInfo.get_info_str(dramas))
```

### output
```
深夜的奇葩戀愛圖鑑   EP 4
http://jp03.jplovetv.com/2018/10/4-jp181006-ep4.html
主婦勝利   EP 3
http://jp03.jplovetv.com/2018/10/3-jp181007-ep3.html
我是大哥大   EP 3
http://jp03.jplovetv.com/2018/10/3-jp181014-ep3.html
```