# Configuring Gunicorn for Docker

![rw-book-cover](https://pythonspeed.com/assets/titles/gunicorn-in-docker.png)

## Metadata
- Author: [[Itamar Turner-Trauring]]
- Full Title: Configuring Gunicorn for Docker
- Category: #articles
- Document Tags: [[devops]] [[docker]] [[gunicorn]] 
- Summary: This article explains how to properly configure Gunicorn for use in Docker containers, addressing common issues like worker heartbeats and logging. It recommends using an in-memory filesystem for temporary files and starting multiple workers to handle requests efficiently. Additionally, it emphasizes the importance of customizing configurations for container environments instead of relying on traditional setups.
- URL: https://pythonspeed.com/articles/gunicorn-in-docker/

## Highlights
- **The solution: start at least two workers, and probably also start a number of threads using the `gthread` worker backend.**That way each worker process can handle multiple queries so long as some of its time is spent waiting (e.g. for a database query to return). This ensures maximum CPU _utilization_ (not scaling) for the CPU power the container gets, and reduces the chances of being unable to respond to a heartbeat query. ([View Highlight](https://read.readwise.io/read/01jdc0g0x6xzhxryf189wyrn03))



----
📂 [[Articles]] | Последнее изменение: 23.11.2024 16:34