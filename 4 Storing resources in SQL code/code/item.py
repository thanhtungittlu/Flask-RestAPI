from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found'},404

    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        querry = "SELECT * FROM items WHERE name=? "
        result = cursor.execute(querry,(name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {'item' : {'name' : row[0], 'price': row[1]}}
        

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        
        try:
            self.insert(item)
        except:
            return {'message': "An error occurred inserting the item."},500

        return item,201

    @classmethod
    def insert(cls,item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        querry = "INSERT INTO items VALUES (?,?)"
        cursor.execute(querry,(item['name'], item['price']))

        connection.commit()
        connection.close()

    def delete(self, name):
                
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        querry = "DELETE FROM items WHERE name=?"
        cursor.execute(querry,(name,))

        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}


    @classmethod
    def update(cls,item):

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        querry = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(querry,(item['price'], item['name']))

        connection.commit()
        connection.close()

    def put(self, name):
        data = Item.parser.parse_args()
        # Once again, print something not in the args to verify everything works
        item = self.find_by_name(name)
        update_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                self.insert(update_item)
            except:
                return {'message': 'An error occureed inserting the item.'},500
        else:
            try: 
                self.update(update_item)
            except:
                return {'message': 'An error occureed updating the item.'}
        return update_item

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        item = []
        for row in cursor.execute('SELECT * FROM items'):
            item.append({'name': row[0], 'price':row[1]})
        return {'items': item}
