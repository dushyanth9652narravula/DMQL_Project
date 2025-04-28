# app.py

import streamlit as st
import psycopg2
import pandas as pd
import urllib.parse

# Title
st.title("Music Streaming Database 🎵")

st.markdown("Run SQL queries and visualize results!")

# Connect to your Render PostgreSQL database
def get_connection():
    try:
        conn = psycopg2.connect("postgresql://digitalmusicstoreanalysis_c7kr_user:ZY1ux0SCrWWhl94QTKPRVcqWSzUJb9F4@dpg-d07fdq9r0fns738gro70-a.oregon-postgres.render.com/digitalmusicstoreanalysis_c7kr")
        return conn
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return None

conn = get_connection()

# Text box to enter SQL
query = st.text_area("Enter your SQL query:")

# Run query button
if st.button("Execute Query"):
    if conn:
        try:
            df = pd.read_sql_query(query, conn)
            st.success("Query executed successfully!")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error running query: {e}")

# Close the connection
if conn:
    conn.close()
