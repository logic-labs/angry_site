# uwsgi --plugin=python37 --ini angry_site_uwsgi.ini &
gunicorn --workers 3 --bind unix:angry_site_wsgi.sock -m 007 wsgi:app > angry_site_gunicorn.log 2>&1 &
sleep 3
chmod 666 angry_site_wsgi.sock
# sleep 1
su -c "/etc/init.d/nginx start"
