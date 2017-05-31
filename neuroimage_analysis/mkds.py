#!/usr/bin/python
"""
Construct HDF5 data files from NIFTI timeseries per subject.

Performs generation of input datasets for classification analysis. For each run
an HRF-modeling is performed using NiPy's GLM implementation, after spatial
smoothing of BOLD images with a Gaussian kernel of 2.0mm FWHM.

The output dataset contains one sample of beta weights per run per stimulation
category.

This script is called with a one-based subj index and yields an output dataset
in a data/ subdirectory.

Call once per subject.
"""

import sys
from os.path import join as _opj

from mvpa2.datasets.sources.openfmri import OpenFMRIDataset
from mvpa2.datasets.eventrelated import fit_event_hrf_model
from mvpa2.base.hdf5 import h5save
from nilearn.image import smooth_img
import nibabel as nb


# Set datapath to directory where Pandora data is
datapath = 'data'
of = OpenFMRIDataset(datapath)

# Increment first input argument to get subject number
sub = int(sys.argv[1]) + 1


def smooth(img):
    """Smoothing function from nilearn to be passed to pvmvpa."""
    nimg = smooth_img(img, fwhm=2.0)
    return nb.Nifti1Image(nimg.get_data(),
                          img.get_affine(),
                          header=img.get_header())


# With the OpenFMRIDataset source object imported above, PyMVPA knows how the
# dataset is organized and can parse the directory structure automatically to
# load the data from all runs.
ds = of.get_model_bold_dataset(
    model_id=1, subj_id=sub,
    flavor='dico_bold7Tp1_to_subjbold7Tp1',
    # full brain
    mask=_opj(
        datapath, 'sub%.3i' % sub, 'templates', 'bold7Tp1',
        'qa', 'jointfgbrainmask_bold7Tp1_to_subjbold7Tp1.nii.gz'),
    preproc_img=smooth,
    # HP filtering is done by NiPy's GLM
    modelfx=fit_event_hrf_model,
    time_attr='time_coords',
    condition_attr='condition')

h5save(_opj('data', 'sub%.3i_2.0mm_hrf.hdf5' % sub), ds)
