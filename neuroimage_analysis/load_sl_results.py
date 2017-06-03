"""Load searchlight results and save to nifti format."""
from os.path import join as _opj
import numpy as np
from mvpa2.base.hdf5 import h5load
from mvpa2.datasets.mri import map2nifti

sub = 1
sl_res = h5load(_opj('results', 'sub%.3i_2.0mm_hrf_sl_orig.hdf5' % sub))
np.mean(sl_res)

# Convert and save to NIFTI format
sl_res_nii = map2nifti(sl_res)
sl_res_nii.to_filename(_opj('results', 'sub%.3i_2.0mm_hrf_sl_orig.nii' % sub))
