import json

import requests

url_ddg = "https://api.duckduckgo.com"


def test_ddg0():
    q = "presidents of the united states"
    resp = requests.get(url_ddg + "/?q=" + q + "&format=json")
    rsp_data = resp.json()
    # print(json.dumps(rsp_data, indent=4))
    print(rsp_data['RelatedTopics'])
    assert check_presidents(rsp_data['RelatedTopics'])




def check_presidents(topics):
    pres_list = ["Washington", "Lincoln", "Adams", "Jefferson", "Madison", "Monroe","Adams", "Jackson", "Van Buren",
                 "Harrison", "Tyler", "Polk", "Taylor", "Fillmore", "Pierce", "Buchanan", "Johnson", "Grant",
                 "Hayes", "Garfield", "Arthur", "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson", "Harding",
                 "Coolidge", "Hoover", "Truman", "Eisenhower", "Kennedy", "Johnson", "Nixon", "Ford", "Carter",
                 "Reagan", "Bush", "Clinton", "Obama", "Trump", "Biden"]
    for president in pres_list:
        for topic in topics:
            if president in topic['Text']:
                break
        else:
            return False
    return True

