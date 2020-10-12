#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Yahoo! Finance market data downloader (+fix for Pandas Datareader)
# https://github.com/ranaroussi/fix-yahoo-finance
#
# Copyright 2017-2019 Ran Aroussi
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import yfinance

__version__ = 'yfinance v. ' + yfinance.__version__
__author__ = yfinance.__author__

Ticker = yfinance.download
download = yfinance.download
pdr_override = yfinance.download

def get_yahoo_crumb(*args, **kwargs):
    pass

def parse_ticker_csv(*args, **kwargs):
    pass

__all__ = yfinance.__all__ + ['get_yahoo_crumb', 'parse_ticker_csv']

import warnings

warnings.showwarning("""

*** `fix_yahoo_finance` was renamed to `yfinance`. ***
Please install and use `yfinance` directly using `pip install yfinance -U`

More information: https://github.com/ranaroussi/yfinance
""",
DeprecationWarning, __file__, 0)
