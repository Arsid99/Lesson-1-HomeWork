import json

with open('acdc.json') as file:
    data = json.load(file)['album']['tracks']['track']

def duration_track(data):
    new_list = []
    for elem in data:
        new_list.append(int(elem['duration']))
    return sum(new_list)

def convert_to_preferred_format(sec):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60

    return "%02d:%02d:%02d" % (hour, min, sec)

print(f"The music will last {duration_track(data)} seconds or {convert_to_preferred_format(duration_track(data))} minutes")














