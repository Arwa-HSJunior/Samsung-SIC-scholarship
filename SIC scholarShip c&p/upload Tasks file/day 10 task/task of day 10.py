
# import re
# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if not self.isEmpty():
#             return self.stack.pop()
#         return None

#     def peek(self):
#         if not self.isEmpty():
#             return self.stack[-1]
#         return None

#     def size(self):
#         return len(self.stack)

#     def isEmpty(self):
#         return len(self.stack) == 0


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

#     return "Valid" if stack.isEmpty() else "Invalid"

# print(validation(html_page))


# list=list(input("enter a list").split())
# number_dict = {i: list[i]
# for i in list for i in range(len(list))
    
#     }
# print(number_dict)
        

# def frequency():
#     user_input = input("Enter text: ").split()
#     dict={}
#     for i in user_input:
    
#         if i in dict:
#             dict[i] += 1
#         else:
#             dict[i] = 1
#     return dict
     
# print(frequency())



def binary_search():
    nums=[1,2,3,4,5,6,7,8]
    start= nums[0]
    end = nums[-1]
    mid=(start+end)//2
    target = 3
    for i in range(len(nums)):
        if target < mid:
            start = mid +1
        elif target > mid:
            end = mid-1
        elif target == mid:
           return target 
        else:
            print("eror 404 :)")
                        

print(binary_search())
