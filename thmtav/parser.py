from bs4 import BeautifulSoup
import copy
from mastodon import Mastodon
import json
from collections import OrderedDict
import re
from hashlib import sha256

#Mastodon.create_app(
#    'thmtav',
#    api_base_url = 'https://zettel.haus',
#    to_file = 'thmtav.secret'
#)

#mastodon = Mastodon(client_id = 'thmtav.secret',)
#mastodon.log_in(
#    '<user>',
#    '<pass>',
#    to_file = 'thmtav_user.secret'
#)

mastodon = Mastodon(access_token = 'thmtav_user.secret')

with open("relations.json") as file:
    relations = OrderedDict(json.load(file))
    #print(relations)

with open("build/thmtav.html") as file:
    content = file.read()
    detailsoup = BeautifulSoup(content, "html.parser")

    thm_ids = []
    thms = detailsoup.find_all('div', {'class': 'newtheorem'})
    for c in thms:
        details = c.find_all('a')
        idd = details[2]['id']
        thm_ids.append(idd)

        head = c.find('span', {'class': 'cmbx-10'})
        head.replaceWith("#{} {} - ".format(idd, head.string.split(" ")[0]))

        c['id'] = idd

        if not idd in relations:
            relations[idd] = {}

    thms = detailsoup.find_all('div', {'class': 'newtheorem'})
    for c in thms:
        # try to find a parent
        outer = c.find_parent('div', {'class': 'newtheorem'})
        #outer = c.parent.parent.find('div', {'class': 'newtheorem'})
        #print(" {} || {}".format(outer['id'], c['id']))

        if not outer:
            continue

        if outer['id'] == c['id']:
            continue

        relations[c['id']]['parent'] = outer['id']

    #print(relations)

    # remove all links with empty name, otherwise prepend tag path
    for link in detailsoup.find_all('a'):
        if link.string == None:
            link.decompose()
        elif link.attrs['href'][0] == "#":
            link.attrs['href'] = "https://zettel.haus/tags/{}".format(link.attrs['href'][1:])

    # remove all links with empty name
    for link in detailsoup.find_all('p'):
        if len(link.contents) > 0:
            continue

        link.decompose()

    # remove XMLNs fields in math tags
    for math in detailsoup.find_all('math'):
        if "xmlns" in math.attrs:
            math.attrs['xmlns'] = None

    thms = []

    tmp = detailsoup.find_all("div", {"class": "newtheorem"})
    for t in tmp:
        t = copy.copy(t)
        for inner in t.find_all("div", {"class": "newtheorem"}):
            inner.decompose()
    
        thms.append(t)

    out = open("thmtav_out.html", "w")
    for i in thms:
        elm = relations[i['id']]
        if 'parent' in elm:
            parent = elm['parent'] 
            parent = relations[parent]['key']
        else:
            parent = None

        i_str = i.prettify()
        i_str = " ".join(str(i_str).split())

        # don't update if hash matches previous version
        tag = sha256(i_str.encode('utf-8')).hexdigest()
        if "tag" in elm and elm["tag"] == tag:
            continue
        else:
            elm["tag"] = tag

        if "key" in elm:
            print("Updating {} -> {}".format(i['id'], elm['key']))
            ret = mastodon.status_update(elm['key'], i_str)
        else:
            ret = mastodon.status_post(i_str, in_reply_to_id=parent)#, idempotency_key=i['id'])
            print("Created {} as {}".format(i['id'], ret['id']))

        relations[i['id']]['key'] = ret['id']

        #print(i['id'])
        #i = re.sub(' +', ' ', str(i))
        #print(str(i))
        #out.write(str(i))
        #out.write("\n\n")

    with open("relations.json", "w") as file:
        file.write(json.dumps(relations))
    

    #print(detailsoup.prettify())

    print(len(thms))
