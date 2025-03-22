import streamlit as st
class Library:
    def RegisterAdmin(A_Id, AdminName):
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
        
library = Library()