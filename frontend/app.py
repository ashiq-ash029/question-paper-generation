from flask import Flask, request, jsonify, render_template,request
import mysql.connector
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="aqpj"
)
mycursor = mydb.cursor()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/sign')
def sign():
    return render_template('signup.html')

@app.route('/submit', methods=['POST','GET'])
def submit():
    name=request.form.get('name')
    gmail = request.form.get('gmail')
    password = request.form.get('password')
    query='insert into auth (name,gmail,password) VALUES(%s,%s,%s)'
    val=(name,gmail,password)
    mycursor.execute(query,val)
    mydb.commit()
    return render_template('test.html')

@app.route('/loginsubmit',methods=['POST','GET'])
def loginsub():
    user=request.form.get('username')
    password=request.form.get('password')
    query='select password from auth where gmail=%s'
    val=(user,)
    mycursor.execute(query,val)
    results = mycursor.fetchall()
    if (results[0][0]==password):
        return render_template('test.html')
    return render_template('index.html',msg="password is incorrect")

def qgen(context):
    model_name = "valhalla/t5-small-e2e-qg"
    tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    use_fast=False
)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    input_text = f"generate questions: {context}"
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

    output = model.generate(
        input_ids,
        max_length=64,
        num_beams=8,
        num_return_sequences=8,
        do_sample=True,
        early_stopping=True
    )
    questions=tokenizer.decode(output[0], skip_special_tokens=True)
    questions=questions.split("<sep>")
    return questions


@app.route('/generate', methods=['POST'])
def generate_questions():
    context = request.form['context']
    questions = qgen(context)
    return render_template('test.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)
