i18n-md-トランスレータ
===============

Microsoft Translator API を使用して Markdown ファイルを翻訳するコマンドライン ツール。テーブル、コード ブロック、リスト、脚注などの Markdown 構造が保持されます。

🛠 取り付け
------

[[CODEBLOCK0]]]

🚀 使い
----

[[CODEBLOCK1]]]

* `-s` または `--source`: ソース言語 (デフォルト: `en`)
* `-t` または `--target`: ターゲット言語 (デフォルト: `yue`)

🧪 例
---

```bash
i18n-md-translate ./README.md -s en -t yue
```

作成： `./yue/README.md`

🌐 サポートされている言語
-------------

参照項目: [言語サポート - 翻訳ツール - Azure AI サービス](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)

🔐 APIキー
-------

Translator API の資格情報を `.env` ファイルに入れます。

[[CODEBLOCK3]]]

📄 ライセンス
-------

マサチューセッツ工科大学(MIT)

参照
--

Markdownパーサー、正しく行われました。100%CommonMarkサポート、拡張機能、シンタックスプラグイン、高速性。

* [マークダウン-イット](https://github.com/markdown-it/markdown-it)
* [マークダウンイットピー](https://github.com/executablebooks/markdown-it-py)

HTMLをMarkdownに変換する、クラウド画像のアップロードが組み込まれている最も単純なマークダウンエディタ。

* [python-マークダウン化](https://github.com/matthewwithanm/python-markdownify)
* [マークダウン化](https://github.com/tibastral/markdownify)

---