import sys
import json
import os.path


def traceit(frame, event, arg):
    if event == "line":
        lineno = frame.f_lineno
        # print(frame.f_code)
        filename = os.path.basename(frame.f_globals["__file__"])
        print("==> file {0} line {1}".format(filename, lineno))
    return traceit

sys.settrace(traceit)


def loads_json(): 
    with open('../DATA/solar.json') as SOLAR:
        raw_json = SOLAR.read()

    solar = json.loads(raw_json)
    for k,v in solar.items():
        print(k,v)

loads_json()
