# File: tdemo_chaos.py
# Author: Gregor Lingl
# Date: 2009-06-24

from turtle import *  # turtle 모듈을 불러옵니다. turtle 모듈은 간단한 그래픽을 그릴 수 있는 도구입니다.

N = 80  # N 변수에 80을 저장합니다.

# 아래 세 함수 f, g, h는 모두 동일한 계산을 수행하지만, 계산 순서에 따라 결과가 달라질 수 있음을 보여줍니다.
def f(x):
    return 3.9*x*(1-x)

def g(x):
    return 3.9*(x-x**2)

def h(x):
    return 3.9*x-3.9*x*x

def jumpto(x, y):  # 지정된 위치로 이동하는 함수입니다.
    penup()  # 펜을 들어서 그림이 그려지지 않도록 합니다.
    goto(x,y)  # 지정된 위치로 이동합니다.

def line(x1, y1, x2, y2):  # 두 점을 연결하는 선을 그리는 함수입니다.
    jumpto(x1, y1)  # 첫 번째 점으로 이동합니다.
    pendown()  # 펜을 내려서 선이 그려지도록 합니다.
    goto(x2, y2)  # 두 번째 점으로 이동합니다.

def coosys():  # 좌표계를 그리는 함수입니다.
    line(-1, 0, N+1, 0)  # x 축을 그립니다.
    line(0, -0.1, 0, 1.1)  # y 축을 그립니다.

def plot(fun, start, color):  # 함수의 그래프를 그리는 함수입니다.
    pencolor(color)  # 펜의 색상을 지정합니다.
    x = start  # x의 시작값을 지정합니다.
    jumpto(0, x)  # 시작 위치로 이동합니다.
    pendown()  # 펜을 내려서 선이 그려지도록 합니다.
    dot(5)  # 시작 위치에 점을 찍습니다.
    for i in range(N):  # N번 반복하여
        x=fun(x)  # 주어진 함수에 x를 대입한 결과를 x에 저장하고,
        goto(i+1,x)  # 그 위치로 이동하여
        dot(5)  # 점을 찍습니다.

def main():  # 메인 함수입니다.
    reset()  # turtle 그래픽을 초기화합니다.
    setworldcoordinates(-1.0,-0.1, N+1, 1.1)  # 좌표계의 범위를 지정합니다.
    speed(0)  # 그리는 속도를 최대로 설정합니다.
    hideturtle()  # 거북이를 숨깁니다.
    coosys()  # 좌표계를 그립니다.
    plot(f, 0.35, "blue")  # 함수 f의 그래프를 파란색으로 그립니다.
    plot(g, 0.35, "green")  # 함수 g의 그래프를 초록색으로 그립니다.
    plot(h, 0.35, "red")  # 함수 h의 그래프를 빨간색으로 그립니다.
    for s in range(100):  # 100번 반복하여
        setworldcoordinates(0.5*s,-0.1, N+1, 1.1)  # 좌표계의 범위를 조정합니다.
    return "Done!"  # "Done!" 문자열을 반환합니다.

if __name__ == "__main__":  # 이 스크립트가 직접 실행되면
    main()  # 메인 함수를 실행합니다.
    mainloop()  # turtle 그래픽 창이 닫히지 않도록 합니다.


