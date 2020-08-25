from flask import Flask,request,render_template
import pickle,string
from nltk.corpus import stopwords

app=Flask(__name__)

def stopp(mess):
    word=[c for c in mess if c not in string.punctuation]
    sent=''.join(word)
    return [words for words in sent.split() if words not in stopwords.words('english')]

@app.route('/',methods=['GET','POST'])
def predict_spam():
    mess=request.form['message']
    model=pickle.load(open('spamdetector_model.h5','rb'))
    return render_template('spamclassifiertemp.html',spam=model.predict([[mess]])[0])

if __name__ == '__main__':
    app.run()
        