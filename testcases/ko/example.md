i18n-markdown-translator 예제 데모
==============================

<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center"><img src="https://greenmeeple.github.io/img/logo.png"/></a></p>
<p align="center"> 이것은 테스트 케이스입니다. </p>  
<p align="center"><a href="https://greenmeeple.github.io" align="center">내 웹사이트를 확인하려면 여기를 클릭하십시오</a></p>
<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center">저를 지원해주세요</a></p>

친근한 솔로 프로그래머의 광고
----------------

<table align="center"><tr><td valign="상단" 너비="33%">

### 프로젝트 및 저장소

* [멘사르레커](https://github.com/GreenMeeple/MensaarLecker) Python, Selenium, Google Sheets 및 GitHub Actions를 기반으로 하는 Saarbrücken Mensa를 위한 완전 자동화된 스크레이퍼 및 정적 웹사이트입니다.
* [UDSFAHR플랜](https://github.com/GreenMeeple/uds-fahrplan) Saarland University 학생들을 위해 설계된 경량 텔레그램 봇
* [hafas-bitmask-calculator](https://github.com/GreenMeeple/hafas-bitmask-calculator) HAFAS API에서 사용하는 비트 마스크를 디코딩 및 인코딩하는 데 도움이 되는 간단한 웹 기반 도구입니다.
* [헥소 - 즈루비](https://github.com/GreenMeeple/hexo-zhruby) Node.js를 사용하여 개발된 Hexo 태그 플러그인
* [Azul\_Test](https://github.com/xindoo/eng-practices-cn) 마이클 키슬링(Michael Kiesling)의 보드게임 Azul을 기반으로 한 C++ 프로그램.
* [더 많은 프로젝트](https://github.com/GreenMeeple?tab=repositories)

</td>
<td valign="상단" 너비="33%">

### 개인 블로그

* [python-telegram-bot 개발 경험 및 참고 사항](https://greenmeeple.github.io/python/tgbot/)
* [UdS Fahrplan 봇](https://greenmeeple.github.io/projects/udsfahrplan-bot/)
* [🍽 🥨 MensaarLecker -- 셀레늄🥨 🍽을 사용하여 멘사 레이디가 가장 좋아하는 메뉴를 찾을 수 있는 사랑받는 도구](https://greenmeeple.github.io/projects/mensaar/)
* [MensaarLecker 개발 로그 (3) -- 텔레그램 봇 배포 및 통합](https://greenmeeple.github.io/projects/mensaar-log3/)
* [UdS Fahrplan 봇 개발 로그 (5) -- 봇 세션 및 요청에 대한 설명](https://greenmeeple.github.io/projects/udsfahrplan-log5/)
* [더 많은 게시물](https://greenmeeple.github.io/)

</td>
</tr></테이블>

---

[markdown-it 데모](https://markdown-it.github.io/)의 테스트 케이스
=========================================================

h1 제목
=====

h2 제목
-----

### h3 제목

#### h4 제목

##### h5 제목

###### h6 제목

수평 규칙
-----

---



---



---

강세
--

**이것은 굵은 텍스트입니다.**

**이것은 굵은 텍스트입니다.**

*이것은 기울임꼴 텍스트입니다.*

*이것은 기울임꼴 텍스트입니다.*

~~취소선~~

인용구
---

> 따옴표는 중첩될 수도 있습니다...
>
> > ... 서로 바로 옆에 있는 추가 보다 큼 기호를 사용하여...
> >
> > > ... 또는 화살표 사이에 공백이 있습니다.

목록
--

정렬

* , `-`또는 로 줄을 `+`시작하여 목록을 만듭니다.`*`
* 하위 목록은 2개의 공백을 들여써서 만듭니다.
  + 마커 문자 변경으로 새 목록이 강제로 시작됩니다.
    - 장미는 빨갛습니다
    - 제비꽃은 파란색입니다.
    - 심볼을 변경하더라도
* 여전히 하기 쉽습니다!

주문

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. 일련 번호를 사용할 수 있습니다...
5. ... 또는 모든 숫자를 다음과 같이 유지합니다. `1.`

오프셋으로 번호 매기기 시작:

57. 푸
58. 술집

코드
--

인라인 `code`

들여쓰기된 코드

```
// Some comments
line 1 of code
line 2 of code
line 3 of code

```

블록 코드 "울타리"

```
Sample text here...
```

구문 강조 표시

```js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

테이블
---

| 옵션 | 설명 |
| --- | --- |
| 데이터 | 템플릿에 전달될 데이터를 제공할 데이터 파일의 경로입니다. |
| 엔진 | 템플릿 처리에 사용되는 엔진입니다. 핸들바가 기본값입니다. |
| 내선 | DEST 파일에 사용할 확장자입니다. |

오른쪽으로 정렬된 열

| 옵션 | 설명 |
| --- | --- |
| 데이터 | 템플릿에 전달될 데이터를 제공할 데이터 파일의 경로입니다. |
| 엔진 | 템플릿 처리에 사용되는 엔진입니다. 핸들바가 기본값입니다. |
| 내선 | DEST 파일에 사용할 확장자입니다. |

링크
--

[링크 텍스트](http://dev.nodeca.com)

자동 변환된 링크 <https://github.com/nodeca/pica> (linkify가 볼 수 있도록 활성화)

이미지
---

![GreenMeeple](https://greenmeeple.github.io/img/avatar.png)
![Logo](https://greenmeeple.github.io/img/logo.png "The GreenMeeple Logo")

### [각주](https://github.com/markdown-it/markdown-it-footnote)

각주 1 링크[[1]](#fn1).

각주 2 링크[[2]](#fn2).

인라인 각주[[3]](#fn3) 정의.

중복된 각주 참조[[2:1]](#fn2).

---

1. 각주**에는 마크업이 있을 수 있습니다**.

   및 여러 단락. [↩︎](#fnref1)
2. 각주 텍스트. [↩](#fnref2)[↩︎ ︎](#fnref2:1)
3. 인라인 각주의 [↩텍스트 ︎](#fnref3)