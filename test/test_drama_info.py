# -*- coding: utf-8 -*-
import pytest
from data.drama_info import *
import data.drama_info
import os

class TestDramaInfo(object):
    def test_parse_name_and_num(self):
        # Case 1
        str = "可愛萬歲 第1集 JP181018 Ep1"
        info = DramaInfo()
        info.parse_name_and_num(str)

        assert info.name == "可愛萬歲"
        assert info.num == 1

        # Case 2
        str = "我是老師 第10集 JP181018 Ep10"
        info = DramaInfo()
        info.parse_name_and_num(str)

        assert info.name == "我是老師"
        assert info.num == 10

        # Case 3
        str = "我是老師 第10集 JP181018 Ep"
        info = DramaInfo()
        info.parse_name_and_num(str)

        assert info.name == "我是老師"
        assert info.num == 0

        # Case 4
        str = "我是老師 特別篇 JP181018 Special"
        info = DramaInfo()
        info.parse_name_and_num(str)

        assert info.name == ""
        assert info.num == 0

    def test_handler_add_item(self):
        handler = DramaInfoHandler()
        assert len(handler.get_dramas()) == 0

        info = DramaInfo()
        info.name = "我是老師"
        info.num = 5
        info.url = "https://github.com/s886508/DramaCome"
        handler.add_drama(info)
        assert len(handler.get_dramas()) == 1

        handler.add_drama(info)
        assert len(handler.get_dramas()) == 1

    def test_handler_read_write_file(self):
        info = DramaInfo()
        info.name = "我是老師"
        info.num = 5
        info.url = "https://github.com/s886508/DramaCome"

        info2 = DramaInfo()
        info2.name = "我是老師"
        info2.num = 10
        info2.url = "https://github.com/s886508/DramaCome"

        file_path = "test.json"

        handler = DramaInfoHandler()

        handler.add_drama(info)
        handler.add_drama(info2)
        handler.write_to_file(file_path)
        assert os.path.exists(file_path) == True

        handler.read_from_file(file_path)
        dramas = handler.get_dramas()
        single_drama_list = dramas.get("我是老師")

        assert len(dramas) == 1
        assert single_drama_list is not None
        assert len(single_drama_list) == 2
        assert single_drama_list[0].num == 5
        assert single_drama_list[1].num == 10

        os.remove(file_path)




