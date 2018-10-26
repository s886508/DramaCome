# -*- coding: utf-8 -*-
from tinydb import TinyDB, Query
import re
import os

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
            tokens[1] = re.sub(r".*[Ee][Pp]", "", tokens[1])
            if len(tokens[1]) > 0:
                self.num = int(tokens[1])


class DramaInfoHandler:
    """Store drama infos and provide functions to output as file or html."""

    def __init__(self):
        self.__dramas = {}

    def get_dramas(self):
        return self.__dramas

    def add_drama(self, drama):
        single_drama_list = self.__dramas.get(drama.name)
        if single_drama_list is None:
            single_drama_list = []
        exist = False
        for i in single_drama_list:
            if i.name == drama.name and i.num == drama.num:
                exist = True
                break
        if not exist:
            single_drama_list.append(drama)
        self.__dramas[drama.name] = single_drama_list

    def print_pretty_drama_infos(self):
        for v in self.__dramas.values():
            for i in v:
                print("%s   EP %d   %s" % (i.name, i.num, i.url))

    def write_to_file_html(self, path):
        file = None
        if not os.path.exists(path):
            file = open(path, "x")
        if file is None:
            file = open(path, "w")

        html_text = """<html>
        <head>
        <title>Drama coming</title>
        </head>
        <body>%s</body>
        </html>"""
        drama_content_html = ""
        for v in self.__dramas.values():
            for i in v:
                drama_content_html += """<a target="_blank" href="%s">%s EP %s</a><br>""" % (i.url, i.name, str(i.num))
        html_text = html_text % (drama_content_html)
        file.write(html_text)


    def write_to_file(self, path):
        """
        :param path(str): Path to save drama info to database.
        :param infos(list): Drama info list to write to database.
        """
        db = TinyDB(path)
        for v in self.__dramas.values():
            for i in v:
                db.insert({"name": i.name, "num": i.num, "url": i.url})
        db.close()

    def read_from_file(self, path):
        """ Read saved drama data from file.

        :param path(str): Path to load drama info from database.
        """
        self.__dramas.clear()
        db = TinyDB(path)
        for i in db.all():
            drama_info = DramaInfo()
            drama_info.name = i["name"]
            drama_info.num = int(i["num"])
            drama_info.url = i["url"]
            self.add_drama(drama_info)
        db.close()