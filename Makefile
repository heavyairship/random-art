gen:
	mkdir -p gallery
	python3 random_art.py

update:
	git add . && git commit -m "update" && git push