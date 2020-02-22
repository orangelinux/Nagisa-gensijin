import nagisa
from pykakasi import kakasi
from flask import Flask
from flask import Flask, request, render_template
app = Flask(__name__)
kakasi = kakasi()
kakasi.setMode('J', 'K')
@app.route('/')
def index():
    conv = kakasi.getConverter()
    text = request.args.get('text')
    words = nagisa.tagging(text)
    print(words.words)
    print(words.postags)
    ary = []
    for wwd,wd in enumerate(words.postags):
         print(wd)
         if wd=="名詞" or wd=="動詞" or wd=="助動詞":
             print("selected")
             ary.append(words.words[wwd])     
         else:
            print("unselected")
    strary1 = ','.join(ary)
    strary = strary1.replace(',',' ')
    ap = conv.do(strary)
    kakasi.setMode('H','K')
    conv = kakasi.getConverter()
    return conv.do(ap)
if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=80)

