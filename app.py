# -*- coding: utf-8 -*-
from crawler.jp_drama_crawler import JPDramaCrawler
from data.drama_info import DramaInfo
import data.drama_info

if __name__ == "__main__":
    crawler = JPDramaCrawler()
    crawler.retrieve_url()
    dramas = crawler.get_dramas()

    data.drama_info.print_pretty_drama_infos(dramas)
    data.drama_info.write_to_file("Dramas.json", dramas)