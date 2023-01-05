from flask import Flask,render_template,redirect, url_for, request
app=Flask(__name__)



@app.route("/calculate")
def calculate():
    return render_template("calculate.html")
    
@app.route("/result",methods = ['POST', 'GET'])
def result():
    print("Hoş geldin")
    if request.method=="POST":
        numberx=request.form['numberx']
        numbery=request.form.get('numbery')
        result=int(numberx)+int(numbery)
        print(result)
        return render_template("result.html",result=result)   
    elif(request.method=="GET"):
        print("elif blok çalıştı query string"+request.method)  
        print(request.query_string)  
        print(request.args['numberx'])
        numberx=request.args.get('numberx')
        numbery=request.args.get('numbery')
        result=int(numberx)+int(numbery)
        return render_template("result.html",result=result)
    else:
        print("else blok çalıştı"+request.method)
        return render_template("calculate.html")
    

@app.route("/")
def index():
    message="message"
    numbers=[1,2,34,56,78,3]
    number1=10
    number2=20
    list2=[number1,number2]
    def hello():
        return "hello function"
    return render_template('index.html',list2=list2,numbers=numbers,message=message,hello=hello)
#send to delete page with params
@app.route("/delete3")
def delete3():
    id=request.args.get('numberx')
    x="delete"+"/"+id
    return redirect(x)

@app.route("/delete/<int:id>")
def delete(id):
    id=str(id)
    return "delete  :"+id #dont use integer only send string

@app.route("/delete2/<string:id>/<string:id2>")# double string
def delete2(id,id2):
    return "<h1>delete2 :</h1>"+id+" "+id2

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/search")
def search():
    return "<h1>SEARH PAGE</h1>"

if __name__=="__main__":
    app.run(debug=True)