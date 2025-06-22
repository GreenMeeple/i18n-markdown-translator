i18n-markdown-translator のデモ例
=============================

<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center"><img src="https://greenmeeple.github.io/img/logo.png"/></a></p>
<p align="center"> これはテストケースです。</p>  
<p align="center"><a href="https://greenmeeple.github.io" align="center">ここをクリックして私のウェブサイトを確認してください</a></p>
<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center">サポートしてください</a></p>

あなたのフレンドリーなソロプログラマーからの広告
------------------------

<table align="center"><tr><td valign="top" width="33%">

### プロジェクトとリポジトリ

* [MensaarLecker](https://github.com/GreenMeeple/MensaarLecker) ザールブリュッケンメンサ用の完全に自動化されたスクレーパーおよび静的なWebサイト、Python、Selenium、Googleスプレッドシート、およびGitHubActionsを搭載。
* [ウッズファールプラン](https://github.com/GreenMeeple/uds-fahrplan) ザールラント大学の学生向けに設計された軽量のTelegramボット
* [HAFAS-ビットマスク計算機](https://github.com/GreenMeeple/hafas-bitmask-calculator) HAFAS APIで使用されるビットマスクのデコードとエンコードを支援するシンプルなWebベースのツール。
* [ヘキソ・ジルビ](https://github.com/GreenMeeple/hexo-zhruby) Node.jsを使用して開発されたHexo Tagプラグイン
* [Azul\_Test](https://github.com/xindoo/eng-practices-cn) Michael Kiesling のボードゲーム Azul をベースにした C++ プログラム。
* [その他のプロジェクト](https://github.com/GreenMeeple?tab=repositories)

</TD>
<td valign="top" width="33%">

### 個人ブログ

* [python-telegram-botの開発経験とメモ](https://greenmeeple.github.io/python/tgbot/)
* [UdS Fahrplanボット](https://greenmeeple.github.io/projects/udsfahrplan-bot/)
* [🍽 🥨 MensaarLecker -- Selenium🥨 🍽を使用してMensa Ladiesのお気に入りのメニューを見つけるための最愛のツール](https://greenmeeple.github.io/projects/mensaar/)
* [MensaarLecker 開発ログ (3) -- Telegram ボットのデプロイと統合](https://greenmeeple.github.io/projects/mensaar-log3/)
* [UdS Fahrplan Bot Development Log (5) -- ボットのセッションとリクエストの解説](https://greenmeeple.github.io/projects/udsfahrplan-log5/)
* [他の投稿](https://greenmeeple.github.io/)

</TD>
</TR></テーブル>

---

[markdown-itデモ](https://markdown-it.github.io/)のテストケース
======================================================

h1見出し
=====

h2見出し
-----

### h3見出し

#### h4見出し

##### h5見出し

###### h6見出し

水平ルール
-----

---



---



---

強調
--

**これは太字のテキストです**

**これは太字のテキストです**

*これは斜体のテキストです*

*これは斜体のテキストです*

~~取り消し線~~

ブロッククォート
--------

> ブロッククォートはネストすることもできます...
>
> > ...隣り合って大なり記号を追加で使用することで...
> >
> > > ...または矢印の間にスペースを入れます。

リスト
---

順 不同

* リストを作成するには、行の先頭に `+`、 `-`、または `*`
* サブリストは、次の 2 つのスペースをインデントして作成されます。
  + マーカー文字の変更により、新しいリストが強制的に開始されます。
    - バラは赤です
    - スミレは青
    - 記号を変更しても
* やはり簡単です!

注文

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. 連番を使用できます...
5. ...または、すべての番号を `1.`

オフセット付きで番号付けを開始します。

57. フー
58. バール

コード
---

インライン `code`

インデントされたコード

```
// Some comments
line 1 of code
line 2 of code
line 3 of code

```

ブロックコード「フェンス」

[[CODEBLOCK0]]]

シンタックスハイライト

[[CODEBLOCK1]]]

テーブル
----

| オプション | の説明 |
| --- | --- |
| データ | データ ファイルへのパス: テンプレートに渡されるデータを提供します。 |
| エンジン | テンプレートの処理に使用するエンジン。デフォルトはハンドルバーです。 |
| 内線 | dest ファイルに使用する拡張子。 |

右揃えの列

| オプション | の説明 |
| --- | --- |
| データ | データ ファイルへのパス: テンプレートに渡されるデータを提供します。 |
| エンジン | テンプレートの処理に使用するエンジン。デフォルトはハンドルバーです。 |
| 内線 | dest ファイルに使用する拡張子。 |

リンクス
----

[リンクテキスト](http://dev.nodeca.com)

自動変換されたリンク <https://github.com/nodeca/pica> (linkifyを有効にして表示)

画像
--

![GreenMeeple](https://greenmeeple.github.io/img/avatar.png)
![Logo](https://greenmeeple.github.io/img/logo.png "The GreenMeeple Logo")

### [脚注](https://github.com/markdown-it/markdown-it-footnote)

脚注1リンク[[1]。](#fn1)

脚注 2 リンク[[2]。](#fn2)

インライン脚注[[3]](#fn3) の定義。

脚注参照が重複しています[[2:1]。](#fn2)

---

1. 脚注 **にはマークアップを含めることができます**

   と複数の段落。 [↩︎](#fnref1)
2. 脚注テキスト。[↩](#fnref2:1)[↩︎︎](#fnref2)
3. インライン脚注[↩](#fnref3)のテキスト ︎