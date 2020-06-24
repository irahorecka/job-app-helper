app:
	pyuic5 ./ui/gui.ui -o ./ui/gui.py

clean:
	rm -rf ./ui/__pycache__