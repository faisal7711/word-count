import streamlit as st
st.title("Welcome to word conut")

my_file = st.file_uploader("Upload your .txt file here", type=["txt"])

file_content = ""
if my_file:
    file_content = my_file.read().decode("utf-8")

with st.expander("File content"):
    st.write(file_content)

words = file_content.lower().split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

with st.expander("Word count"):
    st.write(word_count)


st.write("Top 5 Words")
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_words[:5]:
    st.write(f"{word}: {count}")

