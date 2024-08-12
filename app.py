from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)
from flask_cors import CORS

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API Documentation"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
CORS(app)
# In-memory storage for processed data
data_storage = {}

# Mock data simulating data fetched from an external service like Shopify
mock_data = [
    {"id": 1, "name": "Product A", "price": 100},
    {"id": 2, "name": "Product B", "price": 150},
    {"id": 3, "name": "Product C", "price": 200}
]

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    """
    Simulates fetching data from an external service
    """
    return jsonify(mock_data)

@app.route('/process-data', methods=['POST'])
def process_data():
    """
    Processes the fetched data and stores it in memory
    """
    data = request.get_json()
    processed_data = []
    
    for item in data:
        processed_item = {
            "id": item["id"],
            "name": item["name"].upper(),  # Convert name to uppercase
            "price": item["price"]
        }
        processed_data.append(processed_item)
    
    global data_storage
    data_storage = processed_data
    
    return jsonify({"message": "Data processed and stored successfully"}), 200

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    """
    Returns the processed data stored in memory
    """
    return jsonify(data_storage)

if __name__ == '__main__':
    app.run(debug=True)
