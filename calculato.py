from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/") 
def cal_page():# this is used to display the calculator page
    return render_template("index1.html")


@app.route("/math",methods=["POST"]) # "/math" is what is mentioned in the html code
def calculator_test():
    ops=request.form["operation"]
    first_num= request.form["num1"] # this is what is mentioned in the html code,<form action="/math" method="POST">
    second_num= request.form["num2"]

    if(ops=="add"):
        r=int(first_num) + int(second_num)
        return f"addition of {first_num} and {second_num} is {r}"

    if(ops=="subtract"):
        r=int(first_num) - int(second_num)
        return f"substraction of {first_num} and {second_num} is {r}"

    if(ops=="multiply"):
        r=int(first_num) * int(second_num)
        return f"multiplication of {first_num} and {second_num} is {r}"

    if(ops=="divide"):
        try: # if a zero divison error occurs it will be displayed on the terminal
            r=int(first_num) //int(second_num)
            return f"divison of {first_num} and {second_num} is {r}"
        except Exception as e:
            return e

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=5000)