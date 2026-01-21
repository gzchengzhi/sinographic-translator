# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 11:53:45 2026

@author: gzche
"""

from sinographic_translator import SentenceConverter

# 创建转换器
converter = SentenceConverter()

# 转换单词
result = converter.convert_word("president", detailed=True)
print(f"单词: {result['word']}")
print(f"汉字: {result['hanzi']}")  # 输出: 前坐的

# 转换句子
sentence = "The president gave a speech about international cooperation."
result = converter.convert_sentence(sentence, "hybrid")
print(result['converted'])  # 输出: The(那) president(前的) gave a speech(说) about international(间的) cooperation(作).