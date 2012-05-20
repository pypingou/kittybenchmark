# -*- coding: utf-8 -*-

import datetime
import time
from kittystore.kittysastore import KittySAStore
from kittystore.mongostore import KittyMGStore

# Define global constant

TABLE = 'devel'
REP = 30
URL = 'postgres://mm3:mm3@localhost/mm3'
DB_STORE = KittySAStore(URL)
MG_STORE = KittyMGStore(host='localhost', port=27017)

START = datetime.datetime(2012, 3, 1)
END = datetime.datetime(2012, 3, 30)

def output(name, post, mongo):
    stream = open(name, 'w')
    stream.write('MG\tPG\n')
    for i in range(0, len(post)):
        stream.write('%s\t%s\n' % (mongo[i], post[i]))
    stream.close()

def output_2(name, mongo, mongo_cs, post, post_cs):
    stream = open(name, 'w')
    stream.write('MG\tMG-CS\tPG\tPG-CS\n')
    for i in range(0, len(post)):
        stream.write('%s\t%s\t%s\t%s\n' %(mongo[i], mongo_cs[i],
            post[i], post_cs[i]))
    stream.close()

def output_4(name, mongo, post, post_or):
    stream = open(name, 'w')
    stream.write('MG\tPG\tPG-OR\n')
    for i in range(0, len(post)):
        stream.write('%s\t%s\t%s\n' %(mongo[i], post[i], post_or[i]))
    stream.close()

def get_email(rep):
    print 'get_email'
    post = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = DB_STORE.get_email(TABLE, '3D97B04F.7090405@terra.com.br')
        post.append(time.time() - t0)
    for i in range(0,rep):
        t0 = time.time()
        res_mg = MG_STORE.get_email(TABLE, '3D97B04F.7090405@terra.com.br')
        mongo.append(time.time() - t0)
    output('get_email', post, mongo)
    if res_mg['Subject'] != res_pg.subject and res_mg['Date'] != res_pg.date:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s\n' % res_pg

def get_archives_range(rep):
    print 'get_archives_range'
    post = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = len(DB_STORE.get_archives(TABLE, START, END))
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = len(MG_STORE.get_archives(TABLE, START, END))
        mongo.append(time.time() - t0)
    output('get_archives_range', post, mongo)
    if res_mg != res_pg:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s\n' % res_pg

def first_email_in_archives_range(rep):
    print 'first_email_in_archives_range'
    post = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = DB_STORE.get_archives(TABLE, START, END)[0]
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = MG_STORE.get_archives(TABLE, START, END)[0]
        mongo.append(time.time() - t0)
    output('first_email_in_archives_range', post, mongo)
    if res_mg['Subject'] != res_pg.subject and res_mg['Date'] != res_pg.date:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s\n' % res_pg

def get_thread_length(rep):
    print 'get_thread_length'
    post = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = DB_STORE.get_thread_length(TABLE,
            '4FCWUV6BCP3A5PASNFX6L5JOAE4GJ7F2')
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = MG_STORE.get_thread_length(TABLE,
            '4FCWUV6BCP3A5PASNFX6L5JOAE4GJ7F2')
        mongo.append(time.time() - t0)
    output('get_thread_length', post, mongo)
    if res_mg != res_pg:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s\n' % res_pg

def get_thread_participants(rep):
    print 'get_thread_participants'
    post = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = len(DB_STORE.get_thread_participants(TABLE,
            '4FCWUV6BCP3A5PASNFX6L5JOAE4GJ7F2'))
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = len(MG_STORE.get_thread_participants(TABLE,
            '4FCWUV6BCP3A5PASNFX6L5JOAE4GJ7F2'))
        mongo.append(time.time() - t0)
    output('get_thread_participants', post, mongo)
    if res_mg != res_pg:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s\n' % res_pg

def get_archives_length(rep):
    print 'get_archives_length'
    post = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = DB_STORE.get_archives_length(TABLE)
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = MG_STORE.get_archives_length(TABLE)
        mongo.append(time.time() - t0)
    output('get_archives_length', post, mongo)
    if res_mg != res_pg:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s\n' % res_pg

def search_subject(rep):
    print 'search_subject'
    post = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = len(DB_STORE.search_subject(TABLE, 'rawhid'))
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = len(MG_STORE.search_subject(TABLE, 'rawhid'))
        mongo.append(time.time() - t0)
    output('search_subject', post, mongo)
    if res_mg != res_pg:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s\n' % res_pg

def search_subject_cs(rep):
    print 'search_subject_cs'
    post_cs = []
    mongo_cs = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg_cs = len(DB_STORE.search_subject_cs(TABLE, 'rawhid'))
        post_cs.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg_cs = len(MG_STORE.search_subject_cs(TABLE, 'rawhid'))
        mongo_cs.append(time.time() - t0)
    output('search_subject_cs', post_cs, mongo_cs)
    if res_mg_cs != res_pg_cs:
        print '** Results differs'
        print 'MG-CS: %s' % res_mg_cs
        print 'PG-CS: %s\n' % res_pg_cs

def search_content(rep):
    print 'search_content'
    post = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = len(DB_STORE.search_content(TABLE, 'rawhid'))
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = len(MG_STORE.search_content(TABLE, 'rawhid'))
        mongo.append(time.time() - t0)
    output('search_content', post, mongo)
    if res_mg != res_pg:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s\n' % res_pg

def search_content_cs(rep):
    print 'search_content_cs'
    post_cs = []
    mongo_cs = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg_cs = len(DB_STORE.search_content_cs(TABLE, 'rawhid'))
        post_cs.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg_cs = len(MG_STORE.search_content_cs(TABLE, 'rawhid'))
        mongo_cs.append(time.time() - t0)
    output('search_content_cs', post_cs, mongo_cs)
    if res_mg_cs != res_pg_cs:
        print '** Results differs'
        print 'MG-CS: %s' % res_mg_cs
        print 'PG-CS: %s\n' % res_pg_cs

def search_content_subject(rep):
    print 'search_content_subject'
    post = []
    post_or = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = len( DB_STORE.search_content_subject(TABLE, 'rawhid'))
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_pg_or = len( DB_STORE.search_content_subject_or(TABLE, 'rawhid'))
        post_or.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = len( MG_STORE.search_content_subject(TABLE, 'rawhid'))
        mongo.append(time.time() - t0)
    output_4('search_content_subject', mongo, post, post_or)
    if res_mg != res_pg or res_mg != res_pg_or:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s' % res_pg
        print 'PG-OR: %s\n' % res_pg_or

def search_content_subject_cs(rep):
    print 'search_content_subject_cs'
    post_cs = []
    post_or_cs = []
    mongo_cs = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg_cs = len( DB_STORE.search_content_subject_cs(TABLE, 'rawhid'))
        post_cs.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_pg_or_cs = len( DB_STORE.search_content_subject_or_cs(TABLE, 'rawhid'))
        post_or_cs.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg_cs = len( MG_STORE.search_content_subject_cs(TABLE, 'rawhid'))
        mongo_cs.append(time.time() - t0)
    output_4('search_content_subject_cs', mongo_cs, post_cs, post_or_cs)
    if res_mg_cs != res_pg_cs or res_mg_cs != res_pg_or_cs:
        print '** Results differs'
        print 'MG-CS: %s' % res_mg_cs
        print 'PG-CS: %s' % res_pg_cs
        print 'PG-OR-CS: %s\n' % res_pg_or_cs

def search_sender(rep):
    print 'search_sender'
    post = []
    post_or = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = len( DB_STORE.search_sender(TABLE, 'rawhid'))
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_pg_or = len( DB_STORE.search_sender_or(TABLE, 'rawhid'))
        post_or.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = len( MG_STORE.search_sender(TABLE, 'rawhid'))
        mongo.append(time.time() - t0)
    output_4('search_sender', mongo, post, post_or)
    if res_mg != res_pg or res_mg != res_pg_or:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s' % res_pg
        print 'PG-OR: %s\n' % res_pg_or

def search_sender_cs(rep):
    print 'search_sender_cs'
    post_cs = []
    post_or_cs = []
    mongo_cs = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg_cs = len( DB_STORE.search_sender_cs(TABLE, 'rawhid'))
        post_cs.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_pg_or_cs = len( DB_STORE.search_sender_or_cs(TABLE, 'rawhid'))
        post_or_cs.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg_cs = len( MG_STORE.search_sender_cs(TABLE, 'rawhid'))
        mongo_cs.append(time.time() - t0)
    output_4('search_sender_cs', mongo_cs, post_cs, post_or_cs)
    if res_mg_cs != res_pg_cs or res_mg_cs != res_pg_or_cs:
        print '** Results differs'
        print 'MG-CS: %s' % res_mg_cs
        print 'PG-CS: %s' % res_pg_cs
        print 'PG-OR-CS: %s\n' % res_pg_or_cs

def get_list_size(rep):
    print 'get_list_size'
    post = []
    mongo = []
    for i in range(0, rep):
        t0 = time.time()
        res_pg = res_pg = DB_STORE.get_list_size(TABLE)
        post.append(time.time() - t0)
    for i in range(0, rep):
        t0 = time.time()
        res_mg = MG_STORE.get_list_size(TABLE)
        mongo.append(time.time() - t0)
    output('get_list_size', post, mongo)
    if res_mg != res_pg:
        print '** Results differs'
        print 'MG: %s' % res_mg
        print 'PG: %s\n' % res_pg


if __name__ == '__main__':
    t_start = time.time()
    get_email(REP)
    get_archives_range(REP)
    first_email_in_archives_range(REP)
    get_thread_length(REP)
    get_thread_participants(REP)
    get_archives_length(REP)

    search_subject(REP)
    search_subject_cs(REP)
    search_content(REP)
    search_content_cs(REP)
    search_content_subject(REP)
    search_content_subject_cs(REP)
    search_sender(REP)
    search_sender_cs(REP)
    
    get_list_size(REP)
    print "Ran for %s seconds" % (time.time() - t_start)




