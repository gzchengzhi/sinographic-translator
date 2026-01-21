# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 15:56:55 2026

@author: gzche
"""

"""
Sinographic Translator - Convert English words to Chinese characters based on roots
"""

from .converter import SmartConverter
from .sentence_converter import SentenceConverter
from .matcher import EnhancedMatcher, MatchStrategy
from .data_loader import load_and_fix_root_data, create_minimal_test_data

__version__ = "0.1.0"
__author__ = "Your Name"
__all__ = [
    "SmartConverter",
    "SentenceConverter", 
    "EnhancedMatcher",
    "MatchStrategy",
    "load_and_fix_root_data",
    "create_minimal_test_data",
]