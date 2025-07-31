from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",scr=scr,img_src=img_src,img_num=img_num)

@app.route("/",methods=['POST'])
def clear():
    global scr
    if scr==10:
        final=True
    return render_template ("index.html",explanation=False,ans=False,scr=scr,img_src=img_src,img_num=img_num,final=final)

scr=int(0)
used=[False,False,False,False,False,False,False,False,False,False]

img_list=[False,True,True,True,True,True,True,True,True,True]
explain=[
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
]
img_num= -1
img_src=[
    "static/img_1.jpeg",

]

def check(choice,x):
    global scr
    if choice==img_list[x]:
        if choice==False:
            ans="You're right its's real"
            if used[x]==False:
                scr=scr+1
                used[x]=True
        elif choice==True:
            ans="You're right its's AI"
            if used[x]==False:
                scr=scr+1
                used[x]=True
    else:
        if choice==False:
            ans="You're wrong its's AI"
        elif choice==True:
            ans="You're wrong its's real"
    return render_template ("index.html",explanation =explain[x],ans=ans,scr=scr,img_src=img_src,img_num=img_num)

@app.route("/1",methods=['POST'])
def respond():
    global img_num
    img_num+=1
    if img_num!=10:
        if 'AI' in request.form.values():
            temp=True
        elif 'Real' in request.form.values():
            temp=False
        return check(temp,img_num)
    elif img_num==10:
        return render_template("index.html",final=True,scr=scr,img_src=img_src,img_num=img_num)

# main driver function
if __name__ == '__main__':
    app.run(debug=True)

