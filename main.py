from flask import Flask, render_template
import requests
from post import Post

BLOG_URL = "https://api.npoint.io/c790b4d5cab58020d391"

blog_posts = []
response = requests.get(url=BLOG_URL)
response.raise_for_status()
all_blogs = response.json()
for blog in all_blogs:
    new_post = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    blog_posts.append(new_post)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_posts)


@app.route("/read/<int:b_id>")
def post_blog(b_id):
    my_post = None
    for obj in blog_posts:
        if obj.id == b_id:
            my_post = obj
    return render_template("post.html", post=my_post)


if __name__ == "__main__":
    app.run(debug=True)
