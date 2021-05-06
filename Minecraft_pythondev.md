以Fedora33 workstation操作系统为例（其它linux操作系统只是个别命令不同），如果是WINDOWS系统，建议使用visualbox建立虚拟机


1、下载并初次运行Spigot

（1）下载buildtools

```Bash
$mkdir  ~/Spigot1.16.5
$ cd ~/Spigot1.16.5
$wget https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
```
(2)生成 Spigot jar 1.16.5
```Bash
$java -jar BuildTools.jar --rev 1.16.5
```
(3)运行一次
```Bash
java -Xms2048M -Xmx2048M  -jar spigot-1.16.5.jar nogui
```
然后eula改为true，同意协议
```Bash
$ vi eula.txt
$ cat eula.txt
#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).
#Tue Apr 27 12:51:10 CST 2021
eula=true
```
2、启动服务器


（1）调整参数

server.properties是储存多人游戏服务器所有设置的文件。在编辑server.properties时，以#开头的行为注释。

保存了server.properties的更改之后，服务端必须重新启动才能使更改生效。

具体参数含义见：https://minecraft.fandom.com/zh/wiki/Server.properties

```Bash
 $vi server.properties
 ```


a.生存模式修改为创造模式

```Bash
gamemode=survival改为gamemode=creative
```

b.离线模式，不会每次校验客户端账号
```Bash
online-mode=true改为online-mode=false
```
3、Python接口插件

（1）如果没有安装maven，请安装好maven。


```Bash
$sudo yum install maven 

$cd ~/Spigot1.16.5
$git clone https://github.com/wensheng/JuicyRaspberryPie 
$cd ./JuicyRaspberryPie/bukkit
$mvn clean package
$mkdir -p ~/Spigot1.16.5/plugins
$mv ./target/juicyraspberrypie-1.16.5.jar ~/Spigot1.16.5/plugins/
```

（2）运行服务器

```Bash
$cd ~/Spigot1.16.5
$java -Xms2048M -Xmx2048M  -jar spigot-1.16.5.jar
```
（3）退出服务器
```Bash
>stop
```
（4）查看python3路径是否正确
```Bash
$ whereis python3
python3: /usr/bin/python3.9 /usr/bin/python3 /usr/lib/python3.9 /usr/lib64/python3.9 /usr/include/python3.9 /usr/share/man/man1/python3.1.gz

$ cat ~/Spigot1.16.5/plugins/JuicyRaspberryPie/config.yml
api_port: 4711
start_cmdsvr: false
cmdsvr_host: "localhost"
cmdsvr_port: 4731
pyexe: "/usr/bin/python3"
# windows pyexe example
# pyexe: "C:\\Users\\wensheng\\Anaconda3\\python.exe"
```
（5）关闭fedora防火墙
```Bash
$ sudo systemctl disable firewalld.service
```
（6）运行之前服务器
```Bash
$java -Xms2048M -Xmx2048M  -jar spigot-1.16.5.jar
```
4、开发环境测试

配置完毕后，测试运行一下

1)运行服务器（如果服务器已经运行，可忽略这一步，也可使用stop命令停止服务器运行）

2)运行客户端，选择多人游戏，然后，加入服务器127.0.0.1。

3)输入hello,world代码，测试Python脚本可否成功运行。

（1）在电脑上新建目录，并录入代码。

```Bash
$mkdir ~/mc_py
$cp -r ~/Spigot1.16.5/JuicyRaspberryPie/bukkit/src/main/resources/* ~/mc_py/
$cd ~/mc_py
$vi sayHello.py
```
```python
# coding:utf8

# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft

# 建立mc连接对象
mc = minecraft.Minecraft.create()

# 发送消息
mc.postToChat("hello,world")

# 获得玩家位置
pos = mc.player.getTilePos()
# 创建两个block
mc.setBlock(pos.x + 1, pos.y + 1, pos.z, "minecraft:mossy_cobblestone") #注意： "minecraft:mossy_cobblestone" 而不是48
mc.setBlock(pos.x + 1, pos.y + 2, pos.z, "minecraft:magma_block")
```
（2）运行第（1）步输入的脚本
```Bash
$python3 sayHello.py
```
可在客户端界面的左下角处看到“hello,world”输出。

5、运行模式

有2种常用的运行模式：

在本地模式下，客户端和服务器端为同一电脑同一IP地址。前面讲解了本地模式的运行方式。

局域网模式下，服务器端和客户端不在同一台电脑，服务器为局域网服务器。

运行方式如下：


（1）客户端启动后，选择多人，添加并登录本地服务器（局域网服务器的IP地址）。

（2）首先，在客户端电脑上新建一目录my_world，然后，将前面下载的JuicyRaspberryPie软件包中JuicyRaspberryPie/bukkit/src/main/resources/目录下的文件拷贝my_world目录下，最后，新建sayHello.py程序，程序如下：

```python
# coding:utf8

# 引入mcpi目录下的mcpi.minecraft
import mcpi.minecraft as minecraft
import datetime

# 建立mc连接对象
mc = minecraft.Minecraft.create("192.168.10.9")


# 发送消息
now = datetime.datetime.now()
nowStr=now.strftime("%Y/%m/%d")
mc.postToChat(f"今天是：{nowStr}，欢迎")

# 获得玩家位置
pos = mc.player.getTilePos()
# 创建两个block
mc.setBlock(pos.x + 1, pos.y + 1, pos.z, "minecraft:mossy_cobblestone") 
mc.setBlock(pos.x + 1, pos.y + 2, pos.z, "minecraft:magma_block")
```
（3）运行第（3）步输入的脚本
```Bash
$python3 sayHello.py
```


（3）运行第（3）步输入的脚本
```Bash
$python3 sayHello.py
```
可在客户端界面的左下角处看到“hello,world”输出。

