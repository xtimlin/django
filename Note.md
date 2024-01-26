.\pyenv\Scripts\activate
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



user.post_set.create(title='Blog3', content='Third Post Content')


>>> user = User.objects.first()
>>>
>>> post_2 = Post(title='Blog2', content='Second Post Content', author=user)
>>> post_2.save()