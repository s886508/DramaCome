# -*- coding: utf-8 -*-
import re

class DramaInfo:
    def __init__(self):
        self.name = ""
        self.num = 0
        self.url =""

    def parse_name_and_num(self, text):
        """
        Parse given text for drama title and its episode number.
        :param text(str): Text to parse.
        """
        tokens = re.split("第[0-9]+集", text.strip())
        self.name = tokens[0].strip()
        self.num = int(re.sub(r".*[Ee][Pp]", "", tokens[1]))
