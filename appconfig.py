import platform

where = platform.uname().release.find("aws")

if where == -1:
    # Local.
    config = {
        "host": "127.0.0.1",
        "database": "commentsDB",
        "user": "comment",
        "password": "commentpasswd",
    }
else:
    # Not on PA.

    config = {
        "host": "keithdavidson.mysql.pythonanywhere-services.com",
        "database": "keithdavidson$default",
        "user": "keithdavidson",
        "password": "Peace212",
    }
