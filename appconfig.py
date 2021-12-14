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
        "host": "c00252500.mysql.pythonanywhere-services.com",
        "database": "c00252500$commentsdb",
        "user": "c00252500",
        "password": "Peace212",
    }  # pragma: no cover
