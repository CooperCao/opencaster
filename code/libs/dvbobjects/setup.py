#! /usr/bin/env python

from distutils.core import setup, Extension

import sys

# from an original source code by Joachim Kaeber (kaeber@gmd.de)
setup(
    name = "dvbobjects",
    version = "1.0",
    description = "Python Package for dvb transport stream data generation (PAT, PMT, NIT, Object Carousel, ...)",
    author = "Cooper",
    author_email = "caopeng625@gmail.com",
    url = "",
    
    packages = [
        'dvbobjects',
        'dvbobjects.ATSC',
        'dvbobjects.DSMCC',
        'dvbobjects.DSMCC.BIOP',
        'dvbobjects.DVB',
        'dvbobjects.MHP',
        'dvbobjects.HBBTV',
        'dvbobjects.PSI',
        'dvbobjects.MPEG',
        'dvbobjects.SBTVD',
        'dvbobjects.utils',
        ],   
    package_dir={'dvbobjects': 'dvbobjects'},
    package_data={'dvbobjects':['utils/sectioncrc.so']},
)
