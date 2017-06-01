"""Defines function to perform zscoring."""
from mvpa2.mappers.zscore import zscore


def fx(ds):
    """z-score the data."""
    zscore(ds, chunks_attr=None)
    return ds
