# -*- coding: utf-8 -*-
import pytest
from crawler.jp_drama_crawler import JPDramaCrawler

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
        html_text = ""
        crawler = JPDramaCrawler()

        drama_coming = crawler.get_dramas(html_text)
        assert len(drama_coming) > 0

        drama_coming = crawler.get_dramas("")
        assert len(drama_coming) == 0

        drama_coming = crawler.get_dramas("1234567")
        assert len(drama_coming) == 0
