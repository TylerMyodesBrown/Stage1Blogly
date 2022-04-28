"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()


@app.route('/')
def show_users():
    """List Users"""
    users = User.query.all()
    return render_template("list.html", users=users)


@app.route('/add_user')
def add_user():
    return render_template('user_sub.html')


@app.route("/sub_resolve", methods=["POST"])
def add_pet():
    """Add user and Return to List."""
    
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    img = request.form['img_url']

    new_user = User(first_name=f_name, last_name=l_name, img_url=img)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(f"/")

@app.route("/<int:user_id>")
def show_pet(user_id):
    """Show info on a single user."""
    user = User.query.get_or_404(user_id)
    posts = user.posts
    
    return render_template("detail.html", user=user, posts = posts)

@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)


@app.route("/edit_resolve", methods=["POST"])
def edit_resolve_user():
    """Edits user and changes in database."""
    
    f_name = request.form['f_name']
    l_name = request.form['l_name']
    img = request.form['img_url']

    user = User.query.filter_by(first_name=f_name).first()
    
    user.first_name = f_name
    user.last_name = l_name
    user.img_url = img
    
    db.session.add(user)
    db.session.commit()
    
    return redirect(f"/")

@app.route('/delete/<int:user_id>')
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("delete_confirm.html", user=user)

@app.route('/delete-final/<int:user_id>')
def edit_user(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect("/")



"""Everything below this point is added for the benefit of round 2 of the excersize"""


@app.route("/post_details/<int:post_id>")
def show_post(post_id):
    """Show info on a single post."""
    post = Post.query.get_or_404(post_id)
    
    return render_template("post_detail.html", post = post)



@app.route("/edit/<int:post_id>")
def edit_post_route(post_id):
    """Show info on a single user."""
    post = Post.query.get_or_404(post_id)
    
    return render_template("post_edit.html", post = post)



@app.route("/post_edit_resolve", methods=["POST"])
def edit_resolve_user():
    """Edits user and changes in database."""
    
    Title = request.form['title']
    Content = request.form['content']

    post = Post.query.filter_by(title=Title).first()
    
    post.title = Title
    post.content = Content
    
    db.session.add(post)
    db.session.commit()
    
    return redirect(f"/")


@app.route("/add_post/<int:user_id>")
def show_post(user_id):
    """Show info on a single user."""
    user = User.query.get_or_404(user_id)
    
    return render_template("add_post.html", user_id = user_id)


@app.route("/add_post_resolve/<int:user_id>", methods=["POST"])
def edit_resolve_user(user_id):
    """Edits user and changes in database."""
    
    Title = request.form['title']
    Content = request.form['content']
    
    new_post = Post(title=Title, content=Content, user_id = user_id)
    db.session.add(new_post)
    db.session.commit()
    
    return redirect(f"/")


@app.route('/delete_post/<int:post_id>')
def edit_user(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("delete_post_confirm.html", post=post)


@app.route('/delete-post-final/<int:post_id>')
def edit_user(post_id):
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect("/")