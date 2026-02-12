纳甲六爻排盘项目
================

[![image](https://img.shields.io/pypi/v/najia.svg)](https://pypi.python.org/pypi/najia)
[![image](https://img.shields.io/travis/bopo/najia.svg)](https://travis-ci.org/bopo/najia)
[![Documentation Status](https://readthedocs.org/projects/najia/badge/?version=latest)](https://najia.readthedocs.io/en/latest/?badge=latest)
[![Updates](https://pyup.io/repos/github/bopo/najia/shield.svg)](https://pyup.io/repos/github/bopo/najia/)

Python Boilerplate contains all the boilerplate you need to create a
Python package.

-   Free software: MIT license
-   Documentation: <https://najia.readthedocs.io>.

Features
--------

-   全部安易卦爻
-   函数独立编写
-   测试各个函数
-   重新命名函数
-   JSON数据存储（替代pickle）
-   完整的集成测试
-   改进的错误处理和代码质量

阳历，阴历（干支，旬空）

-   卦符: mark (001000)，自下而上
-   卦名: name
-   变爻: bian
-   卦宫: gong
-   六亲: qin6
-   六神: god6
-   世爻: shiy, ying
-   纳甲: naja
-   纳甲五行: dzwx
-   卦宫五行: gowx

修复问题
--------

-   ✓ 解决: 六神不对
-   ✓ 解决: 世应也有点小BUG , 地天泰卦的世爻为3, 应爻为6
-   ✓ 解决: 归魂卦世爻为3 此处返回4, 需要修改
-   ✓ 解决: 归魂卦的六亲是不对的问题, 变卦六亲现在使用初始卦所属的本宫卦来计算, 而不是按变卦所在的本宫卦

优化改进 (2025)
--------

-   ✓ 数据存储改进: 将guaci.pkl转换为JSON格式，提高可维护性
-   ✓ 代码质量提升: 移除反模式代码，使用命名常量替代魔术数字
-   ✓ 错误处理改进: 使用具体的异常类型(ValueError)替代空消息Exception
-   ✓ 测试覆盖增加: 新增5个集成测试，全面验证编译和渲染流程
-   ✓ 文档更新: 改进函数文档字符串，提高代码可读性

Credits
-------

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
