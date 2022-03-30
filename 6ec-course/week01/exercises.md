# Exercises Lab Session Week 1

## 1. Explore Jupyter Notebook
- Write a very simple program (e.g., using simple assignments (`a = 5`), arithmetic operations (`a + b`), and the `print()` function) and run it.
- Add Markdown cells with some explanations. You can find a comprehensive guide to Markdown at https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
- Explore how to interact with Jupyter Notebook and discuss with your neighbor.

## 2. Run a simple program in multiple ways
- Check out different ways of running Python code. Think especially of using the `python` interpreter on the command line.
- But you can also consider working with a text editor, or an IDE like `spyder`. It's not about which tool you use exactly, but to explore different possibilities.

## 3. Run (and modify!) the examples in Chapter 2
- You can copy-paste some of the code snippets to Jupyter Notebook. However, you can also download the notebook from Canvas.
- **skip** the examples using `geopandas`.
- But make sure to (1) install the necessary packages, and (2) import them.
- Try to guess the working of elements of the code by playing around with it and changing parts!


---

#### We are skipping the examples using `geopandas`, because you may encounter issues during the installation of `geopandas` (and/or wordcloud).

You *may* encounter problems installing `geopandas`. If that is the case, you can skip the example -- you do not necessarily have to use geopandas in the course, if you are not interested in plotting maps. The reason for the problem is that a part of geopandas is written in the language C, and you do not have a C-compiler (a program for transforming C code into an executable file). If you want to solve this problem, here are two approaches:


- You get a C compiler. A C compiler comes with installing `Xcode` (MacOS, via the MacOS App Store -- that's a good idea anyway, it also includes useful tools like `git`) or the `Buildtools for Virtual Studio` (Windows). For some people, this may also be required to install wordcloud (you get an error message that somewhere in the middle complains about not being able to run `clang` or similar).

- You use a version of `geopandas` in which the C-code is already compiled.

For the second option,

1. Install the Python package called `wheel` using `pip` or `pip3` (e.g., `pip3 install wheel` on the Windows command line `cmd`)
2. Follow the steps in https://towardsdatascience.com/geopandas-installation-the-easy-way-for-windows-31a666b3610f
W hen installing the dependencies, make sure you follow the exact order as the packages are listed. So first, you need to install GDAL, then pyproj etc.

Another approach (which is based on the same logic) is outlined at: https://stackoverflow.com/questions/54734667/error-installing-geopandas-a-gdal-api-version-must-be-specified-in-anaconda.

 . Open the Windows PowerShell as an Administrator and then run the commands outlined in the stackoverflow link.
