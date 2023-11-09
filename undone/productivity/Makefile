all: prechelt-development-time.pdf prechelt-development-time.svg

prechelt-development-time.svg: jccpprtTR.csv prechelt-development-time.py
	python prechelt-development-time.py $< $@

prechelt-development-time.pdf: jccpprtTR.csv prechelt-development-time.py
	python prechelt-development-time.py $< $@
