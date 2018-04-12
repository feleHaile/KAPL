#!/usr/bin/python3
import sys
import json

# not in std lib
import web
from mimerender import mimerender

# adapted from
# http://stackoverflow.com/questions/713847/recommendations-of-python-rest-web-services-framework


from collections import namedtuple

def render_html(**info):
    return """
<html>
<title>{0.FirstName} {0.LastName}</title>
</html>
<body>
{0.FirstName} {0.LastName}<br/ >
{0.BirthState}<br/ >
{0.Party}<br/ >
<br/ >
FRUIT: {1}<br/ >
</body>
</html>
    """.format(info['president'],info['fruit'])
    
def render_json(**info):
    return json.dumps(
        [
            info['fruit'],
            [
                info['president'].last_name,
                info['president'].FirstName,
                info['president'].BirthState,
                info['president'].Party,
            ]
        ]
    )
    
def render_text(**info):
    return """
{0.FirstName} {0.LastName}
{0.BirthState}
{0.Party}
FRUIT: {1}
    """.format(info['president'],info['fruit'])

def render_xml(**info):
    return """
<info>
    <president>
        <firstname>{0.FirstName}</firstname>
        <lastname>{0.LastName}</lastname>
        <state>{0.BirthState}</state>
        <party>{0.Party}</party>
    </president>
    <fruit>{1}</fruit>
</info>
    """.format(info['president'],info['fruit'])



#   web.config.debug = 0  # turn off for production

President = namedtuple(
    'President',
    'Term LastName FirstName BirthState Party '
)

presidents = []

def build_data():
    with open('DATA/presidents.txt') as PRES:
        for rec in PRES:
            flds=rec.rstrip().split(':')
            presidents.append(President(flds[0],flds[1],flds[2],flds[10],flds[17]))

class PresidentByTerm(object):
    @mimerender(
        default='html',
        xml = render_xml,
        json = render_json,
        txt = render_text,
        html = render_html
    )
    def GET(self,term_str,fruit=None):
        term = int(term_str)-1
        return {'fruit':fruit,'president':presidents[term]}

class PresidentsByLastName(object):
    def GET(self,lastname):
        recs = [
            "{0.FirstName} {0.LastName}".format(p)
            for p in presidents
            if p.last_name.startswith(lastname)
        ]
        return json.dumps(recs)

urls = (
    '/presidents/(\d+)', 'PresidentByTerm',
    '/presidents/(\d+)/([a-z]+)', 'PresidentByTerm',  # 2nd field is fruit
    '/presidents/([a-zA-Z]+)', 'PresidentsByLastName'
)

app = web.application(urls,globals())

build_data()

if __name__ == '__main__':  # do it this way!
    app.run()
