# Instructions to workshop participants
Participants are invited to bring their laptop to the workshop and follow along with the workshop demonstrations. To make sure that you are able to follow along, please complete the following steps prior to the workshop. Detailed instructions for the steps are provided below.

1. Verify that you have python 2.7 and all necessary dependencies installed.
2. Download this git repository (**clone** it) to get the Jupyter notebooks and datasets that will be used in the workshop.
3. Run the script `check_env.py` found in this git repository to verify that your python environment it prepared for the workshop.
4. (Optional) If you want to follow along with the neuroimage analysis part of the workshop, download the fMRI dataset and install necessary dependencies.


## Detailed Instructions

### Step 1: Python install
Choose the option that applies to you.
* **Option 1**: If you already have python 2.7 installed and you are comfortable with installing python packages, please make sure that you have the following packages installed.
  * pandas (0.20.1)
  * scikit-learn (0.18.1)
  * matplotlib (2.0.2)
  * seaborn (0.7.1)
  * numpy (1.12.1)
  * jupyter (1.0.0)

For example, you can install these packages using `pip`:
```
pip install pandas scikit-learn matplotlib seaborn numpy jupyter
```

* **Option 2**: If you don't already have python installed (or you want to start fresh), you want to get everything you need in one shot, and you have plenty of available storage on your laptop, download Anaconda for python 2.7 [here](https://www.continuum.io/downloads).
* **Option 3**: If you don't want all 720 packages that come with Anaconda, download miniconda for python 2.7 [here](https://conda.io/miniconda.html). You can install all the packages you need with conda, the package and environment manager that comes with miniconda. Run the following command install the above packages along with a number of additional dependencies:
```
conda install python=2.7 pandas scikit-learn matplotlib seaborn numpy jupyter
```

*Note* that if you haven't yet got Python installed, that may mean you are not familiar with the basics of Python programming. Make sure you brush up on the basics using a good tutorial (a quick search will reveal many candidates) before the workshop.


### Step 2: Clone this git repository
This repository, hosted on github, contains the materials that we will use in the workshop. Make sure you have [git](https://www.atlassian.com/git/tutorials/install-git) installed, and then [clone the repository](https://help.github.com/articles/cloning-a-repository/) with the command:

```
git clone git@github.com:florisvanvugt/workshop4june2017.git
```

### Step 3: Run check_env.py to check that dependencies are installed properly
This repository contains the python script `check_env.py` which will try to import all the various libraries that we will use in the workshop.
```
python check_env.py
```

An error message will be displayed if something is missing. Otherwise, you're all set!

### Step 4 (Optional): Download neuroimaging data and install additional dependencies
The last section of the workshop will use a [freely available high-resolution 7-Tesla fMRI dataset](https://openfmri.org/dataset/ds000113b/) from an experiment on the perception of musical genres. This data is very large (~30 GB) so you may not want to put it on your laptop. Some of the analyses we will go over will take too long to run during the workshop. However, if you want to follow along and finish running the analyses at home.
1. Get the data
  * Install [git-annex](https://git-annex.branchable.com/)
  * `git clone http://psydata.ovgu.de/forrest_gump/.git data`
  * `cd data`
  * ```
  git-annex get stimulus/task002/ \
  sub*/BOLD/task002_run*/bold_dico_bold7Tp1_to_subjbold7Tp1.nii.gz \
  models/model001/* \
  sub*/templates/bold7Tp1/qa/jointfgbrainmask_bold7Tp1_to_subjbold7Tp1.nii.gz \
  sub*/model/model001/*
  ```

2. Install the following Python packages (available via conda or pip):
  * scipy
  * [pymvpa](http://www.pymvpa.org/installation.html#requirements)
  * nibabel
  * nilearn
  * h5py
  * nipy
  * lxml

This data was obtained from the OpenfMRI database. Its accession number is ds000113b.

[Hanke M, Dinga R, Häusler C et al. High-resolution 7-Tesla fMRI data on the perception of musical genres – an extension to the studyforrest dataset. F1000Research 2015, 4:174 ](https://f1000research.com/articles/4-174/v1)


## Opening the Jupyter Notebooks

We will teach the workshop from so-called [Jupyter Notebooks](http://jupyter.org/). We have added them to this repository so you can download them and follow along, and also refer back to them in the future. Simply click on them in Github to see their contents. Once downloaded, if you want to view them or execute code within them, you need to first run the **Jupyter Notebook App** as described here: [How to run a Jupyter Notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html). Make sure you run the notebook app in the folder where you downloaded the notebooks.
