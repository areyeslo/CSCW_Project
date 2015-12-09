# LaTeX Makefile
FILE=document
all:
	pdflatex $(FILE)
	pdflatex $(FILE)
	bibtex $(FILE)
	pdflatex $(FILE)
	pdflatex $(FILE)

clean:
	\rm *.aux *.blg *.out *.bbl *.log
