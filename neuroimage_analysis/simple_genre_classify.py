"""Demonstrate multi-voxel pattern analysis with genre classification."""
from os.path import join as _opj

import numpy as np
from mvpa2.base.hdf5 import h5load
from mvpa2.mappers.zscore import zscore
from mvpa2.clfs.knn import kNN
from mvpa2.generators.partition import NFoldPartitioner
from mvpa2.measures.base import CrossValidation
from mvpa2.misc.errorfx import mean_match_accuracy

sub = 3
datapath = 'neuroimage_analysis/data'
ds = h5load(_opj(datapath, 'sub%.3i_2.0mm_hrf.hdf5' % sub))
ds.sa['targets'] = ds.sa.condition
zscore(ds, chunks_attr=None)

# Here, the chunks attribute indicates experimental runs
ds.chunks

# Create a k-nearest neighbors classifier to train
clf = kNN(k=2)
# Set up the cross validation
cv = CrossValidation(
        clf,
        NFoldPartitioner(),
        errorfx=mean_match_accuracy,
        enable_ca=['stats'])

# Perform the cross validation
cv_results = cv(ds)

# Inspect the results
print cv.ca.stats.as_string(description=True)
np.mean(cv_results)
