
https://blog.csdn.net/magicdoubi/article/details/111223876

## 编写原因
有时需要翻译pdf，而且pdf复制后的文本格式需要整理一下才能更好的阅读
随便实现了一下，仅实现了功能，写的不好

## 开发环境
语言：python3.6
系统：win10

## 百度翻译api
注册的百度翻译开发者使用的通用翻译
实名认证后可以使用高级版，标准版其实也够用
注册地址
我写得这个必须要注册，因为需要appid和秘钥，填写两个变量的位置在程序中留出空了

![image](https://img-blog.csdnimg.cn/20201215161933508.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21hZ2ljZG91Ymk=,size_16,color_FFFFFF,t_70)

## 运行效果
剪贴板翻译打钩后，就可以直接获取剪贴板内容翻译
ctrl+shift+c是翻译的快捷键
![image](https://img-blog.csdnimg.cn/20201215161553152.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L21hZ2ljZG91Ymk=,size_16,color_FFFFFF,t_70)

## 程序
要使用的话注意appid和秘钥不要忘记填写
https://github.com/hkahfakh/pdfhelperV2
