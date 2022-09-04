 python manage.py migrate

  migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called


  python manage.py makemigrations

  makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.