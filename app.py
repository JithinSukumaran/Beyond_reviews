from flask import Flask,render_template,redirect,request
import json
import requests
import pandas as pd
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import subprocess

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

class Books(db.Model):  # here we are creating a table in the database
    id = db.Column(db.Integer,primary_key=True)  # these three are the columns
    name = db.Column(db.String(200))
    price = db.Column(db.String(200))
    star_rating = db.Column(db.String(200))
    date_created = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):  # this is what it will print when called
        return '<Task %r>' % self.id

@app.route('/',methods=['POST','GET'])  # this represents a page
def hello_world():
    # subprocess.run(['scrapyrt'])
    if request.method == 'POST':
        return 'Hello'
    else:
        params = {
        'spider_name':'books1',
        'start_requests':True
        }


        spider_name = "books1"
        subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", "output.json"])
        with open("output.json") as items_file:
            return items_file.read()


        # response = requests.get('http://localhost:9080/crawl.json',params)
        # data = json.loads(response.text)
        # count = 0
        # for item in data['items']:
        #     count+=1
        #     item_name = item['Name']
        #     item_price =  item['Price']
        #     item_rating = item['Star Rating']
        #     new_item = Books(name=item_name,price=item_price,star_rating=item_rating)
        #     try:
        #         db.session.add(new_item)
        #         db.session.commit()
        #     except:
        #         return 'There was some error adding the item to the database'
        # return f'All items were successfully added to the database, for loop ran for {count} times'




    # params = {
    # 'spider_name':'books1',
    # 'start_requests':True
    # }
    # response = requests.get('http://localhost:9080/crawl.json',params)
    # data = json.loads(response.text)
    # # print(data)
    # df = pd.DataFrame(data=data['items'],columns=['Name','Price','Star Rating'])
    #
    # # print(df)
    # return render_template('index.html',tables = [df.to_html(classes='data',index=False)],titles=df.columns.values)

# @app.route('/about')
# def about():
# 	return 'This is the about page'

if __name__=='__main__':  # don't use this while deployment
	app.run(debug=True)
