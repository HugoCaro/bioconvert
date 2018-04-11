# -*- coding: utf-8 -*-

###########################################################################
# Bioconvert is a project to facilitate the interconversion               #
# of life science data from one format to another.                        #
#                                                                         #
# Authors: see CONTRIBUTORS.rst                                           #
# Copyright © 2018  Institut Pasteur, Paris and CNRS.                     #
# See the COPYRIGHT file for details                                      #
#                                                                         #
# bioconvert is free software: you can redistribute it and/or modify      #
# it under the terms of the GNU General Public License as published by    #
# the Free Software Foundation, either version 3 of the License, or       #
# (at your option) any later version.                                     #
#                                                                         #
# bioconvert is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of          #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
# GNU General Public License for more details.                            #
#                                                                         #
# You should have received a copy of the GNU General Public License       #
# along with this program (COPYING file).                                 #
# If not, see <http://www.gnu.org/licenses/>.                             #
###########################################################################

""" description """

from bioconvert import ConvBase
from bioconvert.core.decorators import requires

__all__ = ["GENBANK2FASTA"]


class GENBANK2FASTA(ConvBase):
    """Convert :term:`GENBANK` file to :term:`FASTA` file"""
    _default_method = "biopython"

    def __init__(self, infile, outfile, *args, **kargs):
        """.. rubric:: constructor

        :param str infile: input GENBANK file
        :param str outfile: output EMBL filename

        """
        super(GENBANK2FASTA, self).__init__(infile, outfile, *args, **kargs)

        # squizz works as welll but keeps lower cases while biopython uses upper
        # cases

    @requires("squizz")
    def _method_squizz(self, *args, **kwargs):
        """Header is less informative than the one obtained with biopython"""
        cmd = "squizz {} -f genbank -c fasta > {} ".format(self.infile, self.outfile)
        self.execute(cmd)

    @requires(python_library="biopython")
    def _method_biopython(self, *args, **kwargs):
        from Bio import SeqIO
        SeqIO.convert(self.infile, "genbank", self.outfile, "fasta")
