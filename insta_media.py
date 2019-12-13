#!/usr/bin/env python
from sys import argv
from functions import check_args, select_media
from parser import parse_data, get_graph_image

if __name__ == '__main__':
    html, path = check_args(len(argv), argv)
    base_data, type_name = parse_data(html)
    select_media(type_name, base_data, path)

    

    #print(f"path: {path}\nhtml: \n\n{html}")
