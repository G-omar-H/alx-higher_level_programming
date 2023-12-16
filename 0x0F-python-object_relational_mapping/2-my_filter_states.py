#!/usr/bin/python3
"""script that lists all states with a name starting\
    with N (upper N) from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT id, name FROM states WHERE
                name = '%s' ORDER BY id ASC""" % sys.argv[4])
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
