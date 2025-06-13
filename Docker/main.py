from flask import Flask

# Initialize WSGI app
app = Flask(__name__)

# Define route
@app.route('/')
def root():
    return "Welcome, MotherFucker"  

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
