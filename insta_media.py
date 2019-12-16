#!/usr/bin/env python
import os, time
from sys import argv
from functions import check_args, select_media
from parser import parse_data, load_js, dump
from urllib.request import urlopen

if __name__ == '__main__':

    os.system('clear')
    time.sleep(1)

    html, path, op_type = check_args(len(argv), argv)
    if op_type == "single_post":
        base_data, type_name = parse_data(html)
        select_media(type_name, base_data, path)
        print("[*] Done!")
    else:
        html = load_js(argv[2])
        links, dump_dir = dump(html, argv[2], path)
        for l in links:
            output(l)
            link_html = urlopen(l).read()
            base_data, type_name = parse_data(link_html)
            select_media(type_name, base_data, dump_dir)
        print("[*] Done!")

