# 打地鼠 - 鸡你太美 ikun 版

## 安装

到 [Rlease 页面](https://github.com/dreamhunter2333/ikun-whacamole/releases) 下载对应的安装包

![start](readme_assets/start.png)
![game1](readme_assets/game1.png)
![game2](readme_assets/game2.png)
![end](readme_assets/end.png)

## 开发

mac

```bash
python3 -m venv ./venv
./venv/bin/python3 -m pip install pygame pyinstaller
# 运行
./venv/bin/python3 main.py
# 打包
./venv/bin/pyinstaller -F -w -i main.ico main.py -p bucket.py -p config.py -p kun.py -p tools.py --add-data "resources:resources" -n ikun
```

win

```cmd
python -m venv ./venv
.\venv\Scripts\python -m pip install pygame pyinstaller
# 运行
.\venv\Scripts\python main.py
# 打包
.\venv\Scripts\pyinstaller.exe -F -w -i main.ico main.py -p bucket.py -p config.py -p kun.py -p tools.py --add-data "resources;resources" -n ikun
```

## 参考

[https://github.com/CharlesPikachu/Games](https://github.com/CharlesPikachu/Games)
