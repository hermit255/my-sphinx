# 概要
hnakamur/sphinx を使ったsphinx練習用プロジェクト
- blockdiag, blockdiag, PlantUML などの


## 注意点
`my-sphinx-quickstart` したときの conf.py テンプレートが
作成時点で動かない場合があるので注意すること

hnakamur/sphinx は高い完成度だが、個人作成なのでそんなこともある


## conf.pyの修正例

### hnakamur/sphinx:latest(2019/10 時点)の場合
https://github.com/hnakamur/docker-sphinx/tree/9a1504540cce85c8c4f1ae6003b56b82f5efac8a

#### L89

before
```
master_doc = ''
```
after
```
master_doc = 'index'
```

#### L240 - 243

before
```
html_theme = 'solar_theme'
import solar_theme
html_theme_path = [solar_theme.theme_path]
```
after
```
html_theme = 'sphinx_py3doc_enhanced_theme'
import sphinx_py3doc_enhanced_theme
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
```
