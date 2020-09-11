# Tool Overview

-------

## Primary

1. [**Github**]() \
   File sharing, version control and site serving (via Github Pages)

2. **Anaconda** \
   Provides an implementation of Python which is required to run some of the other tools (e.g. mkdocs, sphinx, plotting). In addition to Python, Anaconda also provides a package manager which allows the organized management of software and dependencies.

   To install all project dependencies, run `conda env create -f environment.yml`, or run each of the following commands sequentially:
   - `conda config --add channels conda-forge`
   - `conda install mkdocs`
   - `conda install python-markdown-math`
   - `conda install mkdocs-bootswatch`

## Secondary

1. [**JSON**](https://www.json.org/json-en.html) \
    Also see [yaml](https://yaml.org/spec/1.1/#id857168).
2. **Static site**:
   - Dynamic Sites: (Wordpress)
   - [mkdocs](empty) (Md) vs [Sphinx](empty) (RST)
     - Markdown arguably has a larger developer base than RST with more tools - *arguably*.
     - Markdown is easier/more intuitive than RST.
3. [**Markdown**](https://commonmark.org/)
   - Read about markdown from its creator [here](https://daringfireball.net/projects/markdown/syntax)
   - Find a quick markdown reference [here](https://daringfireball.net/projects/markdown/syntax)
  
## Extra

1. [**Pandoc**](#2-pure-text---data-structuresfundamentals)
