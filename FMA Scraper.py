#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, re, codecs

regex = re.compile('((http:\/\/freemusicarchive.org\/music\/download\/)\w+)')
genres = ['Dance', 'Downtempo', 'Drum_amp_Bass', 'Dubstep', 'Skweee', 'Glitch', 'House', 'Chill-out', 'IDM', 'Jungle', 'Minimal_Electronic', 'Techno', 'Bigbeat','Trip-Hop']
genreCount = 0

while genreCount < 13:
    genre = genres[genreCount]
    URL = 'http://freemusicarchive.org/genre/' + genre + '/?sort=track_date_published&d=120&page=1&per_page=200'
    r = requests.get(URL)
    content = r.text
    file = codecs.open(genre + '.fma', 'w+', 'utf-8')
    filteredContent = re.findall(regex, content)
    for item in filteredContent:
        file.write(item[0])
        file.write('\n')
    file.close()
    print genre + ' list populated!'
    genreCount += 1
