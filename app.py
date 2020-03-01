from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    name='Jack'
    boke = [
        {'title':'《了不起的麦瑟尔夫人》蕴藏在六十年代中的时尚宝典','type':'时尚'},
        {'title':'最好的爱情是哪一种？“白瑞德爱郝思嘉','type':'情感'},
        {'title':'《完美关系》：成年人离婚，都是蓄谋已久的结果','type':'情感'},
        {'title':'我们从未这样怀念那种人间烟火气','type':'生活'},
        {'title':'冬天，我们去海边看落日 ','type':'生活'},
        {'title':'张亮被曝与前妻同进出：中年人的婚姻，多少是离婚不离家 ','type':'情感'},
        {'title':'“我想嫁给谢永强，治服谢广坤”：不给力的丈夫，逼疯了多少女人 ','type':'情感'},
        {'title':'爱鞋常穿常新指南','type':'时尚'}
        ]
    return render_template('index.html',name=name,boke=boke)