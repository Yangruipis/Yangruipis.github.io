# -*- coding: utf-8 -*-
# @File : gen_index.py
# @Author : r.yang
# @Date : Fri Feb 19 18:11:08 2021
# @Description : format string

import os
import sys
from collections import defaultdict
import datetime

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
HEADER = """
#+OPTIONS: ^:nil
#+ATTR_LATEX: :width 5cm :options angle=90
#+TITLE: 索引
#+AUTHOR: 杨 睿
#+EMAIL: yangruipis@163.com
#+KEYWORDS: index
#+OPTIONS: H:4 toc:t
#+SETUPFILE: /Users/yangrui/.local/lib/theme-readtheorg.setup
"""


def extract_abs(path):
    lines = open(path).read().splitlines()
    newlines = []
    for line in lines:
        if line.startswith("*") or line.startswith("#") or line.strip() == "":
            continue
        else:
            newlines.append(line)
    if newlines:
        return "\n".join(newlines)[:200]
    return ""


def main():
    index_txt = HEADER
    src_dir = os.path.join(CURRENT_DIR, '../src')

    for root, dirs, files in os.walk(src_dir):
        eles = root.split("src")[-1].split("/")
        eles = [i for i in eles if i.strip()]
        if eles:
            index_txt += ("*" * (len(eles)) + " {}".format(eles[-1]) + "\n")

        star_len = len(eles) + 1
        for file_ in files:
            if file_.endswith(".org"):
                path = os.path.join(root, file_)
                ts = os.stat(path).st_mtime
                date = datetime.datetime.fromtimestamp(ts)

                title = " [{}] {}".format(date.strftime("%Y-%m-%d"),
                                          file_.replace(".org", ""))

                index_txt += "*" * star_len + " [[file:{}][{}]]".format(
                    "/".join(["./src"] + eles + [file_]), title)
                index_txt += "\n"
                index_txt += extract_abs(os.path.join(root, file_))
                index_txt += "\n"
    with open("./index.org", "w") as f:
        f.write(index_txt)


if __name__ == "__main__":
    main()
