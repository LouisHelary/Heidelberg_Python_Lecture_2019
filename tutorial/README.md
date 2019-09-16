# Tutorial

### How to run Python?

In general once Python has been installed to your computer, you just need to open a new shell and type:

```
$ python
```

This will open an interactive shell where you can try to type in some code. For example try:

```
> 2+2
```


### Autocompletion in a shell:

It can be very useful to enable the autocompletion in a python terminal. This can be achieved (for macos and linux user) by adding the following in your bashrc:

```
#Load python stuff:
export PYTHONSTARTUP=~/.pythonrc
```
And copy the attached .pythonrc file in your home directory. Once both actions are done you should have the autocompletion by typing the Tab key.

```
cp .pythonrc ~/.pythonrc
```
### Executing macro code:

It is possible to write some python code in a file using a text editor, and name it with the extension .py . Once this has been done it is possible to execute the code in a shell.

For instance let's create a HelloWorld.py file that will just display hello world. Copy the following in a shell:

```
$ echo "x=\"Hello World\"">>../python/HelloWorld.py
$ echo "print(x)">>../python/HelloWorld.py
```

This will create the file ../python/HelloWorld.py which will contain:
```
x="Hello World"
print(x)
```

If on just want to execute and quit this file, one just need to do:
```
$ python ../python/HelloWorld.py
```

If one want to start an interactive session and execute the file one need to do:

```
$ python -i ../python/HelloWorld.py
```

### Jupyter notebook:

While in a real life programming case you will most probably use the combo text editor - python shell, the tutorial will be done entirely using the jupyter notebook. This is a powerfull tool that allow to read and execute code simultaneously directly from a web browser!

In order to start a notebook, type the following from a shell:
```
$ jupyter-notebook
```

Now let's get started, open the different files one by one, and try to guess the instructions before running the output. At the end of each file there are some small exercices to do.

Note it is also possible to start the jupyter notebooks from the anaconda navigator by clicking on Launch under Jupyter Notebook.




