#!/usr/bin/env python
import os, re, json, requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve

def check_path(path):
    if os.path.exists(path):
        print("[x] File Exists | [!] Exiting...")
        exit(0)
    else:
        return path

def parse_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    shared_data = soup.find('script', text=re.compile('window._sharedData'))
    json_raw = shared_data.text.split(' = ', 1)[1].rstrip(';')
    raw_data = json.loads(json_raw)
    base_data = raw_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
    type_name = base_data['__typename']

    return base_data, type_name

def get_graph_image(base_data, download_path):
    display_url, file_name = base_data['display_url'], base_data['taken_at_timestamp']    
    download_file_name = f"{download_path}/{str(file_name)}.jpg"
    urlretrieve(display_url, check_path(download_file_name))

def get_graph_video(base_data, download_path):
    video_url, file_name = base_data['video_url'], base_data['taken_at_timestamp']
    download_file_name = f"{download_path}/{str(file_name)}.mp4"
    urlretrieve(video_url, check_path(download_file_name))

def get_graph_sideCar(base_data, download_path):
    response = requests.get(f"https://www.instagram.com/p/" + base_data['shortcode'] + "/?__a=1").json()
    counter = 1

    for edge in response['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']:
        file_name = response['graphql']['shortcode_media']['taken_at_timestamp']
        download_file_name = f"{download_path}/{str(file_name)}-{counter}"
        is_video = edge['node']['is_video']

        if not is_video:
            display_url = edge['node']['display_url']
            download_file_name += ".jpg"
            urlretrieve(display_url, check_path(download_file_name))
        else:
            video_url = edge['node']['video_url']
            download_file_name += ".mp4"
            urlretrieve(video_url, check_path(download_file_name))
        
        counter += 1






    


