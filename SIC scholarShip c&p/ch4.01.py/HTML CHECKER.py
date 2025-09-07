class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def list(self):
        return list(self.items)
    def clear(self):
        self.items = []

# def main():
#     stack1 = Stack()
#     stack2 = Stack()
#     with open("index.html", "r") as f:
#         index_cont = f.read()
#     for i in range(len(index_cont)):
#         if index_cont[i] == "<":
#             stack1.push("<")
#         elif index_cont[i] == ">":
#             stack2.push(">")
#         else:
#             continue
#     k=stack1.list()
#     p=stack2.list()
#     for i in range(len(k)):
#         if len(k) == len(p):
#             if k[i] == "<" and p[i] == ">" :
#
#                 continue
#             else :
#                 print(k[i], p[i],"a proplem here")
#                 break
#         else:
#             print("non symmetric")
#             exit()
#     print("symmetric")
# main()