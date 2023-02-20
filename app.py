from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data/<data>")
def update_data(data):
    print(f"Received data from socket server: {data}")
    return "Data received!"

if __name__ == "__main__":
    app.run()
