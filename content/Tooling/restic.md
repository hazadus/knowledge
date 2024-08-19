## Документация

- https://restic.readthedocs.io/en/stable/030_preparing_a_new_repo.html
- https://restic.readthedocs.io/en/stable/040_backup.html
- https://restic.readthedocs.io/en/stable/045_working_with_repos.html
- https://restic.readthedocs.io/en/stable/050_restore.html

## Примеры команд

```bash
# Set keys
export AWS_ACCESS_KEY_ID=<MY_ACCESS_KEY>
export AWS_SECRET_ACCESS_KEY=<MY_SECRET_ACCESS_KEY>

# Init backup repository
restic -r s3:storage.yandexcloud.net/macbook-backup init

# Create snapshot - dry run
restic -r s3:storage.yandexcloud.net/macbook-backup --verbose backup ~/Projects ~/Documents ~/Downloads ~/PycharmProjects  --dry-run

# List snapshots
restic -r s3:storage.yandexcloud.net/macbook-backup snapshots
```

----
📂 [[Tooling]] | Последнее изменение: 13.08.2024 17:00