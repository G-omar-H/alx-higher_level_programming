#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.name FROM cities c\
                JOIN states s\
                ON c.state_id = s.id\
                WHERE s.name = %(match)s\
                ORDER BY c.id ASC", {'match': sys.argv[4]})
    print(", ".join([row[0] for row in cur.fetchall()]))
    cur.close()
    db.close()
