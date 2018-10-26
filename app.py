# -*- coding: utf-8 -*-
from drama_come.drama_crawler import JPDramaCrawler
from drama_come.drama_info import *

if __name__ == "__main__":
    handler = DramaInfoHandler()
    #dramas = handler.read_from_file("Dramas.json")
    crawler = JPDramaCrawler()
    crawler.retrieve_url()
    dramas = crawler.get_dramas()
    for new_drama in dramas:
        handler.add_drama(new_drama)

    print(DramaInfo.get_info_str(dramas))
    #print(handler.get_drama_info_string())
    #handler.write_to_file("Dramas.json")
    #handler.write_to_file_html("drama.html")