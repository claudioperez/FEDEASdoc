# Read Me

This document outlines the basic structure of the FEDEASLab documentation website, and the primary tools which are used in its implementation. 

The current repository [(claudioperez/FEDEASdoc)]() contains the source files from which FEDEASLab documentation is built. The static website files which are generated from the source in this repository are hosted in the separate [claudioperes/FEDEASdoc**s**](https://github.com/claudioperez/FEDEASdocs) repository, which is currently serving the website.

## Site structure

-------

This section outlines 3 basic types of pages used by the website, and explains the different workflows they entail:

1. Pages which are automatically generated from comments in program source code.
2. Pages which are manually written for the purpose of explaining certain concepts
3. Pages which are deeply linked to scripts or code, but also contain a lot of written content (e.g. examples).

### 1. Text from code - API/Functions

> [Markdown](https://commonmark.org/help/)

These pages are automatically extracted from comments or docstrings in source code files, and serve the purpose of documenting specific function APIs.

#### To build API documentation from a FEDEAS release.

*Assuming no changes are made to the current `m2html` scripts.*

1. build docs with m2html
2. copy created directories into `docs/FEDEASLab/`
3. run find-replace from '.html' to '/' on all FEDEASLab.html files
<!-- 4. run `pandoc` to convert from html to md -->
<!-- 5. run find-replace on entire site directory to delete instances of `[]{#_synopsis}` and variants -->
2. Change file extensions from .html to .md.
3. *delete* `<head>` section from files

### 2. Pure text - Data Structures/Fundamentals

>[Pandoc](https://pandoc.org/MANUAL.html)

These pages describe aspects of FEDEASLab in detail beyond what is written in the code comments. These pages are not directly linked to any program files.

#### Fundamental elements

### 3. Text with code - Examples

These pages are intimately linked with code.

## Tool Overview

----------

### Preliminary

1. [**Github**]()
   File sharing, version control and site serving (via Github Pages)

2. **Anaconda**
   Provides an implementation of Python which is required to run some of the other tools. In addition to Python, Anaconda also 

### Secondary

1. **Data serialization**: [yaml](https://yaml.org/spec/1.1/#id857168), [JSON]()
2. **Static site**: [markdown](https://commonmark.org/)
   - Dynamic Sites: (Wordpress)
   - [mkdocs](empty) (Md) vs [Sphinx](empty) (RST)
     - Markdown arguably has a larger developer base than RST with more tools - *arguably*.
     - Markdown is easier/more intuitive than RST.
  
### Extra

1. **Document translation**:  [Pandoc](#2-pure-text---data-structuresfundamentals)

## Layout

The layout of the website is specified in the file `/mkdocs.yml`. For more information go to [mkdocs.org](https://www.mkdocs.org).

## Other notes

-------

### Directory layout

    docs
    ├── css                     # 
    ├── src                     #
    ├── FEDEASLab.md            # 
    ├── index.md                # 
    ├── css/                     # 
    ├── src/                    #
    └── FEDEASLab/ 
        ├── FEDEASLab.md        # 
        ├── index.md 
            └── README.md
### Styling

Colors schemes and fonts used throughout the site are specified in the file `css/extra.css`.

### Commands

#### Powershell / Cmd

Build site html files.
> `mkdocs build`

Create a local server for real-time editing.
> `mkdocs serve`

Convert all html files in the active directory to markdown.
> gci -r -i *.html |foreach{$md=$_.directoryname+"\"+$_.basename+".md";pandoc $_.name -o $md}

#### Bash (Linux subsystem)

>make all

>make doc-serve

### Resources



### Equation Handling

Details regarding equation handling and supported Latex commands can be found [here](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/).

The displaying of equations typeset in Latex is handled by the python package `python-markdown-math`. This can be installed by running the following command in an Anaconda-activated command line environment. 

> `conda install -c conda-forge python-markdown-math`

[stackoverflow answer](https://stackoverflow.com/questions/27882261/mkdocs-and-mathjax/31926644#31926644)

### YAML

There are two groups of styles, block and flow. Block styles use indentation to denote nesting and scope within the document. In contrast, flow styles rely on explicit indicators to denote nesting and scope [3.2.3.1. Node Styles].

There are 5 styles of scalars in YAML: plain, single-quoted, double-quoted, literal, and folded

### References

Layout references

- [pandas](https://pandas.pydata.org/docs/)- Sphinx
- [Stripe](https://stripe.com/docs/api?utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier&utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier)
- [pyramid](https://trypyramid.com/documentation.html)
- [seaborn](https://seaborn.pydata.org/)
- [Heroku](https://devcenter.heroku.com/?utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier) 
- [colorlib](https://colorlib.com/)
- [numba](http://numba.pydata.org/) - Sphinx
- [julia](https://julialang.org/)