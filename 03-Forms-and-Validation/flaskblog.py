from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a20bc41bb5e72ee23304db97f1cd17f99c'

posts = [
    {
        'author': 'Dheeraj Bhagchandani',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Jatin kumar',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 25, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'dheerajbhagchandani@gmail.com' and form.password.data == '12345':
            flash('You have been logged in Successfuly!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
