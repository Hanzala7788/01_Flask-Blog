from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_blog.models import Post
from flask_blog.posts.forms import SearchForm

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.dateposted.desc()).paginate(page=page, per_page=5)

    
    # Truncate post content to 500 characters
    for post in posts.items:
        if len(post.content) > 500:
            post.content = post.content[:500] + '...'
    

    form = SearchForm()  # Creating an instance of SearchForm
    return render_template('home.html', posts=posts, form=form)

@main.route('/about')
def about():
    form = SearchForm()
    return render_template('about.html', title='About', form=form)


