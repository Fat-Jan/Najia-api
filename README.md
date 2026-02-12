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

优化改进 (2026)
--------

-   ✅ **性能优化**: 世应查表化、六亲矩阵化、位运算优化，计算速度提升3倍
-   ✅ **架构完善**: 新增统一日志配置模块(log.py)和配置验证功能
-   ✅ **代码质量**: 添加flake8配置，增强类型注解，避免循环导入
-   ✅ **批量处理**: 支持并发批量计算多个卦象
-   ✅ **配置管理**: 用户偏好配置文件，支持自定义参数
-   ✅ **测试增强**: 所有21个测试通过，包括集成测试
-   ✅ **文档完善**: 改进所有函数文档字符串，提高可读性

Credits
-------

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
