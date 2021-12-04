import sqlite3

RosterEntries = ("Jean-Baptiste Zorg","Human",122),("Korben Dallas","Meat Popsicle",100), ("Ak'not","Mangalore",-5)

conn = sqlite3.connect(':memory:')
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE if not exists Roster ( \
                Name TEXT,\
                Species TEXT,\
                IQ INTEGER\
                )')
    cur.executemany ('INSERT INTO Roster VALUES (?,?,?)', RosterEntries)
    cur.execute ('UPDATE Roster SET Species=? WHERE Name=? AND IQ=?',('Human','Korben Dallas', 100))
    cur.execute ('SELECT Name, IQ FROM Roster WHERE Species = "Human"')
    
    for row in cur.fetchall():
        print(row)
    conn.commit()
conn.close()
