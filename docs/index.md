---
hide_toc: true
---

<!-- # FEDEASLab -->

<body>

<header>

<!-- 
<nav class="navbar navbar-expand-lg">
    <div class="navbar-brand">
    <img src="_static/FEDEASLab-blue-icon-rgb.svg" style="height: 2rem;" alt="FEDEASLab logo">
    </div>
    <div class="navbar-light bg-light">
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    </div>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
    <ul class="navbar-nav">
        <li class="navbar-item"><a class="nav-link" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/user/5minguide.html">Learn FEDEASLab in 5 minutes</a></li>

        <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Documentation
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <a class="dropdown-item" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/index.html">Overview</a>
            <a class="dropdown-item" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/user/index.html">User Manual</a>
            <a class="dropdown-item" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/reference/index.html">Reference Manual</a>
            <a class="dropdown-item" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/cuda/index.html">NVIDIA CUDA GPU Programming</a>
            <a class="dropdown-item" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/roc/index.html">AMD ROCm GPU Programming</a>
            <a class="dropdown-item" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/developer/index.html">Developer Manual</a>
            <a class="dropdown-item" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/release-notes.html">Release Notes</a>
        </div>
        </li>

        <li class="navbar-item"><a class="nav-link" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/user/installing.html">Install</a></li>
        <li class="navbar-item"><a class="nav-link" href="https://FEDEASLab.pydata.org/FEDEASLab-examples/">Examples</a></li>
        <li class="navbar-item"><a class="nav-link" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/user/talks.html">Talks/Tutorials</a></li>

        <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink2" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Community
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink2">
            <a class="dropdown-item" href="https://github.com/FEDEASLab/FEDEASLab">Github</a>
            <a class="dropdown-item" href="https://pypi.org/project/FEDEASLab/">PyPI</a>
            <a class="dropdown-item" href="https://gitter.im/FEDEASLab/FEDEASLab">Gitter Chat</a>
            <a class="dropdown-item" href="https://groups.google.com/a/continuum.io/forum/#!forum/FEDEASLab-users">FEDEASLab Mailing List</a>
        </div>
        </li>

    </ul>
    </div>
</nav> -->

<div class="hero position-relative overflow-hidden p-3 text-center text-dark">
    <div class="col-md-5 p-lg-1 mx-auto my-5">
    <img src="_static/FEDEASLab-blue-horizontal-rgb.svg" style="max-width: 30rem;" alt="FEDEASLab logo">
        <p class="lead font-weight-normal">
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathvariant="normal">&#x03A6;<!-- Φ --></mi>
  <mi>&#x03F5;<!-- ϵ --></mi>
  <mi>&#x03B9;<!-- ι --></mi>
  <mi>&#x03B4;<!-- δ --></mi>
  <mi>&#x03B9;<!-- ι --></mi>
  <mi>&#x03B1;<!-- α --></mi>
  <mi>&#x03C2;<!-- ς --></mi>
</math>
    </p>
        <p class="lead ">
    FEDEASLab is a modular research framework for the simulation of nonlinear structural response under static and dynamic loads, with a reference implementation written in Matlab©.
    </p>
    <a class="btn outline-FEDEASLab btn-lg" href="http://missing/link.html">Learn More</a>
    <a class="btn filled-FEDEASLab btn-lg" href="http://missing/link.html"
                    role="button">Try FEDEASLab &raquo;</a>
    </div>
    <div class="product-device box-shadow d-none d-md-block"></div>
    <div class="product-device product-device-2 box-shadow d-none d-md-block"></div>
</div>

</header>
<main role="main">

    <!-- Wrap the rest of the page in another container to center all the content. -->
    <div class="container marketing p-md-5">

    <div class="row featurette">
        <div class="col-md-7">
        <h2 class="featurette-heading">Post-Processing</h2>
        <p class="lead">Post-processing is accommodated in the program by generating a data object that carries all important material, element and structural information for plotting or printing. Several functions that address basic post-processing tasks are provided. The user can easily enhance and extend the current capabilities.</p>

        <a class="btn btn-outline-secondary" href="http://FEDEASLab/linktoPostlib.html" role="button">Post Library &raquo;</a>
        <a class="btn btn-secondary" href="https://mybinder.org/v2/gh/FEDEASLab/FEDEASLab-examples/master?filepath=notebooks%2Fbasics.ipynb" role="button">Try Now &raquo;</a>
        </div>

        <div class="col-md-5 code-block">
        <pre><code class="language-python">from FEDEASLab import jit
import random

@jit(nopython=True)
def monte_carlo_pi(nsamples):
acc = 0
for i in range(nsamples):
    x = random.random()
    y = random.random()
    if (x ** 2 + y ** 2) < 1.0:
        acc += 1
return 4.0 * acc / nsamples</code></pre>
        </div>
    </div>

    <hr class="featurette-divider">

    <div class="row featurette">
        <div class="col-md-7">
        <h2 class="featurette-heading">Built for Scientific Computing</h2>
        <p class="lead">FEDEASLab is designed to be used with NumPy arrays and functions.  FEDEASLab generates specialized code for
            different array data types and layouts to optimize performance.  Special decorators can create <a href="https://docs.scipy.org/doc/numpy/reference/ufuncs.html">universal functions</a> that broadcast over NumPy arrays just like NumPy functions do.</p>
        <p class="lead">FEDEASLab also works great with Jupyter notebooks for interactive computing, and with distributed execution frameworks, like Dask and Spark.</p>
        <a class="btn btn-outline-secondary" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/reference/numpysupported.html" role="button">Learn More &raquo;</a>
        <a class="btn btn-secondary" href="https://mybinder.org/v2/gh/FEDEASLab/FEDEASLab-examples/master?filepath=notebooks%2Fnumpy.ipynb" role="button">Try Now &raquo;</a>
        </div>
    
        <div class="col-md-5 code-block">
        <pre><code class="language-python">@FEDEASLab.jit(nopython=True, parallel=True)
def logistic_regression(Y, X, w, iterations):
for i in range(iterations):
    w -= np.dot(((1.0 /
            (1.0 + np.exp(-Y * np.dot(X, w)))
            - 1.0) * Y), X)
return w</code></pre>        
        </div>
    </div>

    <hr class="featurette-divider">

    <div class="row featurette">
    <h2 class="featurette-heading">State-of-the-art modeling</h2>
    <p>FEDEASLab offers functions for a wide spectrum of advanced modeling.</p>
    <div class="row">

        <div class="col-lg-4">
        <h2 class="mt-3">Simplified Threading</h2>
        <pre><code class="language-python">@jit(nopython=True, parallel=True)
def simulator(out):
# iterate loop in parallel
for i in prange(out.shape[0]):
    out[i] = run_sim()</code></pre>
        <p>FEDEASLab can automatically execute NumPy array expressions on multiple CPU cores and makes it easy to write parallel loops.</p>
        <p>
            <a class="btn btn-outline-secondary" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/user/parallel.html" role="button">Learn More &raquo;</a>
            <a class="btn btn-secondary" href="https://mybinder.org/v2/gh/FEDEASLab/FEDEASLab-examples/master?filepath=notebooks%2Fthreads.ipynb" role="button">Try Now &raquo;</a>
        </p>
        </div><!-- /.col-lg-4 -->
        <div class="col-lg-4">
        <h2 class="mt-3">Nonlinear</h2>
        <pre><code class="language-nasm">LBB0_8:
vmovups	(%rax,%rdx,4), %ymm0
vmovups	(%rcx,%rdx,4), %ymm1
vsubps	%ymm1, %ymm0, %ymm2
vaddps	%ymm2, %ymm2, %ymm2</code></pre>
        <p>FEDEASLab can automatically translate some loops into vector instructions for 2-4x speed improvements.  FEDEASLab adapts to your CPU capabilities, whether your CPU supports SSE, AVX, or AVX-512.</p>
        <p>
            <a class="btn btn-outline-secondary" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/user/performance-tips.html" role="button">Learn More &raquo;</a>
            <a class="btn btn-secondary" href="https://mybinder.org/v2/gh/FEDEASLab/FEDEASLab-examples/master?filepath=notebooks%2Fsimd.ipynb" role="button">Try Now &raquo;</a>
        </p>
        </div><!-- /.col-lg-4 -->
        <div class="col-lg-4">
        <h2 class="mt-3">Transient</h2>
        <p> Transient response under several support acceleration patterns is also included.</p>
        <p>
            <a class="btn btn-outline-secondary" href="http://FEDEASLab.pydata.org/FEDEASLab-doc/latest/cuda/index.html" role="button">Transient Library &raquo;</a>
            <a class="btn btn-outline-secondary" href="http://link-to-dynamic.library/index.html" role="button">FEDEASLab ROCm &raquo;</a>
        </p>
        </div><!-- /.col-lg-4 -->
    </div><!-- /.row -->
    </div>
    
<hr class="featurette-divider">

<div class="row featurette">
    <div class="col-md-12">
    <h2 class="featurette-heading">Education</h2>
    <p class="lead">Talk about use in the classroom, probably link to examples.</p>
    <p class="lead">FEDEASLab supports Intel and AMD x86, POWER8/9, and ARM CPUs, NVIDIA and  AMD GPUs, Python 2.7 and 3.4-3.7, as well as Windows/macOS/Linux.  Precompiled FEDEASLab binaries for most systems are available as conda packages and pip-installable wheels.</p>
    <a class="btn btn-outline-secondary" href="http://missing.link/fix.html" role="button">Learn More &raquo;</a>
    </div>
</div>
</div>

<hr class="featurette-divider">

<section id="supporters">

<div class="container supporters">
    <h2>Acknowledgements</h2>
    <p>FEDEASLab development is made possible through the current and/or past support of a number of organizations:<p>
    <div class="row">
    <div class="col supporter">
        <a href="https://ce.berkeley.edu/programs/semm"><img src="img/UCBEngineering_logo.png" alt="SEMM logo"></a>
    </div>
    <div class="col supporter">
        <a href="https://www.darpa.mil"><img src="_static/darpa_logo.png" alt="DARPA logo"></a>
    </div>
    <div class="col supporter">
        <a href="https://www.moore.org/grant-detail?grantId=GBMF5423"><img src="_static/moore_logo.png" alt="Moore foundation logo"></a>
    </div>
    </div>
    <div class="row">
    <div class="col supporter">
        <a href="https://www.intel.com"><img src="_static/intel_logo.png" alt="Intel logo"></a>
    </div>
    <div class="col supporter">
        <a href="https://www.nvidia.com/"><img src="_static/nvidia_logo.png" alt="NVIDIA logo"></a>
    </div>
    <div class="col supporter">
        <a href="https://www.amd.com"><img src="_static/amd_logo.png" alt="AMD logo"></a>
    </div>
    </div>
</div>
</section>

</main>

<!-- Code highlighting -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/prism.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/components/prism-python.min.js"></script>

</body>


