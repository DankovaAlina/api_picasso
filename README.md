# **Стек технологий**

- Python 3.9.6
- Django 4.2.10
- Django REST Framework 3.14.0

# **Как запустить проект**

### **Клонировать репозиторий и перейти в него в командной строке:**

```
git clone https://github.com/DankovaAlina/api_picasso.git
cd api_picasso
```

### **Запустить команду docker compose:**

```
docker compose up
```

# **Структура файла .env**

- USE_POSTGRES - bool - флаг использования PostgreSQL или SQLite
- POSTGRES_USER - str - логин пользователя в PostgreSQL
- POSTGRES_PASSWORD - str - пароль пользователя в PostgreSQL
- POSTGRES_DB - str - название БД в PostgreSQL
- DB_HOST - str - название хоста в PostgreSQL
- DB_PORT - int - порт PostgreSQL
- SECRET_KEY - str - ключ шифрования
- DEBUG - bool - флаг использования режима отладки
- ALLOWED_HOSTS - str - разрешенные хосты с разделителем через запятую ('localhost,127.0.0.1')
- RABBITMQ_DEFAULT_USER - str - логин пользователя в RabbitMQ
- RABBITMQ_DEFAULT_PASSWORD - str - пароль пользователя в RabbitMQ

# **Автор**

@DankovaAlina