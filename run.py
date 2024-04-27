from flask_blog import create_app

app = create_app()

# app.app_context().push()
# file = open('posts.json', 'r')
# data = json.load(file)

# for x in data:
#      post = Post(title = x.get('title'), content = x.get('content'), user_id = x.get('user_id'))
#      db.session.add(post)

# db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
    

