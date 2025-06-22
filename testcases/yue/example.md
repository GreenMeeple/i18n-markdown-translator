i18n-markdown-translator嘅示例演示
=============================

<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center"><img src="https://greenmeeple.github.io/img/logo.png"/></a></p >
<p align="center">係一個測試用例。 </人>  
<p align="center"><a href="https://greenmeeple.github.io" align="center">點擊這裡查看我的網站</a></p>
<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center">支持我</a></p>

來自你友好嘅獨立程序員嘅廣告
--------------

<table align="center"><tr><td valign="top" width="33%">

### 項目同存儲庫

* [门萨尔莱克](https://github.com/GreenMeeple/MensaarLecker) Saarbrócken Mensa嘅全自動爬蟲同靜態網站，由Python、Selenium、Google Sheets同GitHub Actions提供支持。
* [UDSFAHRPLAN](https://github.com/GreenMeeple/uds-fahrplan) 專為萨尔大學學生設計嘅羽量級Telegram機械人
* [hafas位掩碼電腦](https://github.com/GreenMeeple/hafas-bitmask-calculator) 一個簡單嘅基於Web嘅工具，可幫助你解碼同編碼HAFAS API使用嘅位掩碼。
* [Hexo-zhruby](https://github.com/GreenMeeple/hexo-zhruby) 使用Node.js開發嘅Hexo Tag插件
* [Azul\_Test](https://github.com/xindoo/eng-practices-cn) 一個基於Michael Kiesling嘅棋盤遊戲Azul嘅C++程序。
* [更多項目](https://github.com/GreenMeeple?tab=repositories)

</td>
<td valign="top" width="33%">

### 個人博客

* [python-telegram-bot開發心得及注意事項](https://greenmeeple.github.io/python/tgbot/)
* [UdS Fahrplan機械人](https://greenmeeple.github.io/projects/udsfahrplan-bot/)
* [🍽 🥨 MensaarLecker--使用Selenium🥨 🍽查找Mensa女士最愛餐牌嘅心愛工具](https://greenmeeple.github.io/projects/mensaar/)
* [MensaarLecker開發日誌(三)--Telegram Bot部署與集成](https://greenmeeple.github.io/projects/mensaar-log3/)
* [UdS Fahrplan Bot開發日誌( 5 )——機械人會話同請求說明](https://greenmeeple.github.io/projects/udsfahrplan-log5/)
* [更多文章](https://greenmeeple.github.io/)

</td>
</tr></table >

---

[markdown-it演示](https://markdown-it.github.io/)中嘅測試用例
=====================================================

h1標題
====

h2航向
----

### h3航向

#### h4航向

##### h5航向

###### h6航向

水平標尺
----

---



---



---

強調
--

**此為粗體文本**

**此為粗體文本**

*這是斜體文本*

*這是斜體文本*

~~刪除線~~

蚊引用
---

> 區塊引用都可以嵌套......
>
> > ... 透過使用彼此相鄰嘅其他大於符號...
> >
> > > ... 或箭頭之間有空格。

清單
--

無序

* 透過以 `+`、 `-`或 `*`
* 子列表透過縮進2個空格嚟製作：
  + 把標記字符更改將強制新列表開始：
    - 玫瑰係紅色嘅
    - 紫羅蘭係藍色嘅
    - 即使您更改了符號
* 仍然好易做到！

命令

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. 你可以使用串行號...
5. ... 抑或把所有數字保留為 `1.`

以偏移量開始編號：

57. foo
58. 酒吧

法典
--

內嵌 `code`

縮進代碼

```
// Some comments
line 1 of code
line 2 of code
line 3 of code

```

阻止代碼"fences"

```
Sample text here...

```

語法高亮顯示

```js
var foo =函數( bar ) {
返回bar++;
};
console.log(foo(5));
```

表
-

| 選項 | 描述 |
| --- | --- |
| 數據 | path to data files嚟提供將傳遞到糢闆中嘅數據。 |
| 發動機 | engine用于處理糢闆。 Handlebars係默認設置。 |
| 內線 | 用于DEST文件嘅擴展名。 |

右對正嘅列

| 選項 | 描述 |
| --- | --- |
| 數據 | path to data files嚟提供將傳遞到糢闆中嘅數據。 |
| 發動機 | engine用于處理糢闆。 Handlebars係默認設置。 |
| 內線 | 用于DEST文件嘅擴展名。 |

連結
--

[連結文字](http://dev.nodeca.com)

自動轉換嘅連結 <https://github.com/nodeca/pica> (啟用linkify以查看)

圖像
--

![GreenMeeple](https://greenmeeple.github.io/img/avatar.png)
![Logo](https://greenmeeple.github.io/img/logo.png "The GreenMeeple Logo")

### [腳註](https://github.com/markdown-it/markdown-it-footnote)

腳註1連結[[ 1 ]。](#fn1)

腳註2連結[[ 2 ]。](#fn2)

內聯腳註[[3]](#fn3) 定義。

重複的腳註引用[[2：1]。](#fn2)

---

1. 腳註 **可以有標記**

   同多個段落。 [↩︎](#fnref1)
2. 腳註文本。[↩](#fnref2)[↩︎ ︎](#fnref2:1)
3. 內聯腳註 [↩≤嘅](#fnref3) 文字