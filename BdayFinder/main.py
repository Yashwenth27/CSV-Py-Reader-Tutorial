import csv
import streamlit as st
st.set_page_config(layout="wide")
details = []
def read_csv_file(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            reg_no = row[1]
            name = row[2]
            dob = row[3]
            deg = row[4]
            main_dic = {"regno": reg_no, "details": {"name": name, "dob": dob, "deg": deg}}
            details.append(main_dic)
        #print(details)  

# Example usage:
file_path = "../BdayFinder/all_rec.csv"  # Replace 'example.csv' with the path to your CSV file
read_csv_file(file_path)

st.header("Bday 2day!")
st.subheader("Find whose bday is it today!")
st.markdown('''<hr>''',unsafe_allow_html=True)

c1,c2 = st.columns(2)
with c1:
    name = st.text_input("Search By Name: ")
    if st.button("Search!"):
        for i in details:
            if(name.lower() in i["details"]["name"].lower()):
                with st.chat_message("human"):
                    st.subheader(i["details"]["name"])
                    st.write(i["details"]["deg"])
                    st.write(i["regno"])
                    st.write(i["details"]["dob"])
                    if st.button(key=i["details"]["name"],label="Go to PWI."):
                        import webbrowser
                        url = "https://webstream.sastra.edu/sastraparentweb/"
                        webbrowser.open(url)

with c2:
    dt = st.date_input("Choose The Date!")
    if st.button("Find!"):

        dts = str(dt)
        yyyy = dts[0:4]
        mm = dts[5:7]
        dd = dts[8:10]

        #st.write(details)
        print(dd+"-"+mm+"-"+yyyy)
        for i in details:
            if (dd+"-"+mm+"-" in i["details"]["dob"]):
                with st.chat_message("human"):
                    st.subheader(i["details"]["name"])
                    st.write(i["details"]["deg"])
                    st.write(i["regno"])
                    if st.button(key=i["details"]["name"],label="Go to PWI."):
                        import webbrowser
                        url = "https://webstream.sastra.edu/sastraparentweb/"
                        webbrowser.open(url)


