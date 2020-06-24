app:
	pyuic5 ./ui/gui.ui -o ./ui/gui.py

black:
	rm -rf ./ui/__pycache__
	black main.py ./ui/gui.py ./utils/set_up_docs.py