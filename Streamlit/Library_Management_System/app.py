import streamlit as st
import Library


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
st.session_state.setdefault("AdminRegistered", False)
st.session_state.setdefault("Books", {})  
st.session_state.setdefault("Members", {})
st.session_state.setdefault("IssuedBooks", {})
st.session_state.setdefault("IssueHistory", {})  


st.title("📚 Library Management System")
Navbar = ["Register Admin", "Add Book", "Register Member", "Issue Book", "Return Book", "ShowBooks", "SearchBooks", "Show Members", "Issue History"]
choice = st.sidebar.selectbox("",Navbar)

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

elif choice == "ShowBooks":
    st.subheader("📖Books in Library")
    if not st.session_state["Books"]:
        st.warning("NoBooks available!")
    else:
        for B_Id, info in st.session_state["Books"].items():
            status = "✅ Available" if info["available"] else "❌ Issued"
            st.write(f"📌 **{B_Id}**: *{info['title']}* by {info['author']} ({info['category']}) - {status}")

elif choice == "SearchBooks":
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
            
elif choice == "Issue History":
    M_Id = st.text_input("Enter Member ID")
    if st.button("Show History"):
        if M_Id in st.session_state["IssueHistory"] and st.session_state["IssueHistory"][M_Id]:
            for record in st.session_state["IssueHistory"][M_Id]:
                st.write(f"📖 *{record['title']}*")
        else:
            st.warning("⚠️ No history found.")

st.write("👨‍💻 **Designed by Afroz Khan**")
