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

----
📂 [[Tooling]]