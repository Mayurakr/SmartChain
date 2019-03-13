import argparse
try:
    from . import db_connection
except:
    import db_connection


def add_to_black_list(prod_name, location_lat, location_long,additional_details):
    conn = db_connection.get_connection()
    mycursor = conn.cursor()
    SQL_QUERY = "INSERT INTO spurious_list ( prod_name , location_lat, location_long , additional_details ) VALUES (%s, %s, %s, %s)"
    value = (prod_name, location_lat, location_long,additional_details)
    mycursor.execute(SQL_QUERY, value)
    conn.commit()
    conn.close()

if __name__=='__main__':
    add_to_black_list('crocin',12.88,77.34,'jdhdjkhd')