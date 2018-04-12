#!/usr/bin/python3
import sys
import json

# not in std lib
import web
from mimerender import WebPyMimeRender
renderer = WebPyMimeRender()

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
</body>
</html>
    """.format(info['president'])
    
def render_json(**info):
    return json.dumps(
        {
            'Lastname':info['president'].last_name,
            'FirstName':info['president'].FirstName,
            'BirthState':info['president'].BirthState,
            'Party':info['president'].Party,
        }
    )
    
def render_text(**info):
    return """
{0.FirstName} {0.LastName}
{0.BirthState}
{0.Party}
    """.format(info['president'])

def render_xml(**info):
    return """
<info>
    <president>
        <firstname>{0.FirstName}</firstname>
        <lastname>{0.LastName}</lastname>
        <state>{0.BirthState}</state>
        <party>{0.Party}</party>
    </president>
</info>
    """.format(info['president'])



#   web.config.debug = 0  # turn off for production

# new magic!
President = namedtuple(
    'President',
    'Term LastName FirstName BirthState Party '
)

presidents = []

def build_data():
    with open('../DATA/presidents.txt') as PRES:
        for rec in PRES:
            flds=rec.rstrip().split(':')
            presidents.append(President(flds[0],flds[1],flds[2],flds[10],flds[17]))

class PresidentByTerm(object):
    @renderer(
        default='html',
        xml = render_xml,
        json = render_json,
        txt = render_text,
        html = render_html
    )
    def GET(self,term_str):
        term = int(term_str)-1
        return {'president':presidents[term]}

class PresidentsByLastName(object):
    def GET(self,lastname):
        recs = [
            "{0.FirstName} {0.LastName}".format(p)
            for p in presidents
            if p.last_name.lower().startswith(lastname.lower())
        ]
        return json.dumps(recs)

urls = (
    '/presidents/(\d+)', 'PresidentByTerm',
    '/presidents/([a-zA-Z]+)', 'PresidentsByLastName'
)

app = web.application(urls,globals())

build_data()

if __name__ == '__main__':  # do it this way!
    app.run()
