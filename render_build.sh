if [[ $CREATE_SUPERUSER ]];
then
  python manage.py migrate --noinput
  python manage.py createsuperuser --no-input
fi