`docker build -t notes-app:1.0 .`

`docker run -d -p 8000:8000 --name dj_notes_service notes-app:1.0`

`docker run -d --name dj_notes_service -p 8000:8000 -v .:/app notes-app:1.0`