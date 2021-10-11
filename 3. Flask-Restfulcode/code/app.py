from flask import Flask,request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app,authenticate, identity)


items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        # for item in items:
        #     if name == item['name']:
        #         return item
        # return  {'item' : None},404
        item = next(filter(lambda x: x['name'] == name, items),None)
        return {'item' : item}, 200 if item else 404
        

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items),None): # nếu tìm được 1 tên trùng thì sẽ True, sau đó đưa ra thông báo tìm dc tên trùng, nếu False thì thêm
            return {"message": "An item with name {} already exists.".format(name)},400 #400 là mã lỗi Bad request

        data = request.get_json()
        item = {'name': name, 'price' : data['price']}
        items.append(item)
        return item, 201
    def delete(self,name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self,name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items),None)
        if item is None:
            item = { 'name':name, 'price' : data['price']}
            items.append(item)
        else:
            item.update(data)
            # itemUpdate = { 'name':data['name'], 'price' : data['price']}
            # item.update(itemUpdate)
        return item,200


class ItemsList(Resource):
    def get(slef):
        return {'items' : items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')



app.run(port = 5000, debug = True)