#!/usr/bin/env python
import os
from sys import exit
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from parser import get_graph_image, get_graph_video, get_graph_sideCar

def check_url(url):
    try:
        html = urlopen(url).read()
    except HTTPError as http_error:
        print(f"[x] HTTP Error encountered:\n{http_error}")
        exit(0)
    except URLError as url_error:
        print(f"[x] URL Error encountered:\n{url_error}")
        exit(0)
    else:
        return html

def check_args(arg_len, arg_list):
    if arg_len == 2 or arg_len == 4:
        if arg_len == 2:
            return check_url(arg_list[1]), "./"
        elif arg_len == 4:
            response = check_url(arg_list[1])
            if arg_list[2] == "-p":
                return response, arg_list[3]
            else:
                print(f"[!] Usage: {arg_list[0]} <URL> [-p <PATH>]")
                exit(0)
    else:
        print(f"[!] Usage: {arg_list[0]} <URL> [-p <PATH>]")
        exit(0)

def select_media(type_name, base_data, download_path):
    if type_name == 'GraphImage':
        get_graph_image(base_data, download_path)
    elif type_name == 'GraphVideo':
        get_graph_video(base_data, download_path)
    elif type_name == 'GraphSidecar' :
        get_graph_sideCar(base_data, download_path)
    else:
        print("[x] Media not found!")
        exit(0)

        