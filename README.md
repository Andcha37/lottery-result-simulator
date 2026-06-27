# 로또 번호 확인 웹 프로그램

이 프로젝트는 Python으로 `lottery.html` 파일을 생성하고, 생성된 HTML 화면에서 사용자가 직접 로또 번호 6개를 입력해 당첨 결과를 확인할 수 있게 만든 예제 프로그램입니다.

## 프로젝트 개요

이 프로그램의 목적은 Python, HTML, CSS, JavaScript가 함께 어떻게 사용되는지 이해하기 위한 간단한 로또 결과 확인 예제입니다.

Python은 최종 HTML 파일을 만들어 주는 역할을 담당하고, 실제 화면에서 사용자가 번호를 입력하거나 버튼을 누르는 동작은 HTML 안에 포함된 JavaScript가 처리합니다.

사용자는 `lottery.html`을 브라우저에서 열고 1부터 45까지의 숫자 6개를 입력합니다. 이후 `결과 확인` 버튼을 누르면 현재 페이지에서 새로 뽑힌 당첨 번호와 비교해 당첨 등수와 당첨금을 보여줍니다.

## 주요 기능

- 사용자가 로또 번호 6개를 직접 입력할 수 있습니다.
- 입력 번호는 1부터 45 사이의 정수만 허용합니다.
- 같은 번호를 중복해서 입력하면 오류 메시지를 보여줍니다.
- `자동 입력` 버튼으로 번호 6개를 무작위로 채울 수 있습니다.
- `결과 확인` 버튼으로 사용자가 입력한 번호와 당첨 번호를 비교합니다.
- 당첨 번호는 결과 확인 시 화면에 공개됩니다.
- 일반 당첨 번호와 일치한 입력 공은 빨간색으로 강조됩니다.
- 보너스 번호와 일치한 입력 공은 파란색으로 강조됩니다.
- 당첨 등수에 따라 당첨금이 표시됩니다.
- 1등부터 4등까지는 간단한 축하 효과가 나타납니다.
- 페이지를 새로 열거나 브라우저 창을 닫았다 다시 열면 당첨 번호가 새로 생성됩니다.
- `새 당첨번호` 버튼을 누르면 현재 화면에서 당첨 번호를 다시 뽑을 수 있습니다.

## 파일 구성

```text
lottery_example/
├── lottery.py
├── lottery_driver.py
├── lottery.html
└── README.md
```

### `lottery.py`

로또 번호 생성과 당첨금 판정에 필요한 기본 Python 함수가 들어 있습니다.

주요 함수는 다음과 같습니다.

- `generate_numbers(n)`: 1부터 45까지의 숫자 중 중복 없이 `n`개를 생성합니다.
- `draw_winning_numbers()`: 일반 당첨 번호 6개와 보너스 번호 1개를 생성합니다.
- `count_matching_numbers(numbers, winning_numbers)`: 두 번호 목록에서 일치하는 번호 개수를 셉니다.
- `check(numbers, winning_numbers)`: 입력 번호와 당첨 번호를 비교해 당첨금을 문자열로 반환합니다.

현재 `lottery.html` 안의 사용자 입력 기능은 JavaScript로 동작하지만, `lottery.py`는 Python으로 로또 로직을 연습하거나 별도로 테스트할 때 사용할 수 있습니다.

### `lottery_driver.py`

최종 결과물인 `lottery.html`을 생성하는 Python 파일입니다.

이 파일 안에는 HTML, CSS, JavaScript 코드가 하나의 문자열로 들어 있으며, 실행하면 같은 폴더에 `lottery.html` 파일을 새로 작성합니다.

실행 명령:

```powershell
python lottery_driver.py
```

실행 후 생성되는 파일:

```text
lottery.html
```

### `lottery.html`

사용자가 실제로 브라우저에서 여는 화면입니다.

이 파일에는 다음 요소가 포함되어 있습니다.

- 번호 입력 공 6개
- 결과 확인 버튼
- 자동 입력 버튼
- 새 당첨번호 버튼
- 당첨 번호 표시 영역
- 당첨 결과 표시 영역
- 입력 검증 JavaScript
- 당첨 번호 생성 JavaScript
- 결과 강조 및 축하 효과 CSS/JavaScript

## 실행 방법

1. 명령 프롬프트 또는 PowerShell을 엽니다.

2. 프로젝트 폴더로 이동합니다.

```powershell
cd C:\python\lottery_example
```

3. HTML 파일을 다시 생성합니다.

```powershell
python lottery_driver.py
```

4. 생성된 `lottery.html` 파일을 브라우저로 엽니다.

```powershell
start lottery.html
```

브라우저가 열리면 화면에서 직접 번호 6개를 입력하고 `결과 확인` 버튼을 누르면 됩니다.

## 사용 방법

1. `lottery.html`을 브라우저에서 엽니다.
2. 동그란 입력 공 6개에 1부터 45까지의 숫자를 입력합니다.
3. 번호는 서로 달라야 합니다.
4. 직접 입력하기 귀찮으면 `자동 입력` 버튼을 누릅니다.
5. `결과 확인` 버튼을 누릅니다.
6. 화면에 당첨 번호, 일치 개수, 등수, 당첨금이 표시됩니다.
7. 새로운 당첨 번호로 다시 확인하고 싶으면 `새 당첨번호` 버튼을 누릅니다.
8. 브라우저 창을 닫았다 다시 열면 당첨 번호가 초기화되어 새 번호로 시작됩니다.

## 당첨 판정 기준

이 프로젝트에서 사용하는 당첨금 기준은 다음과 같습니다.

| 조건 | 등수 | 당첨금 |
| --- | --- | ---: |
| 일반 번호 6개 일치 | 1등 | 1,000,000,000원 |
| 일반 번호 5개 + 보너스 번호 일치 | 2등 | 50,000,000원 |
| 일반 번호 5개 일치 | 3등 | 1,000,000원 |
| 일반 번호 4개 일치 | 4등 | 50,000원 |
| 일반 번호 3개 일치 | 5등 | 5,000원 |
| 그 외 | 꽝 | 0원 |

## 화면 동작 방식

당첨 번호는 브라우저에서 페이지가 로드될 때 JavaScript로 생성됩니다.

즉, `lottery.html`을 새로 열 때마다 이전 당첨 번호를 저장하지 않고 새 당첨 번호를 뽑습니다. 별도의 데이터베이스나 저장 파일을 사용하지 않기 때문에, 창을 닫았다 다시 열면 당첨 번호가 초기화되는 구조입니다.

입력한 번호와 당첨 번호를 비교한 뒤에는 다음과 같이 화면 효과가 적용됩니다.

- 일반 당첨 번호와 일치하면 입력 공이 빨간색으로 표시됩니다.
- 보너스 번호와 일치하면 입력 공이 파란색으로 표시됩니다.
- 일치하지 않는 번호는 회색으로 표시됩니다.
- 높은 등수에 당첨되면 색종이 효과가 나타납니다.
- 잘못된 입력이 있으면 입력 공이 흔들리고 오류 메시지가 표시됩니다.

## 코드 구조 요약

### Python 흐름

```text
lottery_driver.py 실행
→ HTML 문자열 준비
→ lottery.html 파일 생성
→ 브라우저에서 lottery.html 실행
```

### 브라우저 흐름

```text
페이지 열림
→ JavaScript가 당첨 번호 생성
→ 사용자가 번호 6개 입력
→ 결과 확인 버튼 클릭
→ 입력값 검증
→ 당첨 번호와 비교
→ 등수와 당첨금 표시
```

## 수정할 때 참고할 부분

화면 디자인을 바꾸고 싶다면 `lottery_driver.py` 안의 `<style>` 영역을 수정하면 됩니다.

버튼 동작이나 당첨 판정 화면을 바꾸고 싶다면 `lottery_driver.py` 안의 `<script>` 영역을 수정하면 됩니다.

Python에서 번호 생성 로직을 연습하고 싶다면 `lottery.py`의 함수를 수정하거나 직접 실행해 볼 수 있습니다.

## 주의 사항

- `lottery.html`을 직접 수정한 뒤 `lottery_driver.py`를 다시 실행하면 직접 수정한 HTML 내용은 덮어써집니다.
- 화면을 영구적으로 수정하려면 `lottery_driver.py` 안의 HTML 문자열을 수정해야 합니다.
- 이 프로젝트는 실제 복권 시스템과 연결되어 있지 않은 학습용 예제입니다.
- 당첨 번호와 당첨금은 프로그램 내부 규칙에 따라 계산되는 가상 결과입니다.

---

# Lotto Number Checker Web Program

This project is an example program that uses Python to generate a `lottery.html` file. In the generated HTML page, users can directly enter six lotto numbers and check the winning result.

## Project Overview

The purpose of this program is to provide a simple lotto result checker example for understanding how Python, HTML, CSS, and JavaScript can work together.

Python is responsible for generating the final HTML file. The actual screen interactions, such as entering numbers or clicking buttons, are handled by JavaScript included inside the HTML.

The user opens `lottery.html` in a browser and enters six numbers from 1 to 45. When the user clicks the `Check Result` button, the program compares the entered numbers with the newly drawn winning numbers on the current page and displays the prize rank and prize amount.

## Main Features

- Users can directly enter six lotto numbers.
- Only integer values from 1 to 45 are allowed.
- If duplicate numbers are entered, an error message is displayed.
- The `Auto Pick` button can randomly fill in six numbers.
- The `Check Result` button compares the user's numbers with the winning numbers.
- The winning numbers are revealed on the screen after checking the result.
- Input balls that match the main winning numbers are highlighted in red.
- Input balls that match the bonus number are highlighted in blue.
- The prize amount is displayed according to the winning rank.
- A simple celebration effect appears for 1st through 4th prize results.
- When the page is reopened or the browser window is closed and opened again, the winning numbers are newly generated.
- The `New Winning Numbers` button can redraw the winning numbers on the current screen.

## File Structure

```text
lottery_example/
├── lottery.py
├── lottery_driver.py
├── lottery.html
└── README.md
```

### `lottery.py`

This file contains the basic Python functions needed for generating lotto numbers and judging prize results.

The main functions are as follows.

- `generate_numbers(n)`: Generates `n` unique numbers from 1 to 45.
- `draw_winning_numbers()`: Generates six main winning numbers and one bonus number.
- `count_matching_numbers(numbers, winning_numbers)`: Counts how many numbers match between two number lists.
- `check(numbers, winning_numbers)`: Compares the input numbers with the winning numbers and returns the prize amount as a string.

The user input feature inside `lottery.html` currently runs with JavaScript, but `lottery.py` can still be used to practice the lotto logic in Python or test it separately.

### `lottery_driver.py`

This Python file generates the final output file, `lottery.html`.

The file contains HTML, CSS, and JavaScript code as one large string. When executed, it writes a new `lottery.html` file in the same folder.

Run command:

```powershell
python lottery_driver.py
```

Generated file:

```text
lottery.html
```

### `lottery.html`

This is the page that users actually open in a browser.

This file includes the following elements.

- Six number input balls
- Check result button
- Auto pick button
- New winning numbers button
- Winning number display area
- Prize result display area
- Input validation JavaScript
- Winning number generation JavaScript
- CSS and JavaScript for result highlighting and celebration effects

## How to Run

1. Open Command Prompt or PowerShell.

2. Move to the project folder.

```powershell
cd C:\python\lottery_example
```

3. Regenerate the HTML file.

```powershell
python lottery_driver.py
```

4. Open the generated `lottery.html` file in a browser.

```powershell
start lottery.html
```

When the browser opens, enter six numbers directly on the screen and click the `Check Result` button.

## How to Use

1. Open `lottery.html` in a browser.
2. Enter numbers from 1 to 45 into the six round input balls.
3. Each number must be different.
4. If you do not want to enter numbers manually, click the `Auto Pick` button.
5. Click the `Check Result` button.
6. The winning numbers, match count, rank, and prize amount will be displayed.
7. To check again with new winning numbers, click the `New Winning Numbers` button.
8. If you close and reopen the browser window, the winning numbers are reset and a new draw starts.

## Prize Rules

This project uses the following prize amount rules.

| Condition | Rank | Prize |
| --- | --- | ---: |
| 6 main numbers match | 1st prize | 1,000,000,000 KRW |
| 5 main numbers + bonus number match | 2nd prize | 50,000,000 KRW |
| 5 main numbers match | 3rd prize | 1,000,000 KRW |
| 4 main numbers match | 4th prize | 50,000 KRW |
| 3 main numbers match | 5th prize | 5,000 KRW |
| All other cases | No prize | 0 KRW |

## Screen Behavior

The winning numbers are generated by JavaScript when the browser page loads.

This means that every time `lottery.html` is opened, the previous winning numbers are not saved and a new set of winning numbers is drawn. Because the project does not use a separate database or saved file, closing and reopening the window resets the winning numbers.

After the entered numbers are compared with the winning numbers, the following visual effects are applied.

- If a number matches a main winning number, the input ball is displayed in red.
- If a number matches the bonus number, the input ball is displayed in blue.
- Numbers that do not match are displayed in gray.
- For higher prize ranks, a confetti effect appears.
- If the input is invalid, the input balls shake and an error message is displayed.

## Code Flow Summary

### Python Flow

```text
Run lottery_driver.py
→ Prepare the HTML string
→ Generate lottery.html
→ Open lottery.html in a browser
```

### Browser Flow

```text
Page loads
→ JavaScript generates winning numbers
→ User enters six numbers
→ User clicks the check result button
→ Input values are validated
→ User numbers are compared with the winning numbers
→ Rank and prize amount are displayed
```

## Notes for Editing

If you want to change the screen design, edit the `<style>` section inside `lottery_driver.py`.

If you want to change button behavior or the result display logic, edit the `<script>` section inside `lottery_driver.py`.

If you want to practice number generation logic in Python, you can modify or run the functions in `lottery.py`.

## Important Notes

- If you edit `lottery.html` directly and then run `lottery_driver.py` again, your direct HTML changes will be overwritten.
- To make permanent screen changes, edit the HTML string inside `lottery_driver.py`.
- This project is a learning example and is not connected to any real lottery system.
- The winning numbers and prize amounts are virtual results calculated according to the program's internal rules.
