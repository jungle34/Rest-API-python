import mysql.connector

def dbexc(sql):
    conn = mysql.connector.connect(
        host='localhost',
        user='johnny',
        password='20010506jV!',
        database='teste'
    )

    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    results = []
    
    for row in rows:
        row_dict = {}    
        for i in range(len(cursor.description)):
            row_dict[cursor.description[i][0]] = row[i]    
        results.append(row_dict)
    conn.close()

    return results