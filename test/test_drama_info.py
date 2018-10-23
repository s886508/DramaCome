# -*- coding: utf-8 -*-
import pytest
from data.drama_info import DramaInfo
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

    def test_read_write_file(self):
        info = DramaInfo()
        info.name = "我是老師"
        info.num = 5
        info.url = "https://github.com/s886508/DramaCome"

        file_path = "test.json"

        dramas = [info, info]
        data.drama_info.write_to_file(file_path, dramas)
        assert os.path.exists(file_path) == True

        dramas.clear()
        dramas = data.drama_info.read_from_file(file_path)

        assert len(dramas) == 2
        assert dramas[0].name == "我是老師"
        assert dramas[0].num == 5

        os.remove(file_path)


