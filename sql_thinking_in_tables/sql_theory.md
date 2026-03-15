1. Explain why databases are important in real-world AI systems. Mention examples of the types of data typically stored in databases and why structured storage is necessary.

Databases are important in real world AI systems to store data which will be used by AI systems for new data generation and prediction. They depend on large amounts of reliable, organized, and continuously updated data.
In practical applications of Artificial Intelligence, databases are used to store different types of information such as user data (profiles, preferences, browsing history), transaction data (purchases, timestamps, payment records), multimedia data (images, videos, audio), sensor or IoT data (temperature, location, health signals), and text data (reviews, emails, chatbot conversations). Structured storage is necessary because it ensures data consistency, removes duplication, maintains relationships between different data entities, and enables fast querying and retrieval during model training and real-time decision making. It also supports scalability, security, and integration of data from multiple sources, which helps AI systems perform efficiently and reliably in areas like recommendation systems, fraud detection, healthcare monitoring, and autonomous vehicles.

2. Describe the relational database mental model. Explain what tables, rows, and columns represent, and why each table should represent a single entity.

Relational databases are those databases where the data is stored in the form of structured tables known as Schema.
Tables:- It reperesents a combination of rows and columns whre data is stored in database. It makes our data structured and well formatted. Storing data in tables is a very clean way to work with data. In this many tables can be related to each other using keys.
Columns:- These are vertical lines which store fields of the table.
Rows:- These are horizontal lines which store records in the table. The record of each and every entity is tored in rows for different fields.

3. Explain the concept of a primary key. Describe why primary keys must be unique and non-null, and how they help identify records in a table.

Primary key is a field (or combination of fields) in a database table that uniquely identifies each record 📊.

It must be unique so that no two rows have the same value, which helps avoid confusion and duplication of data.

It must be non-null because every record must have an identifier; if the value is missing, the record cannot be properly recognized.

Primary keys help in fast searching, updating, and deleting specific records in a table.

They also help in creating relationships between tables (through foreign keys), which keeps the database structured and organized.

4. Explain what a database schema is. Describe what information a schema defines and why schemas are important for maintaining consistent data structure.

A database schema represents the structure of database by defining its table. It is typically the design of a database. It defines the fields(i.e. columns) of the table. It specifies information such as table names, column names, data types, primary keys, foreign keys, and relationships between different tables. 
The schema also defines constraints and rules (like uniqueness, default values, and data limits) to ensure correct data entry.Schemas are important because they help maintain a consistent and well-structured data format, making it easier to store, retrieve, and manage data efficiently.They also improve data integrity, reduce errors, and support smooth communication between database systems and applications.

5. Explain how relationships between tables work in relational databases. Describe the role of foreign keys and how tables such as users and orders can be connected.

In relational databases, relationships between tables are created to connect related data stored in different tables.
These relationships are usually formed using a primary key in one table and a foreign key in another table, which helps link matching records.There are common types of relationships such as one-to-one (one record in a table is linked to one record in another), one-to-many (one record is linked to multiple records), and many-to-many (multiple records are linked through a separate junction table).
Relationships help in reducing data duplication, improving data organization, and making queries more meaningful and efficient.They also ensure data integrity and consistency, so that related information remains accurate across the database.

Suppose there is a column named used_id in table users where all records of user_id are described as primary key for users table. Also there is another table named as orders where the same column name use_id will be present. Then in orders table user_id will be described as foreign key. Hence a column with primary is present as foreign key in another table. A foreign key establishes relationship between two tables using their common columns.