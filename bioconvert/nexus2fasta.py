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

"""NEXUS2FASTA conversion"""
import os

import colorlog
from Bio import SeqIO

from bioconvert import ConvBase
from bioconvert.core.decorators import requires

_log = colorlog.getLogger(__name__)


__all__ = ['NEXUS2FASTA']


class NEXUS2FASTA(ConvBase):
    """
    Converts a sequence alignment from :term:`NEXUS` format to :term:`FASTA` format. ::
    """
    _default_method = 'goalign'

    def __init__(self, infile, outfile=None, alphabet=None, *args, **kwargs):
        """.. rubric:: constructor

        :param str infile: input :term:`NEXUS` file.
        :param str outfile: (optional) output :term:`FASTA` file
        """
        super().__init__(infile, outfile)
        self.alphabet = alphabet

    @requires("conda")
    def _method_goalign(self, threads=None, *args, **kwargs):
        """
        Convert :term:`NEXUS` interleaved file in :term:`FASTA` format using goalign tool.
        https://github.com/fredericlemoine/goalign

        :param threads: not used.
        """
        self.install_tool('goalign')
        cmd = 'goalign reformat fasta -i {infile} -o {outfile} -x'.format(
            infile=self.infile,
            outfile=self.outfile)
        self.execute(cmd)
