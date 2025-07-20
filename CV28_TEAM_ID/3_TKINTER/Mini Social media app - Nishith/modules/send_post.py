posts = []

def create_post(content, image=None):
    post = {
        "user": "Nishith",
        "content": content,
        "image": image,
        "likes": 0,
        "comments": []
    }
    posts.append(post)
