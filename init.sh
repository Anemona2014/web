sudo rm -r /etc/nginx/sites-enabled/default
sudo rm -r /etc/gunicorn.d/django.py
sudo rm -r /etc/gunicorn.d/hello.py
sudo rm -r /etc/gunicorn.d/test1
sudo rm -r /etc/gunicorn.d/test2
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -s  ~/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s ~/web/etc/django.py  /etc/gunicorn.d/dgango.py
sudo ln -s ~/web/etc/gunicorn.conf   /etc/gunicorn.d/test1
sudo ln -s ~/web/etc/django-gunicorn.conf  /etc/gunicorn.d/test2
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start

