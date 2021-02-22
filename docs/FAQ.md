# Frequently Asked Questions

> `Error using optimoptions. Invalid solver specified. Provide a solver name or handle (such as 'fmincon' or @fminunc). Type DOC OPTIMOPTIONS for a list of solvers.`

The Matlab user group reports this error for older versions of Matlab or for missing the global optimization toolbox in a more recent version.

If you believe that you are using Matlab 2019b make sure that the following directories are on your path

    - C:\Program Files\MATLAB\R2019b\toolbox\optim\optim
    - C:\Program Files\MATLAB\R2019b\toolbox\optim
    - C:\Program Files\MATLAB\R2019b\toolbox\optim\optimdemos
    - C:\Program Files\MATLAB\R2019b\toolbox\optim\problemdef
    - C:\Program Files\MATLAB\R2019b\toolbox\globaloptim
    - C:\Program Files\MATLAB\R2019b\toolbox\globaloptim\globaloptim
    - C:\Program Files\MATLAB\R2019b\toolbox\globaloptim\globaloptimdemos

in Matlab 2019b (by typing "path" at the command prompt).