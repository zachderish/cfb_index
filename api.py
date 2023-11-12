from flask import Flask, redirect, url_for
import database

app = Flask(__name__)

@app.route('/recruiting')
def hello_admin():
   return database.table_data()

if __name__ == '__main__':
   app.run(debug = True)