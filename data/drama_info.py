# -*- coding: utf-8 -*-
import re
from tinydb import TinyDB, Query

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
        if len(tokens) > 1:
            self.name = tokens[0].strip()
            self.num = int(re.sub(r".*[Ee][Pp]", "", tokens[1]))

def print_pretty_drama_infos(infos):
    for i in infos:
        print("%s   EP %d   %s" % (i.name, i.num, i.url))

def write_to_file(path, infos):
    """
    :param path(str): Path to save drama info to database.
    :param infos(list): Drama info list to write to database.
    """
    db = TinyDB(path)
    for i in infos:
        db.insert({"name": i.name, "num": i.num, "url": i.url})
    db.close()

def read_from_file(path):
    """

    :param path(str): Path to load drama info from database.
    :return: List of drama info.
    """
    infos = []

    db = TinyDB(path)
    for i in db.all():
        drama_info = DramaInfo
        drama_info.name = i.name
        drama_info.num = int(i.num)
        drama_info.url = i.url
        infos.append(drama_info)
    db.close()

    return infos