# :microscope: Pairwise Sequence Aligment Tool (PSAT) :microscope:

This repository offers a simple application to align sequences of proteins or amino acids. On PSAT you will find some options of sequence alignment such as global alignment, implemented using the Needleman-Wunsh algorithm, and local alignment, using the Smith-Waterman algorithm.

![PSAT UI](https://github.com/mgfzemor/Pairwise-sequence-Aligment-Tool/blob/master/docs/img/aligment.png)

```bash
$ git clone https://github.com/mgfzemor/Pairwise-sequence-Aligment-Tool.git
```
### :floppy_disk: Prerequisites
To have this running your local machine, you only must have a Python version = 3.* and a Virtualenv tool. 

Learn more about [Virtualenv](https://virtualenv.pypa.io/en/latest/), which is pretty useful to manage isolated Python environments.
- Installing Virtualenv
```bash
$ sudo apt-get install virtualenv
```

### :zap: Getting Started
- Install application requirements listed above
- clone project

```bash
$ git clone https://github.com/mgfzemor/Pairwise-sequence-Aligment-Tool.git
```
- Go to project path and create a virtual environment

```bash
$ cd Pairwise-sequence-Aligment-Tool/ && virtualenv env
```

- Active the virtualenv and install requirements
```bash
$ . env/bin/activate && pip install -r requirements.txt
```

- Run application
```bash
$ flask run
```
