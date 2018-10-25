# -*- coding: utf-8 -*-
from crawler.jp_drama_crawler import JPDramaCrawler
from data.drama_info import *
import data.drama_info

if __name__ == "__main__":
    handler = DramaInfoHandler()
    dramas = handler.read_from_file("Dramas.json")
    crawler = JPDramaCrawler()
    crawler.retrieve_url()
    for new_drama in crawler.get_dramas():
        handler.add_drama(new_drama)

    handler.print_pretty_drama_infos()
    handler.write_to_file("Dramas.json")
    handler.write_to_file_html("drama.html")