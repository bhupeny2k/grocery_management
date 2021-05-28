
def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from uom")
    cursor.execute(query)
    result = cursor.fetchall()
    response = []
    for data in result:
        response.append({
            'uom_id': data[0],
            'uom_name': data[1]
        })
    return response


if __name__ == '__main__':
    from .sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))