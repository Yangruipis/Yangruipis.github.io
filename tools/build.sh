#!/usr/bin/env bash


python tools/gen_index.py

gsed s@CUR_DIR@$PWD@g ./lib/theme-readtheorg.setup.tpl > ./lib/theme-readtheorg.setup

find . -name "*.org" | xargs gsed -i s@'SETUP_FILE'@$PWD/lib/theme-readtheorg.setup@g
find . -name "*.org" | xargs -I {} emacs {} --batch --eval '(setq make-backup-files nil)' -l $PWD/lib/htmlize.el -f org-html-export-to-html
