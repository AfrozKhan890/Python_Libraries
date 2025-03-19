import streamlit as st
import mysql.connector
import os

# Ensure uploads directory exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Database connection function
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Use 'user' instead of 'username'
            password="",  # Add your MySQL password here
            database="python_stream"
        )
        return connection
    except mysql.connector.Error as err:
        st.error(f"Error connecting to MySQL: {err}")
        return None

# Function to add a book
def add_book(title, author, genre_id, status, rating, total_pages, pages_read, isbn, publication_year, publisher, file_path):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        INSERT INTO books (title, author, genre_id, status, rating, total_pages, pages_read, isbn, publication_year, publisher, file_path)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (title, author, genre_id, status, rating, total_pages, pages_read, isbn, publication_year, publisher, file_path))
            connection.commit()
            st.success("Book added successfully!")
        except mysql.connector.Error as err:
            st.error(f"Error adding book: {err}")
        finally:
            cursor.close()
            connection.close()

# Function to search books
def search_books(search_term, search_by):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        if search_by == "Title":
            query = "SELECT * FROM books WHERE title LIKE %s"
        else:
            query = "SELECT * FROM books WHERE author LIKE %s"
        cursor.execute(query, (f"%{search_term}%",))
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results

# Function to set reading goals
def set_reading_goal(user_id, year, target_books, target_pages):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        INSERT INTO reading_goals (user_id, year, target_books, target_pages)
        VALUES (%s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (user_id, year, target_books, target_pages))
            connection.commit()
            st.success("Reading goal saved successfully!")
        except mysql.connector.Error as err:
            st.error(f"Error saving reading goal: {err}")
        finally:
            cursor.close()
            connection.close()

# Function to add to wishlist
def add_to_wishlist(user_id, title, author, priority, notes):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        INSERT INTO wishlist (user_id, title, author, priority, notes)
        VALUES (%s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (user_id, title, author, priority, notes))
            connection.commit()
            st.success("Book added to wishlist!")
        except mysql.connector.Error as err:
            st.error(f"Error adding to wishlist: {err}")
        finally:
            cursor.close()
            connection.close()

# Function to create a collection
def create_collection(user_id, name, description):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        INSERT INTO collections (user_id, name, description)
        VALUES (%s, %s, %s)
        """
        try:
            cursor.execute(query, (user_id, name, description))
            connection.commit()
            st.success("Collection created successfully!")
        except mysql.connector.Error as err:
            st.error(f"Error creating collection: {err}")
        finally:
            cursor.close()
            connection.close()

# Streamlit App
st.sidebar.title("Navigate")
page = st.sidebar.radio("Choose a page", ["Dashboard", "My Library", "Add Book", "Search Books", "Reading Goals", "Wishlist", "Loan Tracker", "Collections", "Import/Export"])

if page == "Dashboard":
    st.title("Library Dashboard")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        
        # Total Books
        cursor.execute("SELECT COUNT(*) FROM books")
        total_books = cursor.fetchone()[0]
        
        # Books Read
        cursor.execute("SELECT COUNT(*) FROM books WHERE status = 'Read'")
        books_read = cursor.fetchone()[0]
        
        # Average Rating
        cursor.execute("SELECT AVG(rating) FROM books")
        average_rating = cursor.fetchone()[0]
        
        if average_rating is None:
            average_rating = 0.0

        # Books/Month (Example calculation)
        books_per_month = books_read / 12  # Assuming 12 months
        
        cursor.close()
        connection.close()
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Books", total_books)
        with col2:
            st.metric("Books Read", books_read)
        with col3:
            st.metric("Average Rating", f"{average_rating:.1f}")
        with col4:
            st.metric("Books/Month", f"{books_per_month:.1f}")
        
        st.write("Recommended Next Reads")
        st.write("Add more books to your library to get personalized recommendations!")

elif page == "My Library":
    st.title("My Library")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        
        for book in books:
            st.write(f"### {book[1]} by {book[2]}")
            st.write(f"**Status**: {book[4]}")
            st.write(f"**Progress**: {book[6]}/{book[5]} pages")
            st.write(f"**Rating**: {book[7]}")
            st.write("---")
        
        cursor.close()
        connection.close()

elif page == "Add Book":
    st.title("Add a New Book")
    title = st.text_input("Title*")
    author = st.text_input("Author*")
    genre_id = st.number_input("Genre ID*", min_value=1)
    status = st.selectbox("Status", ["Reading", "Read", "DNF", "Want to Read", "On Hold", "Re-Reading"])
    rating = st.slider("Rating", 0, 5)
    total_pages = st.number_input("Total Pages*", min_value=1)
    pages_read = st.number_input("Pages Read", min_value=0, max_value=total_pages)
    isbn = st.text_input("ISBN")
    publication_year = st.number_input("Publication Year*", min_value=1750)
    publisher = st.text_input("Publisher")

    # File upload section
    uploaded_file = st.file_uploader("Upload Book File (PDF, EPUB, etc.)", type=["pdf", "epub", "txt"])

    file_path = None
    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File uploaded successfully: {file_path}")

    if st.button("Add Book"):
        add_book(title, author, genre_id, status, rating, total_pages, pages_read, isbn, publication_year, publisher, file_path)

elif page == "Search Books":
    st.title("Search Books")
    search_by = st.selectbox("Search by", ["Title", "Author"])
    search_term = st.text_input("Enter search term")
    if st.button("Search"):
        results = search_books(search_term, search_by)
        for book in results:
            st.write(f"### {book[1]} by {book[2]}")
            st.write(f"**Genre ID**: {book[3]}")
            st.write(f"**Status**: {book[4]}")
            st.write(f"**Rating**: {book[5]}")
            st.write("---")

elif page == "Reading Goals":
    st.title("Reading Goals")
    user_id = st.number_input("User ID*", min_value=1)
    year = st.selectbox("Select Year", [2025, 2026, 2027])
    target_books = st.number_input("Target Number of Books*", min_value=1)
    target_pages = st.number_input("Target Number of Pages*", min_value=1)
    if st.button("Save Goal"):
        set_reading_goal(user_id, year, target_books, target_pages)

elif page == "Wishlist":
    st.title("Book Wishlist")
    st.write("### Add to Wishlist")
    user_id = st.number_input("User ID*", min_value=1)
    wishlist_title = st.text_input("Title*")
    wishlist_author = st.text_input("Author*")
    priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    notes = st.text_area("Notes")
    if st.button("Add to Wishlist"):
        add_to_wishlist(user_id, wishlist_title, wishlist_author, priority, notes)
    
    st.write("### Your Wishlist")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM wishlist")
        wishlist_items = cursor.fetchall()
        for item in wishlist_items:
            st.write(f"#### {item[2]} by {item[3]}")
            st.write(f"**Priority**: {item[4]}")
            st.write(f"**Notes**: {item[5]}")
            st.write("---")
        cursor.close()
        connection.close()

elif page == "Loan Tracker":
    st.title("Book Loan Tracker")
    st.write("### Active Loans")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM loans")
        loans = cursor.fetchall()
        for loan in loans:
            st.write(f"**Book ID**: {loan[1]}")
            st.write(f"**Borrower**: {loan[2]}")
            st.write(f"**Loan Date**: {loan[3]}")
            st.write(f"**Return Date**: {loan[4]}")
            st.write("---")
        cursor.close()
        connection.close()

elif page == "Collections":
    st.title("Book Collections")
    st.write("### Create New Collection")
    user_id = st.number_input("User ID*", min_value=1)
    collection_name = st.text_input("Collection Name*")
    collection_description = st.text_area("Description")
    if st.button("Create Collection"):
        create_collection(user_id, collection_name, collection_description)
    
    st.write("### Your Collections")
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM collections")
        collections = cursor.fetchall()
        for collection in collections:
            st.write(f"#### {collection[2]}")
            st.write(f"**Description**: {collection[3]}")
            st.write("---")
        cursor.close()
        connection.close()

elif page == "Import/Export":
    st.title("Import/Export")
    st.write("Functionality to import/export data will be implemented here.")