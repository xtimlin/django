.\venv\Scripts\activate
deactivate


Django
python -m django --version
django-admin


start server
    python .\manage.py runserver


    python .\manage.py createsuperuser
        tim - admin
        test112122312@gmail.com
        password1234

        testuser - Supper11
    python .\manage.py makemigrations
    python .\manage.py migrate



user.post_set.create(title='Blog3', content='Third Post Content')


>>> user = User.objects.first()
>>>
>>> post_2 = Post(title='Blog2', content='Second Post Content', author=user)
>>> post_2.save()




pip install virtualenv
python -m venv venv;
.\venv\Scripts\activate;
python -m pip install --upgrade pip;
pip install Django;
pip install django-crispy-forms;
pip install crispy_bootstrap4;
python -m pip install Pillow;


## Load testPostsData
```py
import json
from blog.models import Post

with open('testPostsData.json') as f:
  posts_json = json.load(f)

for post in posts_json:
  post = Post(title=post['title'], content=post['content'], author_id=post['user_id'])
  post.save()
```