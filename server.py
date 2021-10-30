from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "keepitsecret"

@app.route('/')         
def index():
    return render_template("index.html")


@app.route('/amount', methods=['POST'])         
def amount():
    session["strawberry"] = request.form["strawberry"]
    session["raspberry"] = request.form["raspberry"]
    session["apple"] = request.form["apple"]
    session["first_name"] = request.form["first_name"]
    session["last_name"] = request.form["last_name"]
    session["student_id"] = request.form["student_id"]
    return redirect("checkout")

@app.route('/checkout')
def checkout():
    # print("Charging {{session("first_name")}} for fruits")
    return render_template("checkout.html")#,strawberry=session["strawberry"],raspberry=session["raspberry"],apple=session["apple"],first_name=session["first_name"],last_name=session["last_name"],student_id=session["student_id"]

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    