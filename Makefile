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
