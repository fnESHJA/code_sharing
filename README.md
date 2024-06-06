# -
代码存储（分享用）

用于存储代码，作用约等于网盘

# 原文JSON和MTool的译文JSON合并.py

因为t++从RPG游戏导出的翻译文件中，很多的行会同时包含代码、换行符等奇奇怪怪的东西，导致无法匹配上。于是这边（让AI帮忙）写了一个python代码。代码可以对transDic.output.json里面的每个键值对，把里面的非ASCII字符串导出来，用TrsData.json里面的翻译好的字符串替换，最后塞回到值里面保存。

使用方法就是先不把Mtool的JSON放进去，在SExtractor用正则表达式

'''
22_search=^([\s\S]+)$
extraData=^Original Text$
writeOffset=1
'''

跑一遍，得到没有译文的transDic.output.json。之后把Mtool的JSON重命名为TrsData.json，把这两个json和代码放在一起，跑一遍代码，输出transDic.json。最后把transDic.json放到ctrl文件夹里面，再跑一遍SExtractor，就行了。这个方法应该能够翻译绝大部分的文本。

这个代码对应的是直接使用mtool导出并翻译得到的json文件。因为保留了非ascii的代码字符，游戏应该不会出现没声音或者崩溃的BUG吧（之前是直接用T++翻译文件跑的AI翻译，跑出来的补丁总有一堆BUG）。
