import pytest
from easydev import TempFile, md5

from bioconvert import bioconvert_data
from bioconvert.phylip2fasta import PHYLIP2FASTA


@pytest.mark.parametrize("method", PHYLIP2FASTA.available_methods)
def test_fa2phy_biopython(method):
    if method == "goalign":
        #FIXME
        #https://github.com/evolbioinfo/goalign/issues/3
        pass
    else:
        infile = bioconvert_data("biopython.phylip")
        outfile = bioconvert_data("biopython.fasta")
        with TempFile(suffix=".phylip") as tempfile:
            converter = PHYLIP2FASTA(infile, tempfile.name)
            converter(method=method)

            # Check that the output is correct with a checksum
            if method in ["squizz", "goalign"]:
                assert md5(tempfile.name) == "98b661ab0f22ab6d4172135686cfc363"
            else:
                assert md5(tempfile.name) == md5(outfile)
