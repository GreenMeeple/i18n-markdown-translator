i18n-md-번역기
===========

Microsoft Translator API를 사용하여 Markdown 파일을 변환하는 명령줄 도구입니다. 표, 코드 블록, 목록 및 각주를 포함한 Markdown 구조를 보존합니다.

🛠 설치
----

```bash
pip install i18n-md-translator
```

🚀 사용법
-----

```bash
i18n-md-translate path/to/file.md -s en -t zh-Hant
```

* `-s` 또는 `--source`: 소스 언어(기본값: `en`)
* `-t` 또는 `--target`: 대상 언어(기본값: `yue`)

🧪 본보기
-----

```bash
i18n-md-translate ./README.md -s en -t yue
```

만듭니다: `./yue/README.md`

🌐 지원되는 언어
---------

참조: [언어 지원 - 번역기 - Azure AI 서비스](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)

🔐 API 키
-------

Translator API 자격 증명을 파일에 넣습니다.`.env`

```ini
TRANSLATOR_KEY=your_key_here
TRANSLATOR_REGION=your_region_here
```

📄 면허
----

MIT (영어)

참조
--

Markdown 파서가 올바르게 완료되었습니다. 100% CommonMark 지원, 확장, 구문 플러그인 및 고속.

* [마크다운-잇](https://github.com/markdown-it/markdown-it)
* [마크다운-잇-파이](https://github.com/executablebooks/markdown-it-py)

HTML을 Markdown으로 변환, cloudinary 이미지 업로드 기능이 내장된 가장 간단한 마크다운 편집기입니다.

* [파이썬 markdownify](https://github.com/matthewwithanm/python-markdownify)
* [마크다운파이](https://github.com/tibastral/markdownify)

---