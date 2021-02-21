#!/usr/bin/env bash


python tools/gen_index.py

find . -name "*.org" | xargs -I {} emacs {} --batch --eval '(setq make-backup-files nil)' --eval "(setq org-html-checkbox-type 'html)" --eval "(setq org-html-htmlize-output-type 'css)" -l $PWD/lib/htmlize.el -f org-html-export-to-html
