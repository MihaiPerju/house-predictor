from flask import Flask, render_template,request
from model import model,X_test,features
import pandas as pd

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def root():
    if request.method == 'POST':

        year = request.form.get('year')
        quality = request.form.get('quality')
        bsmt_area = request.form.get('bsmt_area')
        gr_area = request.form.get('gr_area')

        try:
            data = pd.DataFrame({'OverallQual': [quality],'YearBuilt':[year],'TotalBsmtSF':[bsmt_area],'GrLivArea':[gr_area]});
            prediction = model.predict(data[features])[0]
            return render_template("index.html",prediction=prediction)
        except:
            return render_template("index.html",prediction="Invalid Request")

    else:
        return render_template("index.html")
    