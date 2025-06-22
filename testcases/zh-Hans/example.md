i18n-markdown-translator 的示例演示
==============================

<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center"><img src="https://greenmeeple.github.io/img/logo.png"/></a></p>
<p align="center"> 这是一个测试用例。</人>  
<p align="center"><a href="https://greenmeeple.github.io" align="center">点击这里查看我的网站</a></p>
<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center">支持我</a></p>

来自您友好的独立程序员的广告
--------------

<table align="center"><tr><td valign="top" width="33%">

### 项目和存储库

* [门萨尔莱克](https://github.com/GreenMeeple/MensaarLecker) Saarbrücken Mensa 的全自动爬虫和静态网站，由 Python、Selenium、Google Sheets 和 GitHub Actions 提供支持。
* [UDSFAHRPLAN](https://github.com/GreenMeeple/uds-fahrplan) 专为萨尔大学学生设计的轻量级 Telegram 机器人
* [hafas 位掩码计算器](https://github.com/GreenMeeple/hafas-bitmask-calculator) 一个简单的基于 Web 的工具，可帮助您解码和编码 HAFAS API 使用的位掩码。
* [Hexo-zhruby](https://github.com/GreenMeeple/hexo-zhruby) 使用 Node.js 开发的 Hexo Tag 插件
* [Azul\_Test](https://github.com/xindoo/eng-practices-cn) 一个基于 Michael Kiesling 的棋盘游戏 Azul 的 C++ 程序。
* [更多项目](https://github.com/GreenMeeple?tab=repositories)

</td>
<td valign="top" width="33%">

### 个人博客

* [python-telegram-bot 开发心得及注意事项](https://greenmeeple.github.io/python/tgbot/)
* [UdS Fahrplan 机器人](https://greenmeeple.github.io/projects/udsfahrplan-bot/)
* [🍽 🥨 MensaarLecker -- 使用 Selenium🥨 🍽 查找 Mensa 女士最爱菜单的心爱工具](https://greenmeeple.github.io/projects/mensaar/)
* [MensaarLecker 开发日志(三)-- Telegram Bot 部署与集成](https://greenmeeple.github.io/projects/mensaar-log3/)
* [UdS Fahrplan Bot 开发日志 (5) -- 机器人会话和请求说明](https://greenmeeple.github.io/projects/udsfahrplan-log5/)
* [更多文章](https://greenmeeple.github.io/)

</td>
</tr></table >

---

[markdown-it 演示](https://markdown-it.github.io/)中的测试用例
======================================================

h1 标题
=====

h2 航向
-----

### h3 航向

#### h4 航向

##### h5 航向

###### h6 航向

水平标尺
----

---



---



---

强调
--

**此为粗体文本**

**此为粗体文本**

*这是斜体文本*

*这是斜体文本*

~~删除线~~

块引用
---

> 块引用也可以嵌套......
>
> > ...通过使用彼此相邻的其他大于符号...
> >
> > > ...或箭头之间有空格。

列表
--

无序

* 通过以 `+`、 `-`或 `*`
* 子列表通过缩进 2 个空格来制作：
  + 标记字符更改会强制新列表开始：
    - 玫瑰是红色的
    - 紫罗兰是蓝色的
    - 即使您更改了符号
* 这仍然很容易做到！

命令

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. 你可以使用序列号...
5. ...或者将所有数字保留为 `1.`

以偏移量开始编号：

57. foo
58. 酒吧

法典
--

内嵌 `code`

缩进代码

```
// Some comments
line 1 of code
line 2 of code
line 3 of code

```

阻止代码 "fences"

```
Sample text here...

```

语法高亮显示

```js
var foo = 函数 (bar) {
返回 bar++;
};
console.log(foo(5));
```

表
-

| 选项 | 描述 |
| --- | --- |
| 数据 | path to data files 来提供将传递到模板中的数据。 |
| 发动机 | engine 用于处理模板。Handlebars 是默认设置。 |
| 内线 | 用于 DEST 文件的扩展名。 |

右对齐的列

| 选项 | 描述 |
| --- | --- |
| 数据 | path to data files 来提供将传递到模板中的数据。 |
| 发动机 | engine 用于处理模板。Handlebars 是默认设置。 |
| 内线 | 用于 DEST 文件的扩展名。 |

链接
--

[链接文本](http://dev.nodeca.com)

自动转换的链接 <https://github.com/nodeca/pica> (启用 linkify 以查看)

图像
--

![GreenMeeple](https://greenmeeple.github.io/img/avatar.png)
![Logo](https://greenmeeple.github.io/img/logo.png "The GreenMeeple Logo")

### [脚注](https://github.com/markdown-it/markdown-it-footnote)

脚注 1 链接[[1]。](#fn1)

脚注 2 链接[[2]。](#fn2)

内联脚注[[3]](#fn3) 定义。

重复的脚注引用[[2：1]。](#fn2)

---

1. 脚注 **可以有标记**

   和多个段落。 [↩︎](#fnref1)
2. 脚注文本。[↩](#fnref2)[↩︎ ︎](#fnref2:1)
3. 内联脚注 [↩︎](#fnref3) 的文本