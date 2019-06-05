import os
from bioconvert.bam2wiggle import BAM2WIGGLE
from bioconvert import bioconvert_data
from easydev import TempFile, md5
import pytest



@pytest.mark.parametrize("method", BAM2WIGGLE.available_methods)
def test_conv(method):
    infile = bioconvert_data("test_measles.sorted.bam")
    outfile = bioconvert_data("test_bam2wiggle.wiggle")
    md5out = md5(outfile)

    with TempFile(suffix=".wiggle") as tempfile:
        convert = BAM2WIGGLE(infile, tempfile.name)
        convert(method=method)

        assert md5(tempfile.name) == md5out, "{} failed".format(method)

