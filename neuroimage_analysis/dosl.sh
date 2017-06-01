#!/bin/bash

# Performs a searchlight analysis using the pymvpa2 command line interface

# The specific analysis classification and preprocessing setup is taken from the
# pymvpa2_cv_setup.py, pymvpa2_zscore_ds.py script snippet files.
#
# The searchlight is configured to be of a radius of two voxels (plus the
# center), and searchlight centers are spaced two voxels appart. This performs a
# sparse spatial sampling with overlapping searchlight sphere. The values mapped
# onto each voxel represent the mean accuracy across all classification (spheres)
# a voxel was included in.
#
# The output is one result searchlight map in the results/ subdirectory.
#
# Call once per subject and desired searchlight map.

# Set datadir to point to directory where data can be found
datadir='data'
# Zero pad the first input argument as the subject identifier
sub=$(printf "%03d\n" $1 )
echo Performing searchlight analysis on subject $sub ...

# Call the pymvpa2 command
pymvpa2 searchlight \
			-i ${datadir}/sub${sub}_2.0mm_hrf.hdf5 \
			--ds-preproc-fx pymvpa2_zscore_ds.py \
			--payload pymvpa2_cv_setup.py \
			--neighbors 2 \
			--scatter-rois 2 \
			--nproc 1 \
			-o results/sub${sub}_2.0mm_hrf_sl_orig.hdf5
