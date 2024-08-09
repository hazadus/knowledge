Взято отсюда: https://github.com/yandex-cloud-examples/yc-practicum-serverless-telegram-bot/blob/main/steps/08-create-object-storage/README.md

Следующие команды позволяют создать новый бакет из CLI.

Создать файл `main.tf`:

```
terraform {
  required_providers {
    yandex = {
      source = "terraform-providers/yandex"
    }
  }
}

provider "yandex" {
  token     = "<OAuth>"
  cloud_id  = "<CLOUD_ID>"
  folder_id = "<FOLDER_ID>"
  // zone      = "ru-central1-a"
}

resource "yandex_storage_bucket" "bucket" {
  // AWS_ACCESS_KEY_ID
  access_key = "<ACCESS_KEY>"
  // AWS_SECRET_ACCESS_KEY
  secret_key = "<SECRET_KEY>"
  // Bucket name, eg `sls-tg-bot`
  bucket = "<BUCKET-ID>"
}
```

После внесения правок, находясь в каталоге с файлом  `main.tf` последовательно выполните следующие команды:

```bash
# Use VPN for first command!
terraform init
terraform plan
terraform apply
```

