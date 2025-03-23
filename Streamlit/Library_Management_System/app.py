import streamlit as st


# Custom CSS for the sidebar
st.sidebar.markdown(
    """
    <style>
        h1 {
            font-size: 20px;
            font-weight: bold;
        }
    </style>
    <h1>A K Library</h1>      
    """,
    unsafe_allow_html=True
)
# CSS is copied by AI tools
st.markdown(
    """
    
    <style>

body {
    background-color: #121212;
    color: white;
    font-family: 'Arial', sans-serif;
}

/* Sidebar styling */
.sidebar .sidebar-content {
    background-color: #1e1e1e;
    padding: 20px;
    border-radius: 10px;
}

.sidebar h1 {
    font-size: 24px;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 20px;
}

/* Button styling */
.stButton>button {
    border-radius: 8px;
    padding: 10px 20px;
    font-size: 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    transition: background-color 0.3s ease;
}

.stButton>button:hover {
    background-color: #45a049;
}

.add-button button {
    background-color: green !important;
    color: white;
}

.remove-button button {
    background-color: red !important;
    color: white;
}

/* Metrics container styling */
.metric-container {
    display: flex;
    justify-content: space-around;
    text-align: center;
    font-size: 24px;
    margin-top: 20px;
}

.metric-container div {
    margin: 10px;
    padding: 20px;
    border-radius: 10px;
    background-color: #735853;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.metric-container div:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}

.metric-container h3 {
    font-size: 20px;
    margin-bottom: 10px;
    color: #ffffff;
}

.metric-container p {
    font-size: 28px;
    font-weight: bold;
    color: #ffffff;
}

/* Input fields styling */
.stTextInput>div>div>input {
    background-color: #2d2d2d;
    color: white;
    border-radius: 8px;
    border: 1px solid #444;
    padding: 10px;
}

.stTextInput>div>div>input:focus {
    border-color: #4CAF50;
    box-shadow: 0 0 8px rgba(76, 175, 80, 0.6);
}

/* Select box styling */
.stSelectbox>div>div>select {
    background-color: #2d2d2d;
    color: white;
    border-radius: 8px;
    border: 1px solid #444;
    padding: 10px;
}

.stSelectbox>div>div>select:focus {
    border-color: #4CAF50;
    box-shadow: 0 0 8px rgba(76, 175, 80, 0.6);
}

/* Success and error messages styling */
.stAlert {
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 20px;
}

.stAlert.success {
    background-color: #4CAF50;
    color: white;
}

.stAlert.error {
    background-color: #f44336;
    color: white;
}
</style>
    
    """,
    unsafe_allow_html=True
)
class Library:
    def RegisterAdmin(A_Id, AdminName):
        # Check if an admin is already registered
        if st.session_state.get("AdminRegistered", False):
            st.error("Only one admin can be registered. An admin already exists!")
            return
        
        # Register the admin
        st.session_state["AdminRegistered"] = True
        st.session_state["Admin"] = {"id": A_Id, "name": AdminName}
        st.success(f"Admin '{AdminName}' Registered successfully!")

    def AddBook(B_Id, title, author, category):
        if not st.session_state["AdminRegistered"]:
            st.error("Admin must be Registered first to AddBooks!")
            return
        st.session_state["Books"][B_Id] = {
            "title": title, "author": author, "category": category, "available": True
        }
        st.success(f"Book '{title}' added successfully!")

    def RegisterMember(M_Id, name):
        st.session_state["Members"][M_Id] = name
        st.session_state["IssueHistory"][M_Id] = []
        st.success(f"Member '{name}' Registered successfully!")

    def Issue_Book(B_Id, M_Id):
        if M_Id not in st.session_state["Members"]:
            st.error("User must be Registered to Issue a Book!")
            return
        if B_Id in st.session_state["Books"] and st.session_state["Books"][B_Id]["available"]:
            st.session_state["Books"][B_Id]["available"] = False
        
            st.session_state["IssuedBooks"][B_Id] = {"M_Id": M_Id}  # ❌ Due date removed
            st.session_state["IssueHistory"][M_Id].append({
                "B_Id": B_Id, "title": st.session_state["Books"][B_Id]["title"]
            })
            st.success(f"Book Issued to {st.session_state['Members'][M_Id]}")
        else:
            st.error("Book is not available or invalid Book ID!")

    def return_Book(B_Id):
        if B_Id in st.session_state["IssuedBooks"]:
            del st.session_state["IssuedBooks"][B_Id]
            st.session_state["Books"][B_Id]["available"] = True
            st.success(f"Book returned successfully! ")
        else:
            st.error("Invalid Book ID or Book was not Issued!")

    def searchBooks(query):
        return [
            Book for Book in st.session_state["Books"].values()
            if query.lower() in Book["title"].lower() or query.lower() in Book["author"].lower()
        ]
        

st.session_state.setdefault("AdminRegistered", False)
st.session_state.setdefault("Books", {})  
st.session_state.setdefault("Members", {})
st.session_state.setdefault("IssuedBooks", {})
st.session_state.setdefault("IssueHistory", {})  


st.title("📚 Library Management System")
Navbar = ["Register Admin", "Add Book", "Register Member", "Issue Book", "Return Book", "Show Books", "Search Books", "Show Members", "Issue History","Statistics"]
choice = st.sidebar.selectbox("",Navbar)

library = Library()
if choice == "Register Admin":
    A_Id = st.text_input("Enter Admin ID")
    AdminName = st.text_input("Enter Admin Name")
    if st.button("Register Admin"):
        Library.RegisterAdmin(A_Id, AdminName)

elif choice == "Add Book":
    B_Id = st.text_input("Enter Book ID")
    title = st.text_input("Enter Book Title")
    author = st.text_input("Enter Author Name")
    categories = ["Fiction", "Science", "History", "Technology", "Philosophy", "Mathematics"]
    category = st.selectbox("Select Category", categories)
    if st.button("Add Book"):
        Library.AddBook(B_Id, title, author, category)

elif choice == "Register Member":
    M_Id = st.text_input("Enter Member ID")
    name = st.text_input("Enter Member Name")
    if st.button("Register Member"):
        Library.RegisterMember(M_Id, name)

elif choice == "Issue Book":
    B_Id = st.text_input("Enter Book ID")
    M_Id = st.text_input("Enter Member ID")
    if st.button("Issue Book"):
        Library.Issue_Book(B_Id, M_Id)

elif choice == "Return Book":
    B_Id = st.text_input("Enter Book ID")
    if st.button("Return Book"):
        Library.return_Book(B_Id)

elif choice == "Show Books":
    st.subheader("📖Books in Library")
    if not st.session_state["Books"]:
        st.warning("NoBooks available!")
    else:
        for B_Id, info in st.session_state["Books"].items():
            status = "✅ Available" if info["available"] else "❌ Issued"
            st.write(f"📌 **{B_Id}**: *{info['title']}* by {info['author']} ({info['category']}) - {status}")

elif choice == "Search Books":
    query = st.text_input("🔍 Enter Book title or author name")
    if st.button("Search"):
        results = Library.searchBooks(query)
        if results:
            for Book in results:
                st.write(f"📖 *{Book['title']}* by {Book['author']} ({Book['category']})")
        else:
            st.warning("⚠️ No matchingBooks found.")

elif choice == "Show Members":
    st.subheader("👥 Library Members")
    if not st.session_state["Members"]:
        st.warning("No Members Registered!")
    else:
        for M_Id, name in st.session_state["Members"].items():
            st.write(f"🆔 **{M_Id}**: {name}")
elif choice == "Statistics":
    st.subheader("📊 Library Statistics")
    total_books = len(st.session_state["Books"])
    issued_books = len(st.session_state["IssuedBooks"])
    total_members = len(st.session_state["Members"])
    
    st.markdown(
        f"""
        <div class='metric-container'>
            <div><h3>Total Books</h3><p>{total_books}</p></div>
            <div><h3>Issued Books</h3><p>{issued_books}</p></div>
            <div><h3>Registered Members</h3><p>{total_members}</p></div>
        </div>
        """,
        unsafe_allow_html=True
    )
elif choice == "Issue History":
    M_Id = st.text_input("Enter Member ID")
    if st.button("Show History"):
        if M_Id in st.session_state["IssueHistory"] and st.session_state["IssueHistory"][M_Id]:
            for record in st.session_state["IssueHistory"][M_Id]:
                st.write(f"📖 *{record['title']}*")
        else:
            st.warning("⚠️ No history found.")
elif choice == "Statistics":
    st.subheader("📊 Library Statistics")
    total_books = len(st.session_state["Books"])
    issued_books = len(st.session_state["IssuedBooks"])
    total_members = len(st.session_state["Members"])
    
    st.metric("Total Books", total_books)
    st.metric("Issued Books", issued_books)
    st.metric("Registered Members", total_members)
    

st.write("👨‍💻 Designed by Afroz Khan")
