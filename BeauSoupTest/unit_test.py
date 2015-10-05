#!/usr/bin/python
__author__ = 'bill'

import MySQLdb
import re
import datetime
import urllib2


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", "root", 'Edgar20!4', "website")
    cursor = db.cursor()

    # query = 'alter table greentaxi add index(passenger_count)'
    # cursor.execute(query)
    # db.commit()
    # print 'add greentaxi passenger_count'
    #
    # query = 'alter table greentaxi add index(total_amount)'
    # cursor.execute(query)
    # db.commit()
    # print 'add greentaxi total_amount'
    #
    # query = 'alter table greentaxi add index(tpep_pickup_datetime)'
    # cursor.execute(query)
    # db.commit()
    # print 'add greentaxi tpep_pickup_datetime'
    #
    # query = 'alter table yellowtaxi add index(VendorID)'
    # cursor.execute(query)
    # db.commit()
    # print 'add yellow VendorID'
    #
    # query = 'alter table yellowtaxi add index(passenger_count)'
    # cursor.execute(query)
    # db.commit()
    # print 'add yellow passenger_count'
    #
    # query = 'alter table yellowtaxi add index(total_amount)'
    # cursor.execute(query)
    # db.commit()
    # print 'add yellow total_amount'

    query = 'alter table yellowtaxi add index(pickup_longitude)'
    cursor.execute(query)
    db.commit()
    print 'add yellow longitude'

    query = 'alter table yellowtaxi add index(pickup_latitude)'
    cursor.execute(query)
    db.commit()
    print 'add yellow latitude'

    db.close()
    # url = 'http://www.sec.gov/Archives/edgar/data/1013238/0000891092-04-004981.txt'
    # raw_text = urllib2.urlopen(url).read()
    # # filename = 'edgar_data_1013238_0000891092-04-004981.txt'
    # # with open(filename, 'rb') as f:
    # #     raw_text = f.read()
    #
    # # print raw_text
    # # filename = '/'.join(filename.split('_'))
    # raw_text = raw_text.lower()
    #
    # date_match = re.search(r'(january|february|march|april|may|june|july|august|september|october|november|december) ([0-9]{1,2}),* '
    #                        r'(20[0-9][0-9]) .*?press release', raw_text)
    # # print date_match
    # if date_match is not None:
    #     pr_date = datetime.datetime.strptime(date_match.group(1) + ' ' + date_match.group(2) + ' ' +
    #                                           date_match.group(3), '%B %d %Y' )
    #     # print pr_date
    # else:
    #     date_match = re.search(r'press release.*?(january|february|march|april|may|june|july|august|september|october|november|december) ([0-9]{1,2})'
    #                        r',* (20[0-9][0-9])', raw_text, re.DOTALL)
    #     print date_match.group(0)
    #     if date_match is not None:
    #         pr_date = datetime.datetime.strptime(date_match.group(1) + ' ' + date_match.group(2) + ' ' +
    #                                              date_match.group(3), '%B %d %Y')
    #         # print pr_date