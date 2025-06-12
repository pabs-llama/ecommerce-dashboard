import pandas as pd

def safe_append_to_sql(df, table_name, conn, key_column):
    """
    Appends only new rows to a SQL table by checking against existing primary keys.

    Parameters:
        df (DataFrame): DataFrame to insert
        table_name (str): Name of the target SQL table
        conn (sqlite3.Connection): SQLite database connection
        key_column (str): Name of the primary key column
    """
    try:
        # Load existing primary key values from the SQL table
        existing_keys = pd.read_sql(f"SELECT {key_column} FROM {table_name}", conn)[key_column]

        # Filter the DataFrame to only rows with new keys
        new_rows = df[~df[key_column].isin(existing_keys)]

        # Append only new rows
        new_rows.to_sql(table_name, conn, if_exists='append', index=False)

        print(f"✅ Inserted {len(new_rows)} new rows into '{table_name}'.")
    
    except Exception as e:
        print(f"❌ Error appending to '{table_name}': {e}")


