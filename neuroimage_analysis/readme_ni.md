
# Introduction to machine learning for neuroimage analysis in python

The scripts in this directory are highly influenced by the pyMVPA tutorial and the example scripts for the OpenfMRI.org musical genres dataset found [here](https://github.com/psychoinformatics-de/studyforrest-paper-pandoradata).

These scripts assume that the data from the repository <http://psydata.ovgu.de/forrest_gump/.git> is in a subdirectory 'data' and that git-annex was used to retrieve at least the data for subject 001:
```
git-annex get stimulus/task002/ \
sub001/BOLD/task002_run*/bold_dico_bold7Tp1_to_subjbold7Tp1.nii.gz \
models/model001/* \
sub001/templates/bold7Tp1/qa/jointfgbrainmask_bold7Tp1_to_subjbold7Tp1.nii.gz \
sub*/model/model001/*
```
## Scripts

### `mkds.py`

Performs generation of input datasets for classification analysis. For each run
an HRF-modeling is performed using NiPy's GLM implementation, after spatial
smoothing of BOLD images with a Gaussian kernel of 2.0mm FWHM.

The output dataset contains one sample of beta weights per run per stimulation
category.

This script is called with a one-based subject index and yields an output
dataset in a data/ subdirectory.

Call once per subject.

### `simple_genre_classify.py`
Performs cross-validated genre classification with a kNN classifier using
whole-brain data from one subject.

### `dosl.sh`
Bash shell script to perform a searchlight analysis on one subject using the
pymvpa command line interface.

The specific analysis classification and preprocessing setup is taken from the
pymvpa2_cv_setup.py, pymvpa2_zscore_ds.py script snippet files.

The searchlight is configured to be of a radius of two voxels (plus the
center), and searchlight centers are spaced two voxels appart. This performs a
sparse spatial sampling with overlapping searchlight sphere. The values mapped
onto each voxel represent the mean accuracy across all classification (spheres)
a voxel was included in.

The output is one result searchlight map in the results/ subdirectory.

Call once per subject and desired searchlight map.

### `load_sl_results.py`
Loads the searchlight results in hdf and converts and saves them to nifti
format so that they can be opened in common neuroimaging software.

### `pymvpa2_zscore_ds.py`
Auxillary script passed to the pymvpa command line interface in `dosl.sh`

### `pymvpa2_cv_setup.py`
Auxillary script passed to the pymvpa command line interface in `dosl.sh`
