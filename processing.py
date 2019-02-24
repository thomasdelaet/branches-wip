#!/usr/bin/env python3

import fileinput
import datetime

entries = []
now = datetime.datetime.now(datetime.timezone.utc)

email_to_team_lookup = {
    'thomas@delaet.org': "Tiger Team"
}

team_to_po_lookup = {
    'Tiger Team': 'Alan Smith'
}

for line in fileinput.input():
    line = line.rstrip('\n')
    line = line.split(',')
    date = datetime.datetime.strptime(line[3],"%Y-%m-%d %H:%M:%S %z")
    date_difference = now - date
    author = line[2]
    if author in email_to_team_lookup:
        team = email_to_team_lookup[author]
    else:
        team = 'Unknown'
    if team in team_to_po_lookup:
        po = team_to_po_lookup[team]
    else:
        po = 'Unknown'
    entries.append({
        'repository': line[0],
        'branch': line[1],
        'team': team,
        'po': po,
        'days_since_open': date_difference.days
    })

sorted_list = sorted(entries, key=lambda k: k['days_since_open'], reverse=True) 

for entry in sorted_list:
    print(entry['repository'] + ',' + entry['branch'] + ',' + entry['team'] + ',' + entry['po'] + ',' + str(entry['days_since_open']))
