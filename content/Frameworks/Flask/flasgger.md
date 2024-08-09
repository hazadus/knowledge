🔗 [[Flask]]

----
Flasgger is a Flask extension to **extract [OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#operation-object)** from all Flask views registered in your API.

Flasgger also comes with **[SwaggerUI](http://swagger.io/swagger-ui/) embedded** so you can access http://localhost:5000/apidocs and visualize and interact with your API resources.

Usage example: [flask-restx-learn](https://github.com/hazadus/flask-restx-learn/)

---
## Using Flasgger with external YAML files

1. Install as described in [docs](https://github.com/flasgger/flasgger).
2. Init in the app:
	```python
	from flasgger import Swagger

	app = Flask(__name__)
	swagger = Swagger(app)
	```
3. Define API specs in external YAML files, see example in  [flask-restx-learn](https://github.com/hazadus/flask-restx-learn/). Place YAML file in the same directory with endpoint code.
4. Add docstrings to endpoints:
	```python
	@api.route("/")  
	class BookList(Resource):  
	    def get(self):  
	        """  
	        file: books_get_list.yml
	        """
	        return get_all_books_json()
	```
1. API docs are available at `http://127.0.0.1:5000/apidocs/`.

----
