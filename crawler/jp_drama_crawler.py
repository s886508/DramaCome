# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

JP_LOVE_URL = "http://jp03.jplovetv.com"

class JPDramaCrawler:

    def __init__(self):
        self.__url = JP_LOVE_URL

    def retrieve_url(self):
        return False

    def get_dramas(self, html_text = ""):
        return {}