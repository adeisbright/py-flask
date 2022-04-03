from flask import Flask ,jsonify,request 


from products import Product

app = Flask(__name__) 

product = Product() 

@app.route("/" , methods = ["GET"]) 
def get_home():
    product.add_product("Biscuit" , 30 , 500) 
    product.add_product("Biscuit" , 30 , 500) 
    print(product.show_products())
    return "Welcome to the Home Page" 

@app.route("/books" , methods=["GET" , "POST"]) 

def handle_books():
    if request.method == "GET" : 
        name = request.args.get("name")
        item_filter = request.args.get("filter")
        print(name , item_filter)
        
        return jsonify({
            "status" : "OK" , 
            "data" : [
                {
                    "title"  :"Bread" , 
                    "id" : 1 , 
                    "amount" : 400,
                    "quanity" : 50
                }
            ]
            }),200
    elif request.method == "POST" :
        # reqBody = request.get_json() 
        # title = reqBody["title"]
        # amount = reqBody["amount"]
        # quantity = reqBody["quantity"]

        # print(reqBody , title)
        title = request.form.get("name")
       
        # return jsonify({
        #     "title" : title,
        #     "amount" : amount , 
        #     "quantity" : quantity
        # }),201
        return jsonify({"title" : title}) , 201

@app.route("/products" , methods = ["GET" , "POST"])
def handle_products():
    if request.method == "GET":
        products = product.show_products() 
        print(products)
        return jsonify(products) , 200
    else:
        product_data = request.get_json() 
        title = product_data["title"] 
        amount = product_data["amount"] 
        quantity = product_data["quantity"]
        product.add_product(title,quantity , amount)
        return jsonify({
            "message" : "Product added successfully" , 
            "status" : 201 , 
            "data" : {
                "title" : title , 
                "amount" : amount , 
                "quantity" : quantity
            }
        }) , 201

@app.route("/products/<int:id>" , methods = ["GET" , "PUT" , "DELETE"])
def handle_single_products(id):
    if request.method == "GET":
        target_product = product.find_product(id)
        return jsonify(target_product) , 200
    elif request.method == "PUT":
        product_data = request.get_json() 
        title = product_data["title"] 
        amount = product_data["amount"] 
        quantity = product_data["quantity"]
        product.update_product(id , 
            {
                "title" : title , 
                "amount" : amount , 
                "quantity" : quantity
            }
        )
        return jsonify({
            "message" : "Product added successfully" , 
            "status" : 200 , 
            "data" : {
                "title" : title , 
                "amount" : amount , 
                "quantity" : quantity
            }
        }) , 200
    elif request.method == "DELETE" :
        result = product.remove_product(id)
        return jsonify(result) ,200

@app.route("/upload" , methods=["GET" , "POST"]) 
def handle_upload():
    if request.method == "GET":
        return """<html>
                    <body>
                    <form action = "http://localhost:3500/upload" method = "POST" enctype = "multipart/form-data">
                        <input type = "file" name = "file" />
                        <input type = "submit"/>
                        </form>   
                    </body>
                </html>"""
    elif request.method == "POST":
        f = request.files["file"]
        f.save(f.filename)
        return "file Uploaded successfully"

if __name__ == "__main__" :
    app.run(host="127.0.0.1" , port=3500 , debug=True) 

