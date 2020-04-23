"""

Log in or Sign up


CCC '05 J5 - Bananas View as PDF

Submit solution

All submissions

Best submissions

Points:10

Time limit:1.0s

Memory limit:64M

Problem types

The term "code monkey" is sometimes used to refer to a programmer who doesn't know much about programming. This is unfair to monkeys, because contrary to popular belief, monkeys are quite smart. They have just been misunderstood. This may be because monkeys do not speak English, but only monkey language. Your job is to help humans and monkeys understand each other by writing a monkey language dictionary. For each word that is typed in, your program must determine whether it is a valid monkey language word.

Unlike in English, spelling in monkey language is very simple. Every word in monkey language satisfies the following rules, and every word satisfying the following rules is a monkey language word.

A monkey language word is a special type of word called an A-word, which may be optionally followed by the letter Nand a monkey language word.An A-word is either only the single letter A, or the letter B followed by a monkey language word followed by the letter S.

Here are some examples:

The word A is a monkey language word because it is an A-word.The word ANA is a monkey language word because it is the A-word A followed by the letter N and the monkey language word A.The word ANANA is a monkey language word because it is the A-word A followed by the letter N and the monkey language word ANA.The word BANANAS is a monkey language word because it is an A-word, since it is the letter B followed by the monkey language word ANANA followed by the letter S.

Write a program which accepts words, one word on each line, and for each word prints YES if the word is a monkey language word, and NO if the word is not a monkey language word. The input word "X" indicates the program should terminate, and there is no output for word "X" (even though it is not a monkey word).

Credits: https://dmoj.ca/problem/ccc05j5
"""
