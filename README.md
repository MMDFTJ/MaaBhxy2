# MAABhxy2.0测试版

基于MAA全新架构的崩崩（崩坏学园2）小助手，图像技术 + 模拟控制，解放双手！由 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 强力驱动！纯python（雾）

### 新增UI

## 功能介绍

#### 目前已有功能：

##### 清日常

* ~~启动游戏~~
* 领取/派遣使魔
* 垃圾屋刷新，
* 礼包商店的零时之种购买（应该不会出错买错别的礼包，出bug买错了一律不负责）
* 自动刷多元裂缝，
* 自动刷崩科校活，领使魔碎片
* 领取社团体力
* 自动刷当前活动的BONUS（双倍卷刷三次）
* 领取存在感

##### 重复刷取某一关

* 可选是否使用双倍卷
* 可填重复刷取次数

后面会有的功能（大概）：

* [x] 重复刷同一关卡（需要手动进入重复刷的关卡）
* [ ] 重复刷同一关卡遇到游戏闪退自动重启进入当前关卡继续刷
* [ ] 模拟器多开控制
* [x] UI界面

已知问题

* **AEZAKMI**有几率走出跑道，跑歪就手动走进去一下叭，过完图就正常了（

## 前置说明

Q:会不会检测到后封号？
A:不知道...是通过adb模拟点击的，**用别怕，怕别用**(雾

## 使用说明

**先打开模拟器，分辨率设置为1280*720（重要），后面的操作都是基于已经打开并正确配置模拟器**

### 截图.exe

1. 这个截图([源Github地址](https://github.com/MaaXYZ/MaaFramework/tree/main/tools/ImageCropper))工具用来截取活动界面的图片，点开**./ImageCropper/截图.exe**后，填0(数字)，回车。
2. 框错了可以点击**a**刷新截图，**长按s+回车**保存截图到./resource/image/，自动命名为活动截图.png

### 初始化

打开游戏，进到下面的界面
![avatar](https://github.com/MMDFTJ/MaaBhxy2/blob/main/images/%E6%B4%BB%E5%8A%A8%E7%95%8C%E9%9D%A2.png)
用截图工具截图当前的想要刷的活动
![avatar](https://github.com/MMDFTJ/MaaBhxy2/blob/main/images/%E6%B4%BB%E5%8A%A8%E7%95%8C%E9%9D%A2%E6%88%AA%E5%9B%BE.png)
就那个绿色框框就行，截取到活动的名字
回到首页
![avatar](https://github.com/MMDFTJ/MaaBhxy2/blob/main/images/%E9%A6%96%E9%A1%B5.png)

### 配装选择

常见的愿望杯自动套都行，需要将愿望杯放第一位，如果有金簪愿望杯套金簪放第一位

武器：愿望杯。必要！没有就用不了了 （悲）
衣服：可选幻兔*2，或者战车(拆崩科校活的障碍物)+随便一件（前提是徽章有能对敌人造成伤害的）
徽章：海底秘辛或者与你相遇，能对敌人造成伤害还可以拆崩科校活的障碍物
最低最低配：随便一件衣服+愿望杯+海底秘辛或者与你相遇
省流：带愿望杯(必要，普通愿望杯套愿望杯放第一位，金簪愿望杯金簪放第一位)的自动套，有清障碍能力(幻兔等)
![avatar](https://github.com/MMDFTJ/MaaBhxy2/blob/main/images/%E6%9C%80%E4%BD%8E%E9%85%8D%E7%BD%AE.png)
例子
![avatar](https://github.com/MMDFTJ/MaaBhxy2/blob/main/images/%E6%AD%A3%E5%B8%B8%E9%85%8D%E7%BD%AE.png)

**点开脚本前需要手动将套装换成自动套！**

至此，准备工作已经完成

### 启动！

进入首页
![avatar](https://github.com/MMDFTJ/MaaBhxy2/blob/main/images/%E9%A6%96%E9%A1%B5.png)
双击BHXY.exe
![avatar](https://github.com/MMDFTJ/MaaBhxy2/blob/main/images/%E9%A6%96%E9%A1%B5.png)

1. 先扫描设备，旁边有得选adb地址（一般默认就行）
2. 点连接，然后等个3，4秒（防止没有连接上）
3. 选择要运行的任务
4. 启动！

**有问题提issue**

## 开发相关

* [MaaFramework 快速开始](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/1.1-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.md)
* [MaaFramework 集成文档](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/2.1-%E9%9B%86%E6%88%90%E6%96%87%E6%A1%A3.md)

## 鸣谢

本项目由 **[MaaFramework](https://github.com/MaaXYZ/MaaFramework)** 强力驱动！
感谢开发者对本项目作出的贡献~

