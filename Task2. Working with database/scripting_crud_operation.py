import mysql.connector

# ------ CONNECT TO MY LOCAL MYSQL DATABASE ---------
db_connection = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="library_management"
)


cursor = db_connection.cursor()


# CREATE  ----- ADDING NEW AUTHORS ------
def add_author(authors_name):
	query = "INSERT INTO authors (author_name) VALUES (%s)"
	values = [(author,) for author in authors_name]
	cursor.executemany(query, values)
	db_connection.commit()
	return cursor.lastrowid


# CREATE ----- ADDING NEW GENRES ------
def add_genre(genres_name):
	query = "INSERT INTO genres (genre_name) VALUES (%s)"
	values = [(genre,) for genre in genres_name]
	cursor.executemany(query, values)
	db_connection.commit()
	return cursor.lastrowid


# CREATE ----- ADDING NEW BOOKS ------
def add_book(list_of_books):
	query = "INSERT INTO books (title, author_id, genre_id) VALUES (%s, %s, %s)"
	values = list_of_books
	cursor.executemany(query, values)
	db_connection.commit()
	return cursor.lastrowid


# CREATE ----- ADDING NEW PATRONS ------
def add_patron(patrons_name):
	query = "INSERT INTO patrons (patron_name) VALUES (%s)"
	values = [(patron,) for patron in patrons_name]
	cursor.executemany(query, values)
	db_connection.commit()
	return cursor.lastrowid


# READ ----- RETREIVE ALL BOOKS ------
def get_all_books():
	query = "SELECT books.book_id, books.title, authors.author_name, genres.genre_name FROM books \
             INNER JOIN authors ON books.author_id = authors.author_id \
             INNER JOIN genres ON books.genre_id = genres.genre_id"
	cursor.execute(query)
	all_books = cursor.fetchall()
	return all_books


# UPDATE ----- UPDATING BOOK BY BOOK ID ------
def update_book(book_id, new_title, new_author_id, new_genre_id):
	query = "UPDATE books SET title = %s, author_id = %s, genre_id = %s WHERE book_id = %s"
	values = (new_title, new_author_id, new_genre_id, book_id)
	cursor.execute(query, values)
	db_connection.commit()


# DELETE ----- DELETING BOOK BY BOOK ID ------
def delete_book(book_id):
	query = "DELETE FROM books WHERE book_id = %s"
	cursor.execute(query, (book_id,))
	db_connection.commit()



authors_list = ["David Smith", "Harry kane", "Robertson ", "Sam Curran"]
genre_list = ["Literary Fiction", "Science Fiction", "Historical Fiction ", "Mystery"]
patrons_list = ["Tom", "Jerry", "Alex ", "Peter"]
books_list = [('Programming Language', 1, 1), ('Sharloks Homes', 2, 2), ('World War', 3, 3), ('Amazon', 4, 4)]

author_id = add_author(authors_list)
genre_id = add_genre(genre_list)
book_id = add_book(books_list)
patron_id = add_patron(patrons_list)

print("All Books:")
books = get_all_books()
for book in books:
	print(f"Book ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}")

update_book(2, "Python", 1, 3)
delete_book(4)

# Close the database connection
cursor.close()
db_connection.close()
