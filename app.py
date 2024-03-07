from flask import Flask,render_template
name = "Jack"
app = Flask(__name__,template_folder='template')

@app.route("/")
def hello_World():
  return "Hello World!"

@app.route("/home")
def home():
  return render_template('home.html')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
