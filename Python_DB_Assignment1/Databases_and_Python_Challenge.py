import sqlite3

connection = sqlite3.connect(':memory:')
c = connection.cursor()
c.executescript("""DROP TABLE IF EXISTS Roster;
                CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT);
                INSERT INTO Roster VALUES('Jean-Baptiste Zorg', 'Human', '122');
                """)
peopleValues = (('Korban Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))
c.executemany("INSERT INTO Roster VALUES(?, ?, ?)", peopleValues)
c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
              ('Human', 'Korben Dallas', '100'))
