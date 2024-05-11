from __future__ import annotations
from typing import Any

class Element:
    def __init__(self, value: Any, priority: int) -> None:
        self.__dane = value
        self.__priorytet = priority

    def __It__(self, other: Element) -> bool:
        return self.__priorytet < other.__priorytet
    
    def __gt__(self, other: Element) -> bool:
        return self.__priorytet > other.__priorytet
    
    def __repr__(self) -> str:
        return f"{self.__priorytet} : {self.__dane}"

def shellSort(tab: list[Element]) -> None:
    n = len(tab)
    k = 1
    h = int((3**k - 1)/2)
    while h < n / 3:
        k += 1
        h = int((3**k - 1)/2)

    while h > 0:
        for i in range(h, n):
            j = i
            temp = tab[i]
            while tab[j - h] > temp and j >= h:
                tab[j] = tab[j - h]
                j -= h
            tab[j] = temp
        h = h//3
