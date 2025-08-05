from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html",scr=scr,img_src=img_src,img_num=img_num,img=img)

@app.route("/",methods=['POST'])
def clear():
    global scr
    global final
    global img
    if scr==10:
        final=True
    img+=1
    return render_template ("index.html",explanation=False,ans=False,scr=scr,img_src=img_src,img_num=img_num,final=final,img=img)

scr=int(0)
used=[False,False,False,False,False,False,False,False,False,False]

img_list=[False,False,False,False,False,False,False,False,True,False]
explain=[
    "This is a photo of a Flamingo from a strange angle. It was submitted in an AI image generation competion and won, however its creator revealed it was real",
    "This is a Jerboa, we caught him at a bad time",
    "This is a Proboscis Monkey, he looks a bit like squidward",
    "This is a Saiga Antelope, it lives in Russia and is on the verge of extinction",
    "This is a Basking Shark, it is the second largest type of shark",
    "This is a Tassled Wobbegon, it is a type of carpet shark",
    "This is a Tarsier, it has big eyes",
    "This is a Colugo, it is a type of flying lemur",
    "This is an AI-generated image of a Streaked Tenrec, it would live in Madagascar if it wasn't an AI Image",
    "This is a Glass Frog, its organs can be seen through its body",
]

img_num= -1
img=0

img_src=[
    "static/img_1.jpeg",
    "static/img_2.png",
    "static/img_3.jpg",
    "static/img_4.webp",
    "static/img_5.png",
    "static/img_6.jpeg",
    "static/img_7.jpg",
    "static/img_8.jpg",
    "static/img_10.webp",
    "static/img_9.jpg",
]

final=False

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
    return render_template ("index.html",explanation =explain[x],ans=ans,scr=scr,img_src=img_src,img_num=img_num,img=img)

@app.route("/1",methods=['POST'])
def respond():
    global img_num
    global final
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

