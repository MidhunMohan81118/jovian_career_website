from flask import Flask,render_template,jsonify
name = "Jack"
app = Flask(__name__,template_folder='template')


JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bengaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi, India',
    'salary':'Rs. 15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
  },
  {
    'id':4,
    'title':'Bankend Engineer',
    'location':'San Fransisco, USA',
    'salary':'$12,00,000'
  }
]

@app.route("/")
def hello_World():
  return "Hello World!"

@app.route("/home")
def home():
  return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)

