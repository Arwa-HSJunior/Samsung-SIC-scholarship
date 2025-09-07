# # # with open('basic_html_page','r',encoding='utf-8') as file:
# # #     html_content = file.read()
# # #     stack = Stack()
# #
# # with open('basic_html_page.html','r',encoding='utf-8')as file:
# #       html_content= file.read()
# # print(html_content)
# #
# # def paired_Ups():
# #
# #     from stack import Stack###
# #     closing= "</title></head></h1></p></html>"
# #     stack = Stack()
# #     for ch in html_content:
# #         stack.push(ch)
# #     print(stack)
# #     #     elif ch in closing:
# #     #         if stack.isEmpty() != stack.pop():
# #     #             return "invalid"
# #     # return "valid" if not stack else "invalid"
# # print (paired_Ups())
#
# import re
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, value):
#         self.stack.append(value)
#
#     def pop(self):
#         if not self.isEmpty():
#             return self.stack.pop()
#         return None
#
#     def peek(self):
#         if not self.isEmpty():
#             return self.stack[-1]
#         return None
#
#     def size(self):
#         return len(self.stack)
#
#     def isEmpty(self):
#         return len(self.stack) == 0
# #
#
# html_page="""
# <html>
# <head>
# <title>Short Page</title>
# </head>
# <body>
# <h1>Hello World</h1>
# <p>This is a minimal pure HTML page.</p>
# </body>
# </html>"""
#
# paired_ups = {
#     "<head>": "</head>",
#     "<body>": "</body>",
#     "<h1>": "</h1>",
#     "<p>": "</p>",
#     "<html>": "</html>",
#     "<title>": "</title>"
# }
# def validation(html_page):
#     stack = Stack()
#     tokens = re.findall(r"</?[^>]+>", html_page)
#     for token in tokens:
#         token = token.strip()
#         if token in paired_ups.keys():  # opening
#             stack.push(token)
#         elif token in paired_ups.values():  # closing
#             if stack.isEmpty():
#                 return "Invalid"
#             last_open = stack.pop()
#             if paired_ups[last_open] != token:
#                 return "Invalid"
#
#     return "Valid" if stack.isEmpty() else "Invalid"
#
# print(validation(html_page    ))

### Balanced Parentheses Training Workbook ###

# -------------------------------
# Exercise 1 – Stack Basics
# -------------------------------
def exercise1():
    print("Exercise 1 – Stack Basics")
    stack = []

    # Push some numbers
    stack.append(1)
    stack.append(2)
    stack.append(3)

    print("Stack after pushing:", stack)  # expected [1, 2, 3]

    # Pop the last element
    last_item = stack.pop()   # fill here
    print("Popped item:", last_item)      # expected 3
    print("Stack now:", stack)            # expected [1, 2]")
    print("-" * 60)


# -------------------------------
# Exercise 2 – Matching Pairs Dictionary
# -------------------------------
def exercise2():
    print("Exercise 2 – Matching Pairs Dictionary")
    pairs = {')': '(', ']': '[', '}': '{'}

    # Try to get matching opening
    print(pairs[')'])   # expected '('
    print(pairs[']'])   # expected '['
    print("-" * 40)


# -------------------------------
# Exercise 3 – Simple Round Brackets
# # -------------------------------
# def exercise3():
#     print("Exercise 3 – Simple Round Brackets")
#
#     def is_valid_round(string):
#         stack = []
#         for ch in string:
#             if ch == '(':
#                 stack.append(ch)   # push
#             elif ch == ')':
#                 if not stack:   # stack empty
#                     return "Invalid"
#                 stack.pop()    # pop
#         # If stack is empty at the end → valid
#         if not stack:
#             return "valid"
#         else:
#             return "Invalid"
#
#     print(is_valid_round("((()))"))  # expected Valid
#     print(is_valid_round("(()"))     # expected Invalid
#     print("-" * 40)
#
#
# # -------------------------------
# # Exercise 4 – Count Different Brackets
# # -------------------------------
# def exercise4():
#     print("Exercise 4 – Count Different Brackets")
#
#     def count_brackets(s):
#         round_count = 0
#         square_count = 0
#         curly_count = 0
#
#         for ch in s:
#             if ch == '(' or ch == ')':
#                 round_count += 1
#             elif ch == '[' or ch == ']':
#                 square_count += 1
#             elif ch == '{' or ch == '}':
#                 curly_count += 1
#
#         print("Round:", round_count)
#         print("Square:", square_count)
#         print("Curly:", curly_count)
#
#     count_brackets("([{}])")
#     # expected: Round=2, Square=2, Curly=2
#     print("-" * 40)
#
#
# # -------------------------------
# # Exercise 5 – Full Balanced Parentheses
# # -------------------------------
# def exercise5():
#     print("Exercise 5 – Full Balanced Parentheses")
#
#     def is_valid_parentheses(s):
#         stack = []
#         pairs = {')': '(', ']': '[', '}': '{'}
#
#         for ch in s:
#             if ch in "([{":
#                 stack.append(ch)
#             elif ch in ")]}":
#                 if not stack or stack[-1] != pairs[ch]:
#                     return "Invalid"
#                 stack.pop()
#
#         return "Valid" if not stack else "Invalid"
#
#     print(is_valid_parentheses("{[()]}"))   # expected Valid
#     print(is_valid_parentheses("{[(])}"))   # expected Invalid
#     print(is_valid_parentheses(""))         # expected Valid
#     print("-" * 40)
#
#
# # -------------------------------
# # Run all exercises
# # -------------------------------
# if __name__ == "__main__":
#     exercise1()
#     exercise2()
#     exercise3()
#     exercise4()
#     exercise5()

class Stack:
    def __init__(self):
        self.items= []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        return self.items.append(item)
    def pop(self,item):
        return self.items.pop(item)
    def peek(self):
        return self.items[-1]
    def list(self):
        return list(self.items)
    def clear(self):
        self.items = []

# stack_family = Stack()
# stack_family.push("Baba")
# stack_family.push("Mama")
# stack_family.push("Zozy el nona")
# stack_family.push("Muhammed")
# stack_family.push("Menna")
# stack_family.push("Ahmed")
# stack_family.push("Marwa")
# stack_family.push("Alaa")
# stack_family.push("Omar(in progress)")

# # print(stack_family.pop())

# print(stack_family.list())

# print('peeked', stack_family.peek())

# stack_family.clear()

# print('_'*40)
# family_mem=['Arwa','Baba', 'Mama', 'Zozy el nona', 'Muhammed', 'Menna', 'Ahmed', 'Marwa', 'Alaa']
# print(family_mem)
# startA= Stack()
# for i in family_mem :
#     for ch in i:
#         if ch[0]== 'A':
#             startA.push(i)
#             break
# print(startA.list())


with open('ch4.01.py/basic_html_page.html','r',encoding='utf-8')as file:
      html_content= file.read()
      
print(html_content)

open = Stack()
close = Stack()

for ch in html_content:
    if ch == "<":
        open.push(ch)
    if ch == ch:
        open.pop(ch.index(ch))
        print(open)

