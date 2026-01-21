# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 15:59:10 2026

@author: gzche
"""

#!/usr/bin/env python3
"""
基本使用示例
"""

from sinographic_translator import SentenceConverter, SmartConverter

def main():
    print("=== Sinographic Translator 示例 ===")
    
    # 创建转换器
    converter = SentenceConverter()
    
    # 示例1：转换单词
    print("\n1. 单词转换示例:")
    test_words = ["biology", "happiness", "president", "international"]
    
    for word in test_words:
        result = converter.converter.convert_word(word, detailed=True)
        print(f"{word:15} → {result['hanzi']:10}")
        if result['decomposition']:
            for comp in result['decomposition']:
                print(f"    {comp['element']} → {comp['hanzi']}")
    
    # 示例2：转换句子
    print("\n2. 句子转换示例:")
    sentences = [
        "Science and technology are developing rapidly.",
        "Education is important for personal development.",
        "The president gave a speech about international cooperation."
    ]
    
    for i, sentence in enumerate(sentences, 1):
        print(f"\n句子 {i}: {sentence}")
        result = converter.convert_sentence(sentence, "hybrid")
        print(f"转换结果: {result['converted']}")
    
    # 示例3：分析句子
    print("\n3. 句子分析示例:")
    sentence = "Computer science education"
    analysis = converter.analyze_sentence(sentence)
    
    print(f"句子: {sentence}")
    print(f"单词数: {analysis['word_count']}")
    print(f"成功率: {analysis['statistics']['success_count']}/{analysis['statistics']['total_words']}")
    
    for word_analysis in analysis['words']:
        print(f"\n{word_analysis['word']}:")
        print(f"  汉字: {word_analysis['hanzi']}")
        if word_analysis['decomposition']:
            print(f"  拆解: ", end="")
            for comp in word_analysis['decomposition']:
                print(f"{comp['element']}({comp['hanzi']}) ", end="")
            print()

if __name__ == "__main__":
    main()