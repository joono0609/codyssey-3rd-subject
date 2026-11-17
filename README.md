# Mini NPU Simulator 개발

## 개요
인공지능에서 많이 사용하는 원리인 MAC(Multiply-Accumulate)을 이용하여 NPU 가 왜 필요한지 파이션 기본라이브러리만 활용하여 직접 구현한다

---

## 파일 구조

```
codyssey-3rd-subject/
├── src/
│   ├── mac.py         # Mac 계산 
│   └── judge.json     # 판정부분
├── main.py       # 메인 실행 파일
├── data.json     # 5×5, 13×13, 25×25 필터 및 패턴 데이터
└── README.md
```

---

## 실행 방법

```bash
cd codyssey-3rd-subject
python main.py
```

- **모드 1** 선택 시: 콘솔에서 필터 A, B와 패턴을 직접 입력
- **모드 2** 선택 시: 같은 디렉토리의 `data.json` 자동 로드

---
