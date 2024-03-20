def to_uppercase(s):
    """
    Вроде бы, я забыл написать докстринги в прошлый раз
    """
    return s.upper()


def capitalize_first_letters(s):
    """
    Преобразует первую букву каждого слова в строке в заглавную.

    :param s: Входная строка
    :return: Строка с заглавными первыми буквами слов
    """
    return ' '.join(word.capitalize() for word in s.split())
