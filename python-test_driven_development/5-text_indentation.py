#!/usr/bin/python3
"""
 This function that prints a text with 2 new lines
 after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Return: the result of the text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(result, end="")
