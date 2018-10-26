# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from drama_come.drama_info import DramaInfo
import requests

JP_LOVE_URL = "http://jp03.jplovetv.com"

class JPDramaCrawler:

    def __init__(self):
        self.__url = JP_LOVE_URL
        self.__html_text = ""

    def retrieve_url(self, url = None):
        """ Try to connect the given url.
        :param url(str): The website to get content.
        :return: True if connect to the site success. Otherwise False.
        """
        if url is None:
            url = self.__url

        try:
            respone = requests.get(url)
            self.__html_text = respone.text
        except:
            return False
        return len(self.__html_text) > 0

    def get_dramas(self, html_text = None):
        """ Parse given html content and parse it to get drama list.
        :param html_text(str): HTML scripts.
        :return: list: DramaInfo
        """
        if html_text is None:
            html_text = self.__html_text
        return self.__parse_html(html_text)

    def __parse_html(self, html_text):
        root_label = "post hentry uncustomized-post-template"
        video_title_label = "video_title"

        drama_info = []
        soup = BeautifulSoup(html_text, "html.parser")
        for node in soup.find_all("div", class_=root_label):
            info = DramaInfo()

            title_node = node.find("div", id=video_title_label)
            if title_node is not None:
                info.parse_name_and_num(title_node.text)
            link_node = node.find("a", href=True)
            if link_node is not None:
                info.url = link_node["href"]

            if len(info.name) > 0 and info.num > 0:
                drama_info.append(info)

        return drama_info