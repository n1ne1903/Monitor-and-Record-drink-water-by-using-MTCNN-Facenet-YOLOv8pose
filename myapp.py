import streamlit as st
import pandas as pd

# Function to load student data
def load_student_data():
    return pd.read_csv("student_in4.csv")

# Function to load water drinking data
def load_water_data():
    water_data = pd.read_csv("D:\\Documents\\GDSC23\\code\\face_recognition_mtcnn\\MiAI_FaceRecog_3\\output.csv")
    water_data['Time'] = pd.to_datetime(water_data['Time'])  # Convert 'Time' column to datetime
    water_data['Time'] = water_data['Time'].dt.strftime('%m/%d/%Y %H:%M')  # Format 'Time' to remove seconds
    return water_data.groupby(['Time', 'StudentID']).agg({'IsDrinkingWater': 'first'}).reset_index()

# Function to authenticate user
def authenticate(username, password):
    return (username == "admin" and password == "123") or (username == "user1" and password == "123") or (username == "user2" and password == "123")

def main():
    st.title("Student Information System")

    # Load data
    student_data = load_student_data()
    water_data = load_water_data()

    # Check if user is logged in
    is_logged_in = st.session_state.get("is_logged_in", False)
    login_user = None
    
    if not is_logged_in:
        # Display login form
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")

        if login_button:
            if authenticate(username, password):
                st.session_state.is_logged_in = True
                st.session_state.login_user = username  # Store the logged-in user
                st.success("Login successful!")
                is_logged_in = True  # Set is_logged_in to True after successful login

    if is_logged_in:
        login_user = st.session_state.login_user
        
        # Display student information
        st.subheader("List of Students")
        student_columns = ["StudentID", "Name", "Address", "DateOfBirth"]  # Include address and date of birth
        student_info = student_data[student_columns]
        
        # Display buttons for each student
        for _, row in student_info.iterrows():
            student_name = str(row["Name"])  # Convert student name to string
            student_id = row["StudentID"]
        
            button_key = f"button_{student_id}"  # Generate a unique key for each button
            
            # Check if the logged-in user is a parent and the student ID is not "Lam"
            if login_user == "user1" and student_id != "Lam":
                continue  # Skip displaying this student for parents
            if login_user == "user2" and student_id != "2":
                continue

            if st.button(student_name, key=button_key):
                st.subheader("Student Information")
                st.write("Name:", row["Name"])
                st.write("Student ID:", row["StudentID"])
                st.write("Address:", row["Address"])  # Display address
                st.write("Date of Birth:", row["DateOfBirth"])  # Display date of birth
                
                # Filter water data for the selected student
                student_water_data = water_data[water_data["StudentID"] == student_id]
                st.subheader("Water Drinking Times")
                st.write(student_water_data)

if __name__ == "__main__":
    main()
