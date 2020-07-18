# Read Me

The current repository [(claudioperez/FEDEASdoc)](https://github.com/claudioperez/FEDEASdocs) contains the working source files from which FEDEASLab documentation is built. The static website files (HTML, CSS, JS) which are generated from this repository are hosted in the separate [FCFilippou/fedeaslab](https://github.com/fcfilippou/fedeaslab) repository, which is currently serving the website.

## Local Directory

      dir/
      ├── FEDEASdocs/...
            
      ├── FEDEASdoc/  
         ├── docs/   
            ├── api/
            └── src/...
   
      └── FEDEASLab/ 
         ├── m2html/       
         └── src/
            ├── Solution_Scripts/   
            └── Element_Library/...

## Steps to Build

1. Build function pages from FEDEASLab source
   1. Set current folder in Matlab to `dir/FEDEASLab/`
   2. Add `dir/FEDEASLab/m2html/` to path
   3. run the following:
      `>> m2html('mfiles','src', 'htmldir','../FEDEASdoc/docs/FEDEASLab', 'recursive','on', 'global','on','extension','.md','source','off');`
2. Build website
   1. Open terminal and cd to `dir/FEDEASdoc$`
   2. run the following: `$ mkdocs build`
3. Upload site pages to server
   1. Open Github desktop
   2. Set current repository to **FEDEASdocs**
   3. **commit** changes
   4. **Push origin**

-------------------------

**END OF STAGE 1 MATERIAL**

-------------------------

### Build API docs

>`dir/FedeasAPI$ jsonschema2md -d schemas -o ../FEDEASdoc/docs/dat -h false -p description`

## Other notes

-------


### Site styling

Colors schemes and fonts used throughout the site are specified in the file `css/extra.css`.

### Commands

#### Powershell / Cmd

Build site html files.
> `elstir build`

Create a local server for real-time editing.
> `elstir serve`

Convert all html files in the active directory to markdown.
> gci -r -i *.html |foreach{$md=$_.directoryname+"\"+$_.basename+".md";pandoc $_.name -o $md}

#### Bash (Linux subsystem)

>make all

>make doc-serve

### Equation Handling

Details regarding equation handling and supported Latex commands can be found [here](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/).

The displaying of equations typeset in Latex is handled by the python package `python-markdown-math`. This can be installed by running the following command in an Anaconda-activated command line environment.

> `conda install -c conda-forge python-markdown-math`

<!-- [stackoverflow answer](https://stackoverflow.com/questions/27882261/mkdocs-and-mathjax/31926644#31926644) -->

### YAML Notes

"There are two groups of styles, block and flow. Block styles use indentation to denote nesting and scope within the document. In contrast, flow styles rely on explicit indicators to denote nesting and scope" [3.2.3.1. Node Styles].

"There are 5 styles of scalars in YAML: plain, single-quoted, double-quoted, literal, and folded"

### Json Tools

- [Schema Forms](http://schemaform.io/)

### Inspiration

Layout references

- [Google](https://cloud.google.com/apis/design/documentation#checklist)
- [pandas](https://pandas.pydata.org/docs/)- Sphinx
- [Stripe](https://stripe.com/docs/api?utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier&utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier)
- [pyramid](https://trypyramid.com/documentation.html)
- [seaborn](https://seaborn.pydata.org/)
- [Heroku](https://devcenter.heroku.com/?utm_source=zapier.com&utm_medium=referral&utm_campaign=zapier) 
- [colorlib](https://colorlib.com/)
- [numba](http://numba.pydata.org/) - Sphinx
- [julia](https://julialang.org/)
