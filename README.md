# pysta-dulwich


[Pythonista 3](http://omz-software.com/pythonista/) で、[dulwich](https://github.com/dulwich/dulwich) をどうにかしたいリポジトリ



## 作業方法

`site-packages` に dulwich を入れずに


``` import.py
sys.path.insert(0, os.path.abspath('../dulwich'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))
dulwich = __import__('dulwich')
```

これでをメインファイルに記載して、ディレクトリからimport している(兄弟の階層の場合)

> 3系の書き方としてどうなのかな？🤔

