from sql_connection import get_sql_connection

def get_all_product(connection):
    cursor = connection.cursor()
    query = ("select product.product_id, product.name, product.uom_id, product.price_per_unit, uom.uom_name from product inner join uom on product.uom_id=uom.uom_id")
    cursor.execute(query)
    result = cursor.fetchall()
    response = []
    for data in result:
        response.append({
            'product_id': data[0],
            'name': data[1],
            'uom_id': data[2],
            'price_per_unit': data[3],
            'uom_name': data[4]
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO product "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_products(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_product(connection))
    print(insert_new_product(connection, {
        'product_name': 'potatoes',
        'uom_id': '1',
        'price_per_unit': 10
    }))