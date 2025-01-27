copy_content:
	rm -rf ./content
	mkdir ./content
	mkdir ./content/Reading ./content/Articles
	cp -rp "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/Dev/" ./content/
	cp -rp "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/Reading/" ./content/Reading/
	cp -rp "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/Slip-box/" ./content/Slip-box/
	cp -rp "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/Readwise/Books/" ./content/Reading/
	cp -rp "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/Readwise/Articles/" ./content/Articles/
	cp -rp "/Users/hazadus/Library/Mobile Documents/iCloud~md~obsidian/Documents/Hazadus Vault/attachments/" ./content/attachments
	rm -rf ./content/attachments/*.pdf
prepare:
	make copy_content
	python3 walk.py
serve:
	make prepare
	npx quartz build --serve
build:
	make prepare
	npx quartz build
deploy:
	make prepare
	npx quartz sync