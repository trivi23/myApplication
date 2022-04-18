import sqlite3
connect = sqlite3.connect('my.db')
crsr = connect.cursor()
crsr.execute("""select * from company""")
a = crsr.fetchall()
crsr.execute("""select * from marks""")
b = crsr.fetchall()
crsr.execute("""select * from student""")
c = crsr.fetchall()
print(c)
g = [" ", c[0][0], c[0][4], b[0][2], b[0][4], b[0][6], b[0][8], b[0][10]]
print(g)
#print(d[0][0]+" "+d[0][1])
connect.close()
