# Waterfall
瀑布流图片查看

Flask 学习实例 (＾－＾)V

#### 插件使用备忘

辨识设备类型：https://theapicompany.com/

#### 安装使用 python 3.7.5

#### 安装 Flask 1.1.1

    $ pip install Flask

#### 启动

可以使用 flask 命令或者 python 的 -m 开关来运行这个应用。在 运行应用之前，需要在终端里导出 FLASK_APP 环境变量:

    $ export FLASK_APP=hello.py
    $ flask run

    - Running on http://127.0.0.1:5000/

如果是在 Windows 下，那么导出环境变量的语法取决于使用的是哪种命令行解释器。  
在 Command Prompt 下:

    
    C:\path\to\app>set FLASK_APP=hello.py

在 PowerShell 下:

    PS C:\path\to\app> $env:FLASK_APP = "hello.py"

还可以使用 python -m flask:

    $ export FLASK_APP=hello.py
    $ python -m flask run

    - Running on http://127.0.0.1:5000/

#### 调试模式

如果需要打开所有开发功能（包括调试模式），那么要在运行服务器之前导出 FLASK_ENV 环境变量并把其设置为 development:

    $ export FLASK_ENV=development
    $ flask run

（在 Windows 下需要使用 set 来代替 export 。）

windows vscode:

    $env:FLASK_APP = "Flaskr"
    $env:FLASK_ENV = "development"
    flask run

##### 更改启动端口
    flask run -p 7000

##### SO
    $env:FLASK_APP = "setup.py"
    $env:FLASK_ENV = "development"
    flask run -p 7000

    export FLASK_APP=setup.py
    export FLASK_ENV=development
    flask run -p 7000
    
这样可以实现以下功能：

1. 激活调试器。

2. 激活自动重载。

3. 打开 Flask 应用的调试模式。

### 初始化数据库

1、设置环境

    $env:FLASK_APP = "setup.py"
    $env:FLASK_ENV = "development"

2、初始化

    flask init-db
    #代码在 db.py init_db_command()
    






