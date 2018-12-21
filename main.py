"""
<AMUSEMENT PARK>
"""


class Express:  # A - express 를 기다리는 줄을 관리하는 클래스 생성

    # 현재 오렌지의 위치 초기값
    oi = 0
    oj = 0

    # 현재 멜론의 위치 초기값
    mi = 0
    mj = 0

    # 규칙4에서 활용할 변수 초기화
    xx = 0
    yy = 0

    def __init__(self, n, m, s):
        self.max_p = 0  # 1부터 max_P까지 사람들이 이동하는 순서를 나타냄
        self.p = []  # 격자 내 사람들이 기다리는 줄을 나타낸 리스트
        self.n = n  # 격자의 행 크기
        self.m = m  # 격자의 열 크기
        self.s = s  # 멜론의 위치 설정
        self.t = 1  # 오렌지의 위치 설정(초기값 1로 시작)
        self.C = []  # 오렌지가 멜론을 볼 수 있는 위치를 입력 받는 리스트

    def add_grid(self):  # 격자 내 사람들이 기다리는 줄을 입력받는 함수
        print(N, "X", M, "크기 격자의 이동순서를 입력하세요.")
        for i in range(N):
            for j in range(M):
                self.p[i][j] = int(input())  # 첫 칸에서 부터 순서대로 숫자를 입력 받음

    def find_max_grid(self):  # 사람들이 이동하는 순서를 구하는 함수(1부터 max_P까지 이동)
        for i in range(N):
            for j in range(M):
                if self.p[i][j] > self.p[i - 1][j - 1]:  # 이전 값보다 지금의 값이 더 크다면
                    self.max_p = self.p[i][j]  # 큰 값을 max_p에 집어 넣도록 함

    """
    아래의 rule 함수는 오렌지가 멜론을 볼 수 있는 규칙을 확인하여 리스트에 저장하는 함수이다.
    규칙은 총 4가지이다.
    
    주의사항 : 격자는 (1, 1)부터 시작하지만 리스트 인덱스는 (0, 0)부터 시작한다.
    """

    def rule(self):  # 오렌지가 멜론을 볼 수 있는 규칙을 확인하여 리스트에 저장하는 함수
        while self.s <= self.max_p:  # 멜론의 위치(s)가 마지막 이동경로(max_p)에 도달할 때까지
            for a in range(self.n):
                for b in range(self.m):
                    if self.p[a][b] == self.s:  # p 리스트에 입력된 숫자와 멜론의 위치 숫자와 같으면
                        mi = a + 1  # 멜론의 행(mi)과 열(mj)을 설정함
                        mj = b + 1  # 격자는 (1, 1)부터 시작하므로 행과 열에 각 1씩 더함
                    elif self.p[a][b] == self.t:  # p 리스트에 입력된 숫자와 오렌지의 위치 숫자와 같으면
                        oi = a + 1  # 오렌지의 행(oi)과 열(oj)을 설정함
                        oj = b + 1  # 격자는 (1, 1)부터 시작하므로 행과 열에 각 1씩 더함

            temp_array = []  # 현재 오렌지와 멜론의 위치에서 지나치는 모든 위치값의 임시 리스트 생성 및 초기화

            # 규칙1) 행 또는 열의 차이가 1일 경우
            if abs(mi - oi) == 1 or 1 == abs(mj - oj):  # 리스트 인덱스에 맞게 각 1씩 차감하여 C 리스트에 저장
                self.C.append(self.p[oi - 1][oj - 1])

            # 규칙2) 오렌지와 멜론의 현재 위치에서 행만 같을 경우
            elif oi == mi:
                if oj < mj:  # 오렌지의 열보다 멜론의 열이 더 클 경우
                    for a in range(1, mj - oj):  # 오렌지와 멜론 사이의 위치변수 값을 temp_array 리스트에 저장
                        temp_array.append(self.p[oi - 1][oj + a - 1])
                else:  # 오렌지의 열보다 멜론의 열이 더 작을 경우
                    for a in range(1, oj - mj):  # 오렌지와 멜론 사이의 위치변수 값을 temp_array 리스트에 저장
                        temp_array.append(self.p[oi - 1][oj - a - 1])
                temp_array.sort(reverse=True)  # temp_array 리스트 내림차순 정렬
                if temp_array[0] == 0:  # temp_array 리스트의 첫 번째 값이 0일 경우 C 리스트에 저장
                    self.C.append(self.p[oi - 1][oj - 1])

            # 규칙3) 오렌지와 멜론의 현재 위치에서 열만 같을 경우
            elif oj == mj:
                if oi < mi:  # 오렌지의 행보다 멜론의 행이 더 클 경우
                    for a in range(1, mi - oi):  # 오렌지와 멜론 사이의 위치변수 값을 temp_array 리스트에 저장
                        temp_array.append(self.p[oi + a - 1][oj - 1])
                else:  # 오렌지의 행보다 멜론의 행이 더 작을 경우
                    for a in range(1, oi - mi):  # 오렌지와 멜론 사이의 위치변수 값을 temp_array 리스트에 저장
                        temp_array.append(self.p[oi - a - 1][oj - 1])
                temp_array.sort(reverse=True)  # temp_array 리스트 내림차순 정렬
                if temp_array[0] == 0:  # temp_array 리스트의 첫 번째 값이 0일 경우 C 리스트에 저장
                    self.C.append(self.p[oi - 1][oj - 1])

            # 규칙4) 오렌지와 멜론의 현재 위치가 행과 열 모두 다를 경우
            else:
                x: int = abs(mi - oi)  # 오렌지 행과 멜론 행의 차이(절댓값)
                y: int = abs(mj - oj)  # 오렌지 열과 멜론 열의 차이(절댓값)
                if max(x, y) % min(x, y) > 0:  # x, y 중 큰 수에서 작은 수를 나눈 나머지가 0이 아닐 경우 C 리스트에 저장
                    self.C.append(self.p[oi - 1][oj - 1])
                else:  # x, y 중 큰 수에서 작은 수를 나눈 나머지가 0일 경우
                    if x == y:  # x와 y값이 같을 경우
                        xx = (mi - oi) // x  # 오렌지 행과 멜론 행 사이의 증가 비율(최솟값)
                        yy = (mj - oj) // x  # 오렌지 열과 멜론 열 사이의 증가 비율(최솟값)
                        for a in range(1, x):  # 오렌지와 멜론 사이의 위치변수 값을 temp_array 리스트에 저장
                            temp_array.append(self.p[oi + (xx * a) - 1][oj + (yy * a) - 1])
                        temp_array.sort(reverse=True)  # temp_array 리스트 내림차순 정렬
                        if temp_array[0] == 0:  # temp_array 리스트의 첫 번째 값이 0일 경우 C 리스트에 저장
                            self.C.append(self.p[oi - 1][oj - 1])
                    elif x < y:  # x보다 y값이 클 경우
                        xx = (mi - oi) // x  # 오렌지 행과 멜론 행 사이의 증가 비율(최솟값)
                        yy = (mj - oj) // y  # 오렌지 열과 멜론 열 사이의 증가 비율(최솟값)
                        for a in range(1, y // x):  # 오렌지와 멜론 사이의 위치변수 값을 temp_array 리스트에 저장
                            temp_array.append(self.p[oi + (xx * a) - 1][oj + (yy * a) - 1])
                        temp_array.sort(reverse=True)  # temp_array 리스트 내림차순 정렬
                        if temp_array[0] == 0:  # temp_array 리스트의 첫 번째 값이 0일 경우 C 리스트에 저장
                            self.C.append(self.p[oi - 1][oj - 1])
                    else:  # x보다 y값이 작을 경우
                        xx = (mi - oi) // y  # 오렌지 행과 멜론 행 사이의 증가 비율(최솟값)
                        yy = (mj - oj) // x  # 오렌지 열과 멜론 열 사이의 증가 비율(최솟값)
                        for a in range(1, x // y):  # 오렌지와 멜론 사이의 위치변수 값을 temp_array 리스트에 저장
                            temp_array.append(self.p[oi + (xx * a) - 1][oj + (yy * a) - 1])
                        temp_array.sort(reverse=True)  # temp_array 리스트 내림차순 정렬
                        if temp_array[0] == 0:  # temp_array 리스트의 첫 번째 값이 0일 경우 C 리스트에 저장
                            self.C.append(self.p[oi - 1][oj - 1])
            self.s += 1  # 현재 멜론의 위치에 1을 증가시켜 다음 값을 계산하게 함
            self.t += 1  # 현재 오렌지의 위치에 1을 증가시켜 다음 값을 계산하게 함


if __name__ == "__main__":  # 메인문

    print("행(N)과 열(M)과 멜론의 위치(S)를 차례로 입력하세요.")
    N = int(input())  # 행 크기 설정
    M = int(input())  # 열 크기 설정
    S = int(input())  # 멜론의 위치 설정

    om = Express(N, M, S)  # Express 클래스를 사용하는 om 객체 생성

    om.p = [[0 for i in range(M)] for j in range(N)]  # om 객체의 p 리스트를 NxM 크기의 리스트로 생성
    om.add_grid()  # 격자 이동순서 설정 함수 실행
    om.find_max_grid()  # 줄의 크기(max_p)를 구하는 함수 실행

    print("총 이동 수는", om.max_p, "입니다.")  # om 객체의 줄의 크기를 나타냄
    print(om.p)  # 격자 출력
    om.rule()  # 오렌지가 멜론을 볼 수 있는 규칙 함수 실행

    # 출력
    om.C.sort()  # C 리스트 오름차순 정렬

    print("오렌지가 멜론을 본 횟수는", len(om.C), "번 입니다.")  # 오렌지가 멜론을 본 횟수
    print(om.C)  # 멜론을 본 오렌지의 위치를 나타낸 리스트 출력
