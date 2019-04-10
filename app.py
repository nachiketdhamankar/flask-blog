from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author':"Author1",
        'title':"Title1",
        'content':"Content1",
        'date_posted' : "20 April 2019"
    },  
    {
        'author':"Author3",
        'title':"Title2",
        'content':"Content2",
        'date_posted' : "21 April 2019"
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts,
        title = "Home")

@app.route('/about')
def about():
    return render_template('about.html', title = "About")

if __name__ == '__main__':
    app.run(debug=True)