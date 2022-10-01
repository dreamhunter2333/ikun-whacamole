# 打地鼠 - 鸡你太美 ikun 版

## 安装

到 [Rlease 页面](https://github.com/jinmu333/ikun-whacamole/releases) 下载对应的安装包

![start](readme_assets/start.png)
![game1](readme_assets/game1.png)
![game2](readme_assets/game2.png)
![end](readme_assets/end.png)

## 开发

```bash
python3 -m venv ./venv
./venv/bin/python3 -m pip install pygame
./venv/bin/python3 main.py
# 打包
./venv/bin/pyinstaller -F -w -i main.ico main.py -p bucket.py -p config.py -p kun.py -p tools.py --add-data "resources:resources"
```

## 参考

[https://github.com/CharlesPikachu/Games](https://github.com/CharlesPikachu/Games)
