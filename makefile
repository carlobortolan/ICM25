all: convert move

convert:
	jupyter nbconvert --execute --to html notebook.ipynb

move:
	mkdir -p build
	mv notebook.html build/index.html

# Clean up the build directory
clean:
	rm -rf build