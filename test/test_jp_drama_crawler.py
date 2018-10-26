# -*- coding: utf-8 -*-
from drama_come.drama_crawler import JPDramaCrawler

class TestCrawler(object):

    def test_get_data(self):
        crawler = JPDramaCrawler()

        ret = crawler.retrieve_url("http://jp03.jplovetv.com")
        assert ret == True

        ret = crawler.retrieve_url("")
        assert ret == False

        ret = crawler.retrieve_url("http://123")
        assert ret == False

    def test_parse_data(self):
        html_text = """<div class="post hentry uncustomized-post-template" itemprop="blogPost" itemscope="itemscope" itemtype="http://schema.org/BlogPosting">
<meta content="1222401613855953790" itemprop="blogId"/>
<meta content="1833387847930008325" itemprop="postId"/>
<a name="1833387847930008325"></a>
<h3 class="post-title entry-title" itemprop="name">
<a href="http://jp03.jplovetv.com/2018/10/legal-v-2-jp181011-ep2.html">Legal V 前律師小鳥遊翔子 第2集 JP181011 Ep2</a>
</h3>
<div class="post-header">
<div class="post-header-line-1"></div>
</div>
<div class="post-body entry-content" id="post-body-1833387847930008325" itemprop="description articleBody">
<p>
Legal V 前律師小鳥遊翔子 第2集 JP181011 Ep2
<br/>
<div id="video_div">
<div id="video_ids" style="display:none;">k2JkRUn1uDXcSIs9FVa</div>
<div id="video_title" style="display:none;">Legal V 前律師小鳥遊翔子 第2集 JP181011 Ep2</div>
<div id="video_type" style="display:none;">2</div>
<div id="video_word" style="display:none;">日本電視劇 Legal V 前律師小鳥遊翔子 線上看tv在lovetvshow,Legal V 前律師小鳥遊翔子 最喜歡的日劇影片,Legal V 前律師小鳥遊翔子 演員陣容 米倉涼子 林遣都 向井理</div>
</div>
</p>
Ep2 Source 2<br/>
<div id="video_div_s2">
<div id="video_ids_s2" style="display:none;">P2cQ6_s01n0</div>
<div id="video_type_s2" style="display:none;">3</div>
</div>
<div style="clear: both;"></div>
</div>
<div class="post-footer">
<div class="post-footer-line post-footer-line-1">
<span class="post-author vcard">
</span>
<span class="post-timestamp">
</span>
<span class="reaction-buttons">
</span>
<span class="post-comment-link">
</span>
<span class="post-backlinks post-comment-link">
</span>
<span class="post-icons">
<span class="item-control blog-admin pid-1371793984">
<a href="https://www.blogger.com/post-edit.g?blogID=1222401613855953790&amp;postID=1833387847930008325&amp;from=pencil" title="編輯文章">
<img alt="" class="icon-action" height="18" src="https://resources.blogblog.com/img/icon18_edit_allbkg.gif" width="18"/>
</a>
</span>
</span>
<div class="post-share-buttons goog-inline-block">
</div>
</div>
<div class="post-footer-line post-footer-line-2">
<span class="post-labels">
標籤：
<a href="http://jp03.jplovetv.com/search/label/2018%E6%97%A5%E6%9C%AC%E9%9B%BB%E8%A6%96%E5%8A%87-Legal%20V%20%E5%89%8D%E5%BE%8B%E5%B8%AB%E5%B0%8F%E9%B3%A5%E9%81%8A%E7%BF%94%E5%AD%90" rel="tag">2018日本電視劇-Legal V 前律師小鳥遊翔子</a>
</span>
</div>
<div class="post-footer-line post-footer-line-3">
<span class="post-location">
</span>
</div>
</div>
</div>"""
        crawler = JPDramaCrawler()

        drama_coming = crawler.get_dramas(html_text)
        assert len(drama_coming) > 0
        assert drama_coming[0].name == "Legal V 前律師小鳥遊翔子"
        assert drama_coming[0].num == 2
        assert drama_coming[0].url == "http://jp03.jplovetv.com/2018/10/legal-v-2-jp181011-ep2.html"

        drama_coming = crawler.get_dramas("")
        assert len(drama_coming) == 0

        drama_coming = crawler.get_dramas("1234567")
        assert len(drama_coming) == 0
