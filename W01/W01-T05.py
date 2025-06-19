# Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)  # длина списка чисел
        for i in range(n - 1):  # перебираем все числа, кроме последнего
            for j in range(i + 1, n):  # перебираем все последующие для каждого числа
                if (
                    nums[i] + nums[j] == target
                ):  # если нашли нужную сумму возвращаем индексы
                    return [i, j]
        return []  # возвращаем пустой список, если не нашли


# Palindrome Number


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (
            str(x) == str(x)[::-1]
        ):  # если преобразуемое число в строку равно перевернутой версии, то возвращаем True
            return True
        else:  # иначе False
            return False


# Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }  # словарь значений римских цифр
        r = 0  # счётчик, куда будет накапливаться итоговый результат

        for i in range(len(s)):  # перебираем все символы
            if (
                i < len(s) - 1 and m[s[i]] < m[s[i + 1]]
            ):  # если текущий символ меньше следующего, то вычитаем значение
                r -= m[s[i]]
            else:  # иначе прибавляем
                r += m[s[i]]
        return r


# Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = strs[0]  # берем первую строку за основу
        r_len = len(r)  # начальная длина префикса

        for i in strs[1:]:  # перебираем остальные строки
            while (
                r != i[0:r_len]
            ):  # укорачиваем префикс, пока он не станет началом текущей строки
                r_len -= 1  # уменьшаем длину префикса
                r = r[0:r_len]  # обновляем префикс
                if r_len == 0:  # если префикс пустой, возвращаем пустую строку
                    return ""
        return r  # возвращаем найденный префикс


# Valid Parentheses


def is_valid(s: str) -> bool:
    stack = []  # стек для хранения открывающих скобок
    pairs = {"(": ")", "[": "]", "{": "}"}  # соответствие скобок

    for char in s:  # перебираем все символы
        if char in pairs:  # если это открывающая скобка, добавляем в стек
            stack.append(char)
        else:  # иначе
            if (
                not stack or pairs[stack.pop()] != char
            ):  # если стек пуст или скобки не соответствуют, значит последовательность неверная
                return False  # возвращаем False

    return not stack  # если стек пуст, все скобки закрыты правильно
