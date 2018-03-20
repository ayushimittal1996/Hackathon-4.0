import sqlite3
from PIL import Image
#Open database
conn = sqlite3.connect('database1.db')

c=conn.cursor()
"""
conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')

conn.execute('''CREATE TABLE kart
		(userId INTEGER,
		productId INTEGER,
		FOREIGN KEY(userId) REFERENCES users(userId),
		FOREIGN KEY(productId) REFERENCES products(productId)
		)''')

"""


"""
import sqlite3
from PIL import Image

size = 120, 120
file = "/tmp/a.jpg"
imgobj = Image.open(file)
imgobj.thumbnail(size)

con = sqlite3.connect("/tmp/imagesdb")
cur = con.cursor()
cur.execute("create table img (x blob)")
cur.execute("insert into img(x) values(?)", [ buffer(imgobj.tostring()) ] )
con.commit()
cur.close()
con.close()

# read it back.
con = sqlite3.connect("/tmp/imagesdb")
cur = con.cursor()
row = cur.execute('SELECT * FROM img')
for item in row:
    print item
    
"""


pid = [0, 1, 2, 3, 4, 5]
id=[3, 1, 2, 1,0,0]
stock=[4,3,2,3,3,2]
description=["Good to wear","Makes your home even more beautiful","Painted using homemade colours"," Verified and original product","Made with handmade fabric to give a perfect Rajwadi attire", "traditional looking and effective price"]
price=["500","300","700","10000","580","567"]
name = ["Necklace", "Lantern", "Fine-arts", "Flower Pot","Rajwadi kurta","Indian wear"]
for i in range(len(name)):
    c.execute(''' insert into products (productId,name,price,description,image,stock,categoryId)
                    values(?,?,?,?,?,?,?)''', (pid[i], name[i],price[i],description[i], str(i)+'.jpeg', stock[i], id[i]))

    c.execute(''' select * from products ''')
print(c.fetchall())

c.execute(''' insert into users (userId,password,email ,firstName ,lastName,address1,address2,zipcode ,city,state,country, phone)
                    values(?,?,?,?,?,?,?,?,?,?,?,?)''', (1, "1234","ayushi","Ayushi", "Mittal", "Delhi", "Panipat","132103","Panipat","Haryana","India","768456343"))
id = [0, 1, 2, 3]
name = ["Clothes", "Home Decor", "Paintings", "Jewellery"]
for i in range(len(name)):
    print("hi")
    c.execute(''' insert into categories (categoryId,name)
                    values(?,?)''', (id[i], name[i]))
#c.execute(''' select * from categories''')
result = c.fetchall()
#print(result[2])

print ("done")


conn.commit()
conn.close()

