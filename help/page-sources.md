# Page Sources

---------------------

The layout of the website is specified in the file `dir/FEDEASdoc/elstir.yml`.

This section outlines 3 basic types of pages used by the website, and explains the different workflows they entail:

1. Pages which are automatically generated from comments in program source code.
2. Pages which are manually written for the purpose of explaining certain concepts.
3. Pages which are deeply linked to scripts or code, but also contain a lot of written content (e.g. examples).

### Type I: Text from code - API/Functions

These pages are automatically extracted from comments or docstrings in source code files, and serve the purpose of documenting specific function APIs.

The following steps are currently being followed to build API documentation from a FEDEASLab release:

*Assuming no changes are made to the current `m2html` scripts.*

1. build docs with m2html
2. copy created directories into `docs/FEDEASLab/`
3. run find-replace from '.html' to '/' on all FEDEASLab.html files
<!-- 4. run `pandoc` to convert from html to md -->
<!-- 5. run find-replace on entire site directory to delete instances of `[]{#_synopsis}` and variants -->
2. Change file extensions from .html to .md.
3. *delete* `<head>` section from files

### Type II: Pure text - Data Structures/Fundamentals

Type II pages describe aspects of FEDEASLab in detail beyond what is written in the code comments. These pages are not directly linked to any program files and are provided directly in either Markdown or HTML files.

#### Latex documents

 Markdown and HTML files can be automatically generated from Latex using tools like [Pandoc](https://pandoc.org/MANUAL.html). A simple example of this conversion is presented. If interest arises in this method, a system can be arranged to accomodate more complex document elements such as custom Latex definitions and Bibtex referencing.

#### Data Structures

### Type III: Text with code - Examples

These pages are intimately linked with code, but contain substantial blocks of writing. Examples of this page type include annotated application demonstrations and documents with dynamic or data-driven figures. Ideal source file formats include notebooks (.ipynb, .mlx).
