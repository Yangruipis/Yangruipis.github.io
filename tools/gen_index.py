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
#+TITLE: 主页
#+AUTHOR: 杨 睿
#+EMAIL: yangruipis@163.com
#+KEYWORDS: index
#+OPTIONS: H:4 toc:t
#+SETUPFILE: https://gitee.com/yangruigit/my_blogs/raw/master/lib/theme-readtheorg.setup

#+html: <a href="https://github.com/Yangruipis/Yangruipis.github.io/actions">
#+html:   <img src="https://github.com/Yangruipis/Yangruipis.github.io/workflows/CI/badge.svg"/>
#+html: </a>
#+html: <p>&nbsp;</p>

"""


def extract_title(path):
    lines = open(path).read().splitlines()
    lines = [l for l in lines if "+TITLE" in l]
    if not lines:
        return path.split("/")[-1].split(".")[0]
    return ":".join(lines[0].split(":")[1:]).strip()


def extract_abs(path):
    lines = open(path).read().splitlines()
    newlines = []
    for line in lines:
        if line.startswith("*") or line.startswith("#") or line.strip() == "":
            continue
        else:
            newlines.append(line)
    newlines = newlines[:3]
    if newlines:
        return "\n".join(newlines)[:200]
    return ""


def main():
    index_txt = HEADER
    src_dir = os.path.join(CURRENT_DIR, '../src')

    for root, dirs, files in sorted(os.walk(src_dir)):
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

                title = extract_title(os.path.join(root, file_))
                title = " [{}] {}".format(date.strftime("%Y-%m-%d"), title)

                index_txt += "*" * star_len + " [[file:{}][{}]]".format(
                    "/".join(["./src"] + eles + [file_]), title)
                index_txt += "\n"
                index_txt += "    **摘要** ： \n #+begin_verse\n" + extract_abs(os.path.join(root, file_))
                index_txt += "\n... ... \n#+end_verse\n"
    with open("./index.org", "w") as f:
        f.write(index_txt)


if __name__ == "__main__":
    main()
