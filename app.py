from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",img_list=img_list,names=names,scr=scr,uselist=uselist)

scr=int(0)

img_list=[
    True,
    False
]
explain=[
    "hi",
    "other"
]

uselist=["1","2"]

names={
    "1":["AI1","Real1"],
    "2":["AI2","Real2"]
}

def check(choice,x):
    global scr
    if choice==img_list[x]:
        if choice==False:
            ans="You're right its's real"
            scr=scr+1
        elif choice==True:
            ans="You're right its's AI"
            scr=scr+1
    else:
        if choice==False:
            ans="You're wrong its's AI"
        elif choice==True:
            ans="You're wrong its's real"
    return render_template ("index.html",explanation =explain[x],ans=ans,scr=scr)

@app.route("/1",methods=['POST'])
def respond():
    temp2=0
    if 'AI' in request.form.values():
        temp=True
    elif 'Real' in request.form.values():
        temp=False
    return check(temp,temp2)

# main driver function
if __name__ == '__main__':
    app.run(debug=True)

