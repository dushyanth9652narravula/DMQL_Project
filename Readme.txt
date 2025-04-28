-------------

Project: Digital Music Store Analysis
Description: This project involves simulating a music streaming platform by creating a relational database schema, generating synthetic data using Python, inserting data into PostgreSQL via pgAdmin, and performing SQL-based analytical queries.

-------------------------------------
1. Raw Data Generation (Python + Faker)
-------------------------------------

- We used the `faker` library in Python to generate realistic synthetic data for all tables.
- For each entity (e.g., Customer, Employee, Track), separate Pandas DataFrames were created.
- Manual foreign key relationships were carefully maintained to ensure referential integrity.
- Junction tables (e.g., PlaylistTrack, ArtistTrack) were created based on IDs from parent tables.
- CSV files were saved for each table using `df.to_csv()` with consistent formatting (no index, UTF-8 encoding).

Files created:
  - customer.csv
  - invoice.csv
  - employee.csv
  - track.csv
  - listeninghistory.csv
  - ... (and other relevant tables)

--------------------------
2. Database Creation (pgAdmin)
--------------------------

- A new PostgreSQL database was created via pgAdmin.
- All tables were created using SQL `CREATE TABLE` statements with appropriate primary and foreign keys.
- `SERIAL` was used for auto-incrementing primary keys.
- `ON DELETE CASCADE` and `ON DELETE SET NULL` constraints were added to manage dependencies.
- Each table was created in the correct order to handle foreign key constraints (e.g., Artist → Album → Track).

Example:
```sql
CREATE TABLE Customer (
  CustomerId SERIAL PRIMARY KEY,
  FirstName TEXT,
  LastName TEXT,
  Email TEXT,
  ...
);

-------------------------------
3. Data Insertion (Python + psycopg2 COPY)
-------------------------------

- After generating and exporting all data tables to CSV format, we inserted the data into PostgreSQL using the high-performance `COPY` command via `psycopg2`.

- We used the `copy_expert()` method from the `psycopg2` library to execute SQL-level `COPY` commands, which is significantly faster than row-by-row inserts.