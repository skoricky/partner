#!bin/python
# -*- coding: utf-8 -*-

import psycopg2

conn = psycopg2.connect(host='localhost', port='5439', user='postgres', password='postgres', dbname='getdb')

try:
    cursor = conn.cursor()
    cursor.execute("SELECT abonent_id, page_kks, page_no FROM f7952415767822940get.pages WHERE abonent_id = 633 AND page_id::VARCHAR LIKE '199%'")
    f = cursor.fetchall()
    for n in range(0, len(f)):
        for i in range(0, len(f[n])):
            print(f[n][i])

except psycopg2.DatabaseError as Error_test:
    print("no good")

conn.close()

# arr = [1, 2, 3, 4, 5, 1, 1.1]
#
# print(sum((float(arr[i]) for i in range(0, int(len(arr))))))
