
class Product:
    """
        A Hypothetical database for storing product information 
        Attributes 
        ---------- 
            products : a list of products 
            count: The current count of products 
        Methods:
        ------- 
            add_product() 
            show_products()
            find_product()
            update_product()
            remove_product()
    """
    products = [] 
    count = 0 

    def add_product(self , title , quantity , price):
        if (len(Product.products) > 0 ):
            for product in Product.products:
                if(product["title"] == title):
                    product["quantity"] += quantity 
                    if (price > product["price"]) :
                        product["price"] = price 
                    return 

            Product.count += 1
            product = {
                "title" : title , 
                "quantity" : quantity , 
                "price" : price ,
                "id" : Product.count 
            }

            Product.products.append(product)
        else : 
            Product.count += 1
            product = {
                "title" : title , 
                "quantity" : quantity , 
                "price" : price  , 
                "id" : Product.count 
            }
            Product.products.append(product)

    def show_products(self):
        if(len(Product.products) == 0):
            return "No Product to display" 
        else :
            return Product.products

    def find_product(self , id):
        """ Searches the catalog for a product whose id is id"""
        for product in Product.products:
            if (product["id"] == id):
                result =  {
                    "product" : product 
                }
                return result
        return False
   
    def update_product(self , id , body):
        """
            Upates a particular product with the body using 
            the id 

            Parameters
            ---------- 
            id : Number : The id of the product 
            body : Dictionary : New content for the product
        """
        is_product = self.find_product(id) 
        if(is_product):
            return is_product["product"].update(body)
        else:
            return "Invalid Product ID"
        
    def remove_product(self , id) : 
        """ Removes a product whose id is id"""
        is_product = self.find_product(id) 
        if (is_product) :
            Product.products.pop(is_product["index"])
            return "Product was removed"
        else:
            return "Invalid Product ID"

if __name__ == "__main__":
    catalog = Product() 
    catalog.show_products()
    catalog.add_product("Book" , 45 , 100)
    catalog.add_product("Pen" , 10 , 50) 

    catalog.add_product("Book" , 300 , 190) 
    catalog.add_product("Car" , 200 , 500000)

    #catalog.show_products()

    product = catalog.find_product(7) 
    print("---Searching for a Product by Id--")
    print("The product is:\n\n" , product , "\n\n")
    catalog.update_product(3, 
    {"title" : "Example" , "quantity" : 40 , "price" : 4})
    catalog.remove_product(2)

    print("After Deleting removing a particular item")

    catalog.show_products()