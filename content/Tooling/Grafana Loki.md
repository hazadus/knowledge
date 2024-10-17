Skillbox lesson: [here](https://go.skillbox.ru/profession/profession-python/django-framework/468b94e8-6cb8-4485-9bd6-9ab3d79fedc8/videolesson).

```yml
grafana:  
  container_name: "grafana"  
  image: grafana/grafana:10.2.3  
  environment:  
    - GF_AUTH_ANONYMOUS_ENABLED=true  
    - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin  
  ports:  
    - "3000:3000"  
  
loki:  
  container_name: "loki"  
  image: grafana/loki:2.9.3  
  ports:  
    - "3100:3100"
```

```bash
docker compose up -d grafana loki
```

Navigate to `localhost:3000`.

Click "Home -> Connections -> Data Sources".
Click "Data Sources" button, then select "Loki".
Enter URL: `http://loki:3100/`.
Press "Save and Test".

Команда для установки плагина Loki: `docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions`

Ensure that plugin was installed: `docker plugin ls`.

Add to service config:
```yaml
logging:  
  driver: loki  
  options:  
    loki-url: http://host.docker.internal:3100/loki/api/v1/push
```

Restart services.

*Create new dashboard.*

---
## Примеры построения графиков в дашборде по логам:

Requests Completed:
```logql
sum(
	count_over_time({job="fluentbit"} | json | msg="request completed" [1m])
)
```

----
## Сбор логов из файла с Fluentbit

`fluent-bit.conf`
```
[SERVICE]
   flush       1
   log_level   info
[INPUT]
   name        tail
   path        /etc/data/data.log
   tag         log_generator
[OUTPUT]
   Name        stdout
   Match       *
[OUTPUT]
   # for sending logs to local Loki instance
   name        loki
   match       *
   host        loki
   port        3100
   labels      job=fluentbit
   drop_single_key raw
   line_format     json
```

Заменить имя файла с логом `/usr/projects/go-anvlink/stdout.log` на корректное, остальное можно не трогать. Графана будет на порту 3001.

`docker-compose.yml`:
```yml
version: "3"

networks:
  loki:

services:
  fluent-bit:
    image: fluent/fluent-bit
    volumes:
      - ./fluent-bit.conf:/fluent-bit/etc/fluent-bit.conf
      - /usr/projects/go-anvlink/stdout.log:/etc/data/data.log
    depends_on:
      - loki
    networks:
      - loki

  loki:
    image: grafana/loki:2.7.0
    ports:
      - "3100:3100"
    command: -config.file=/etc/loki/local-config.yaml
    networks:
      - loki

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3001:3000"
    networks:
      - loki
    environment:
      - GF_PATHS_PROVISIONING=/etc/grafana/provisioning
      - GF_AUTH_ANONYMOUS_ENABLED=true
      - GF_AUTH_ANONYMOUS_ORG_ROLE=Admin
    entrypoint:
      - sh
      - -euc
      - |
        mkdir -p /etc/grafana/provisioning/datasources
        cat > /etc/grafana/provisioning/datasources/ds.yaml << EOF
        apiVersion: 1
        datasources:
        - name: Loki
          type: loki
          access: proxy
          orgId: 1
          url: http://loki:3100
          basicAuth: false
          isDefault: true
          version: 1
          editable: true
        EOF
        /run.sh
```

----
📂 [[Tooling]] | Последнее изменение: 07.10.2024 08:44