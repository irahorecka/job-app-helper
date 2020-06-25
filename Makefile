app:
	pyuic5 ./ui/gui.ui -o ./ui/gui.py

black:
	rm -rf ./ui/__pycache__ ./utils/__pycache__
	black main.py ./ui/gui.py ./utils/write_supplementary_text.py