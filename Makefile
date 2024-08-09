serve:
	rm -rf ./content
	mkdir ./content
	cp -r "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/Dev/" ./content/
	cp -r "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/attachments/" ./content/attachments
	rm -rf ./content/attachments/*.pdf
	python3 walk.py
	npx quartz build --serve
build:
	rm -rf ./content
	mkdir ./content
	cp -r "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/Dev/" ./content/
	cp -r "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/attachments/" ./content/attachments
	rm -rf ./content/attachments/*.pdf
	python3 walk.py
	npx quartz build
deploy:
	rm -rf ./content
	mkdir ./content
	cp -r "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/Dev/" ./content/
	cp -r "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/attachments/" ./content/attachments
	rm -rf ./content/attachments/*.pdf
	python3 walk.py
	npx quartz build
	aws s3 rm s3://hazadus-knowledge --recursive --endpoint-url https://storage.yandexcloud.net --profile default
	aws s3 cp public s3://hazadus-knowledge --recursive --endpoint-url https://storage.yandexcloud.net --profile default
