<!-- https://chromium.googlesource.com/external/github.com/tensorflow/tensorflow/+/r0.10/tensorflow/g3doc/how_tos/documentation/index.md#writing-tensorflow-documentation -->

# Writing Project Documentation

Project documentation is maintained in [Markdown] files, and resides in the `docs/` directory of the `FEDEASdoc` Github repository. The About, Examples, and Guides sections are manually edited.

Anything in the `docs/Functions` directory is generated from comments in the code, and should not be edited directly. The script `tools/docs/gen_docs.sh` generates the API documentation. If called without arguments, it rebuilds the Python API documentation only (i.e., documentation for Ops, whether defined in Python or C++). If `-a` is passed, it also rebuilds the documentation for the C++ API. It must be called from the tools/docs directory, and if called with -a, requires doxygen to be installed.

## Narative documentation

### Simple changes

The easiest way to make straightforward documentation updates to Markdown files is to use GitHub's web-based file editor. Browse the tensorflow/docs repository to find the Markdown that roughly corresponds to the tensorflow.org URL structure. In the upper right corner of the file view, click the pencil icon

to open the file editor. Edit the file and then submit a new pull request.
Set up a local Git repo

For multi-file edits or more complex updates, it's better to use a local Git workflow to create a pull request.
Note: Git is the open source version control system (VCS) used to track changes to source code. GitHub is an online service that provides collaboration tools that work with Git. See the GitHub Help to set up your GitHub account and get started.

The following Git steps are only required the first time you set up a local project.
Fork the tensorflow/docs repo

On the tensorflow/docs GitHub page, click the Fork button

to create your own repo copy under your GitHub account. Once forked, you're responsible for keeping your repo copy up-to-date with the upstream TensorFlow repo.
Clone your repo

Download a copy of your remote username/docs repo to your local machine. This is the working directory where you will make changes:

git clone git@github.com:username

/docs
cd ./docs

Add an upstream repo to keep up-to-date (optional)

To keep your local repository in sync with tensorflow/docs, add an upstream remote to download the latest changes.
Note: Make sure to update your local repo before starting a contribution. Regular syncs to upstream reduce the chance of a merge conflict when you submit your pull request.

Add a remote:

git remote add upstream

 git@github.com:tensorflow/docs.git

# View remote repos
git remote -v
origin    git@github.com:username

/docs.git (fetch)
origin    git@github.com:username

/docs.git (push)
upstream

  git@github.com:tensorflow/docs.git (fetch)
upstream

  git@github.com:tensorflow/docs.git (push)

To update:

    git checkout master
    git pull upstream

    master

    git push  # Push changes to your GitHub account (defaults to origin)

### GitHub workflow

#### 1. Create a new branch

After you update your repo from `FEDEASdoc`, create a new branch from the local master branch:

    git checkout -b feature-name



    git branch  # List local branches
  master

* feature-name


#### 2. Make changes

Edit files in your favorite editor and please follow the TensorFlow documentation style guide.

Commit your file change:

    # View changes
    git status  # See which files have changed
    git diff    # See changes within files

    git add path/to/file.md


    git commit -m "Your meaningful commit message for the change."

Add more commits, as necessary.

#### 3. Create a pull request

Upload your local branch to your remote GitHub repo (github.com/username/docs):

    git push

After the push completes, a message may display a URL to automatically submit a pull request to the upstream repo. If not, go to the tensorflow/docs repo—or your own repo—and GitHub will prompt you to create a pull request.
4. Review

Maintainers and other contributors will review your pull request. Please participate in the discussion and make the requested changes. When your pull request is approved, it will be merged into the upstream TensorFlow docs repo.
Success: Your changes have been accepted to the TensorFlow documentation.

There is a separate publishing step to update tensorflow.org from the GitHub repo. Typically, changes are batched together and the site is updated on a regular cadence.



## API Documentation

Ops, classes, and utility functions are defined in Python modules, such as image_ops.py. The module docstring is inserted at the beginning of the Markdown file generated for the Python file. Thus, image_ops.md starts with the module docstring in image_ops.py. `python/framework/gen_docs_combined.py` contains the list of all libraries for which Markdown files are created. If you are adding a new library (generating a separate section in the API documentation), you have to add it to the list of libraries in gen_docs_combined.py. For the C++ api, only a single library file exists, its Markdown is a string in gen_cc_md.py, from which api_docs/cc/index.md is created. 

In the module docstring of a file registered as a library, you can insert generated docs for Ops, classes, and functions by calling them out with the syntax @@<python-name> (at the beginning of an otherwise empty line). The called-out op, function, or class does not have to be defined in the same file.

This allows you to control the order in which the Ops, classes, and functions are documented. Group them in a logical order, with interspersed high level documentation.

Every public op, class or function must be called out with a @@ entry in some library. If you don't, you will get doc_gen_test failures.

Docs for Ops are automatically extracted from Python wrappers or C++ Ops registrations, Python wrappers have priority.

- Python wrappers are in python/ops/*.py.
- C++ Ops registrations are in core/ops/*.cc.

Docs for Classes and Utility Functions are extracted from their docstrings.

## Op Documentation Style Guide

Ideally, you should provide the following information, in order of presentation:

- A short sentence that describes what the op does.
- A short description of what happens when you pass arguments to the op.
- An example showing how the op works (pseudocode is best).
- Requirements, caveats, important notes (if there are any).
- Descriptions of inputs, outputs, and Attrs or other parameters of the op constructor.

Each of these is described in more detail below.

Write your text in Markdown (.md) format. A basic syntax reference is here. You are allowed to use MathJax notation for equations. Those will be rendered properly on tensorflow.org, but don't show up on github.
Writing About Code

Put backticks around these things when they're used in text:

- Argument names (e.g. input, x, tensor)
- Returned tensor names (e.g. output, idx, out)
- Data types (e.g. int32, float, uint8)
- Other op names referenced in text (e.g. list_diff(), shuffle())
- Class names (e.g. Tensor when you actually mean a Tensor object; don‘t capitalize or use backticks if you’re just explaining what an op does to a tensor, or a graph, or an operation in general)
- File names (e.g. image_ops.py, or /path-to-your-data/xml/example-name)

Put three backticks around sample code and pseudocode examples. And use ==> instead of a single equal sign when you want to show what an op returns. For example:

```
# 'input' is a tensor of shape [2, 3, 5]
(tf.expand_dims(input, 0)) ==> [1, 2, 3, 5]
```


Put single backticks around math expressions or conditions. For example:

```markdown
This operation requires that `-1-input.dims() <= dim <= input.dims()`.

Tensor Dimensions

When you‘re talking about a tensor in general, don’t capitalize the word tensor. When you‘re talking about the specific object that’s provided to an op as an argument or returned by an op, then you should capitalize the word Tensor and add backticks around it because you're talking about a Tensor object that gets passed.

Don't use the word Tensors to describe multiple Tensor objects unless you really are talking about a Tensors object. Better to say “a list of Tensor objects.”, or, maybe, “Tensors”.

When you're talking about the size of a tensor, use these guidelines:

Use the term “dimension” to refer to the size of a tensor. If you need to be specific about the size, use these conventions:

    Refer to a scalar as a “0-D tensor”
    Refer to a vector as a “1-D tensor”
    Refer to a matrix as a “2-D tensor”
    Refer to tensors with 3 or more dimensions as 3-D tensors or n-D tensors. Use the word “rank” only if it makes sense, but try to use “dimension” instead. Never use the word “order” to describe the size of a tensor.

Use the word “shape” to describe in detail the dimensions of a tensor, and show the shape in square brackets with backticks. For example:

If `input` is a 3-D tensor with shape `[3, 4, 3]`, this operation will return
a 3-D tensor with shape `[6, 8, 6]`.

Links

To link to something else in the g3docs tree, use a relative path, like [tf.parse_example](../api_docs/python/ops.md#parse_example) Do not use absolute paths for internal links, as this will break the website generator.

To link to source code, use a link starting with: https://www.tensorflow.org/code/, followed by the file name starting at the github root. For instance, a link to this file should be written as https://www.tensorflow.org/code/tensorflow/g3doc/how_tos/documentation/index.md. This ensures that tensorflow.org can forward the link to the branch of the code corresponding to the version of the documentation you're viewing. Do not include url parameters in the URL.
Ops defined in C++

All Ops defined in C++ must be documented as part of the REGISTER_OP declaration. The docstring in the C++ file is processed to automatically add some information for the input types, output types, and Attr types and default values.

For example:

REGISTER_OP("PngDecode")
    .Input("contents: string")
    .Attr("channels: int = 0")
    .Output("image: uint8")
    .Doc(R"doc(
Decodes the contents of a PNG file into a uint8 tensor.

contents: PNG file contents.
channels: Number of color channels, or 0 to autodetect based on the input.
  Must be 0 for autodetect, 1 for grayscale, 3 for RGB, or 4 for RGBA.
  If the input has a different number of channels, it will be transformed
  accordingly.
image:= A 3-D uint8 tensor of shape `[height, width, channels]`.
  If `channels` is 0, the last dimension is determined
  from the png contents.
)doc");

Results in this piece of Markdown:

### tf.image.png_decode(contents, channels=None, name=None) {#png_decode}

Decodes the contents of a PNG file into a uint8 tensor.

#### Args:

*  <b>contents</b>: A string Tensor. PNG file contents.
*  <b>channels</b>: An optional int. Defaults to 0.
    Number of color channels, or 0 to autodetect based on the input.
    Must be 0 for autodetect, 1 for grayscale, 3 for RGB, or 4 for RGBA.  If the
    input has a different number of channels, it will be transformed accordingly.
*  <b>name</b>: A name for the operation (optional).

#### Returns:

  A 3-D uint8 tensor of shape `[height, width, channels]`.
  If `channels` is 0, the last dimension is determined
  from the png contents.

Much of the argument description is added automatically. In particular, the doc generator automatically adds the name and type of all inputs, attrs, and outputs. In the above example, <b>contents</b>: A string Tensor. was added automatically. You should write your additional text to flow naturally after that description.

For inputs and output, you can prefix your additional text with an equal sign to prevent the automatically added name and type. In the above example, the description for the output named image starts with = to prevent the addition of A uint8 Tensor. before our text A 3-D uint8 Tensor.... You cannot prevent the addition of the name, type, and default value of attrs this way, so write your text carefully.
Ops defined in Python

If your op is defined in a python/ops/*.py file, then you need to provide text for all of the arguments and output (returned) tensors.

You should conform to the usual Python docstring conventions, except that you should use Markdown in the docstring. The doc generator does not auto-generate any text for ops that are defined in Python, so what you write is what you get.

Here's a simple example:

def foo(x, y, name="bar"):
  """Computes foo.

  Given two 1-D tensors `x` and `y`, this operation computes the foo.

  For example:

x is [1, 1]
y is [2, 2]

tf.foo(x, y) ==> [3, 3]


Args:
  x: A `Tensor` of type `int32`.
  y: A `Tensor` of type `int32`.
  name: A name for the operation (optional).

Returns:
  A `Tensor` of type `int32` that is the foo of `x` and `y`.

Raises:
  ValueError: If `x` or `y` are not of type `int32`.
"""

...

Description of the Docstring Sections

Here is more detail and examples for each of the elements of the docstrings.
Short sentence that describes what the op does.

Examples:

Concatenates tensors.

Flips an image horizontally from left to right.

Computes the Levenshtein distance between two sequences.

Saves a list of tensors to a file.

Extracts a slice from a tensor.

Short description of what happens when you pass arguments to the op.

Examples:

Given a tensor input of numerical type, this operation returns a tensor of
the same type and size with values reversed along dimension `seq_dim`. A
vector `seq_lengths` determines which elements are reversed for each index
within dimension 0 (usually the batch dimension).

This operation returns a tensor of type `dtype` and dimensions `shape`, with
all elements set to zero.

Example showing how the op works.

The squeeze() op has a nice pseudocode example:

shape(input) => `[1, 2, 1, 3, 1, 1]`
shape(squeeze(input)) =>  `[2, 3]`

The tile() op provides a good example in descriptive text:

For example, tiling `[a, b, c, d]` by 2 produces
`[[a, b, c, d], [a, b, c, d]]`.

It is often helpful to show code samples in Python. Never put them in the C++ Ops file, and avoid putting them in the Python Ops doc. Put them in the module or class docstring where the Ops constructors are called out.

Here's an example from the module docsting in image_ops.py:

TensorFlow can convert between images in RGB or HSV. The conversion
functions work only on `float` images, so you need to convert images in
other formats using [`convert_image_dtype`](#convert-image-dtype).

Example:

```python
# Decode an image and convert it to HSV.
rgb_image = tf.image.decode_png(...,  channels=3)
rgb_image_float = tf.image.convert_image_dtype(rgb_image, tf.float32)
hsv_image = tf.image.rgb_to_hsv(rgb_image)
```

Requirements, caveats, important notes.

Examples:

This operation requires that: `-1-input.dims() <= dim <= input.dims()`

Note: This tensor will produce an error if evaluated. Its value must
be fed using the `feed_dict` optional argument to `Session.run()`,
`Tensor.eval()`, or `Operation.run()`.

Descriptions of arguments and output (returned) tensors.

Keep the descriptions brief and to the point. You should not have to explain how the operation works in the argument sections.

Mention if the Op has strong constraints on the dimensions of the input or output tensors. Remember that for C++ Ops, the type of the tensor is automatically added as either as “A ..type.. Tensor” or “A Tensor with type in {...list of types...}”. In such cases, if the Op has a constraint on the dimensions either add text such as “Must be 4-D” or start the description with = (to prevent the tensor type to be added) and write something like “A 4-D float tensor”.

For example, here are two ways to document an image argument of a C++ op (note the “=” sign):

image: Must be 4-D. The image to resize.

image:= A 4-D `float` tensor. The image to resize.

In the documentation, these will be rendered to markdown as

image: A `float` Tensor. Must be 4-D. The image to resize.

image: A 4-D `float` Tensor. The image to resize.

Optional arguments descriptions (“attrs”)

The doc generator always describe attrs type and default value, if any. You cannot override that with an equal sign because the description is very different in the C++ and Python generated docs.

Phrase any additional attr description so that it flows well after the type and default value.

Here's an example from image_ops.py:

REGISTER_OP("PngDecode")
    .Input("contents: string")
    .Attr("channels: int = 0")
    .Output("image: uint8")
    .Doc(R"doc(
Decode a PNG-encoded image to a uint8 tensor.

The attr `channels` indicates the desired number of color channels for the
decoded image.

Accepted values are:

*   0: Use the number of channels in the PNG-encoded image.
*   1: output a grayscale image.

...

contents: 0-D. The PNG-encoded image.
channels: Number of color channels for the decoded image.
image: 3-D with shape `[height, width, channels]`.
)doc");

This generates the following “Args” section:

  contents: A string Tensor. 0-D. The PNG-encoded image.
  channels: An optional `int`. Defaults to 0. Number of color channels for the
    decoded image.
  name: A name for the operation (optiona


