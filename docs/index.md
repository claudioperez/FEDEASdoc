---
hide_toc: true
---

<!-- # FEDEASLab -->

<body>

<header>


<div class="hero position-relative overflow-hidden p-3 text-center text-dark">
    <div class="col-md-5 p-lg-1 mx-auto my-5">
    <!-- <img src="_static/FEDEASLab-logo.svg" style="max-width: 30rem;" alt="FEDEASLab logo"> -->
        <!-- <p class="lead font-weight-normal"> -->
        <p>
        <h2 class="featurette-heading">  
<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mi mathvariant="normal">&#x03A6;<!-- Φ --></mi>
  <mi>&#x03F5;<!-- ϵ --></mi>
  <mi>&#x03B9;<!-- ι --></mi>
  <mi>&#x03B4;<!-- δ --></mi>
  <mi>&#x03B9;<!-- ι --></mi>
  <mi>&#x03B1;<!-- α --></mi>
  <mi>&#x03C2;<!-- ς --></mi>
</math>
    </h2>
    </p>
        <p class="lead ">
    FEDEASLab is a modular research framework for the simulation of nonlinear structural response under static and dynamic loads, with a reference implementation written in <a href="https://www.mathworks.com/products/matlab.html">Matlab©</a>.
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
    <p class="lead">FEDEASLab development is made possible through the current and/or past support of a number of organizations:<p>
    <div class="row">
    <div class="col supporter">
        <a href="https://ce.berkeley.edu/programs/semm"><img src="img/UCBEngineering_logo.png" alt="SEMM logo"></a>
    </div>
    <div class="col supporter">
        <a href="https://www.support.link.2"><img src="_static/support_logo_2.png" alt="Support logo 2"></a>
    </div>
    </div>
    <div class="row">
    <div class="col supporter">
        <a href="https://www.support_link3.missing"><img src="_static/support_logo_3.png" alt="Support logo 3"></a>
    </div>
    <div class="col supporter">
        <a href=""><img src="_static/nvidia_logo.png" alt="Support logo 4"></a>
    </div>
    </div>
</div>
</section>

</main>

<!-- Code highlighting -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/prism.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.6.0/components/prism-python.min.js"></script>

</body>


