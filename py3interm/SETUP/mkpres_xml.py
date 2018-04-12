#!/usr/bin/python

def parse_date(date_string):
    if date_string == 'NONE':
        return '','',''
    else:
        return date_string.split('-')

print('<?xml version="1.0" encoding="UTF-8"?>')
print("\n\n<presidents>\n")

with open("../DATA/presidents.txt") as fp:
    for rec in fp:
        (index,last_name,first_name,
            birth_date, death_date,
            birth_place, birth_state,
            term_start_date, term_end_date,
            party) = rec[:-1].split(":")

        birth_year, birth_month, birth_day = parse_date(birth_date)
        death_year, death_month, death_day = parse_date(death_date)
        ts_year, ts_month, ts_day = parse_date(term_start_date)
        te_year, te_month, te_day = parse_date(term_end_date)

        print("""
    <president>
       <index>{0}</index>
       <name>
           <last>{1}</last>
           <first>{2}</first>
       </name>
       <termstart>
           <year>{3}</year>
           <month>{4}</month>
           <day>{5}</day>
       </termstart>
       <termend>
           <year>{6}</year>
           <month>{7}</month>
           <day>{8}</day>
       </termend>
       <birthplace>{9}</birthplace>
       <birthstate>{10}</birthstate>
       <birth>
           <year>{11}</year>
           <month>{12}</month>
           <day>{13}</day>
       </birth>
       <death>
           <year>{14}</year>
           <month>{15}</month>
           <day>{16}</day>
       </death>
       <party>{17}</party>
    </president> """.format(
            index, last_name, first_name.replace("'","''"),
            ts_year, ts_month, ts_day, te_year, te_month, te_day,
            birth_place, birth_state,
            birth_year, birth_month, birth_day,
            death_year, death_month, death_day,
            party
        ))
         

print("</presidents>")
