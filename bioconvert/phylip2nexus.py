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

"""PHYLIP2NEXUS conversion"""
import os

import colorlog
from Bio import SeqIO

from bioconvert import ConvBase
from bioconvert.core.decorators import requires

_log = colorlog.getLogger(__name__)


__all__ = ['PHYLIP2NEXUS']


class PHYLIP2NEXUS(ConvBase):
    """
    Converts a sequence alignment from :term:`PHYLIP` format to :term:`NEXUS` format. ::
    """
    _default_method = 'goalign'

    def __init__(self, infile, outfile=None, *args, **kwargs):
        """.. rubric:: constructor

        :param str infile: input :term:`PHYLIP` file.
        :param str outfile: (optional) output :term:`NEXUS` file
        """
        super().__init__(infile, outfile)

    @requires("conda")
    def _method_goalign(self, *args, **kwargs):
        """
        Convert :term:`PHYLIP` interleaved file in :term:`NEXUS` format using goalign tool.
        https://github.com/fredericlemoine/goalign

        """
        self.install_tool('goalign')
        cmd = 'goalign reformat nexus -i {infile} -o {outfile} -p'.format(
            infile=self.infile,
            outfile=self.outfile)
        self.execute(cmd)
