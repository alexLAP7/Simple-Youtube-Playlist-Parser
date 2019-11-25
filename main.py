from bs4 import BeautifulSoup
import requests


# any url of Your youtube playlist, parses up to 100 videos
url = 'https://www.youtube.com/playlist?list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d'

def list_to_string(given_list: list):  
    string_to_return = ""  
    for each_element in given_list:  
        string_to_return += each_element   
    return string_to_return 

def the_fastest_split(given_str: str, seps: list):
    default_sep = seps[0]
    for sep in seps[1:]:
        given_str = given_str.replace(sep, default_sep)
    return [i.strip() for i in given_str.split(default_sep)]

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

list_of_hrefs = []
list_of_titles = []
for i, tr in enumerate(soup.select('tr.pl-video')):
    each_title = '{}. {}'.format(i + 1, tr['data-title'])
    each_href = 'https://www.youtube.com' + tr.a['href']
    list_of_hrefs.append(each_href)
    list_of_titles.append(each_title)

list_of_separators = ['&']
list_of_separated_videos = []

for index, string in enumerate(list_of_hrefs):
    raw_list_of_string = the_fastest_split(string, list_of_separators)
    list_of_parsed_href = list(filter(None, raw_list_of_string))
    list_of_separated_videos.append(list_of_parsed_href[0])

with open('name_of_your_saved_playlist.txt', 'a', encoding="utf-8") as f:
    for index, value in enumerate(list_of_separated_videos):
        if value:
            f.write('\n' + list_of_titles[index] + '\n')
            f.write(list_of_hrefs[index] + '\n')
            f.write(value + '\n')
            f.write('=====')

print('Done.')