class MyStack:
    def __init__(self, length) -> None:
        self.s = [0] * length
        self.top = -1

    def push(self,data):
        if not self.is_full():
            self.top += 1
            self.s[self.top] = data
        else:
            raise Indexerror('가득 차있습니다.')
    # 마지막 요소를 삭제하면서 반환
    def pop(self):
        if not self.is_empty():
            last = self.top
            self.top -= 1
            return self.s[last]
        raise IndexError('스택이 비었습니다.')
    # 마지막 요소를 그냥 반환
    def peek(self):
        if not self.is_empty():
            return self.s[self.top]
        raise Valueerror('스택이 비었습니다.')

    def is_full(self):
        if self.top == len(self.s) - 1:
            return True
        return False

    def is_empty(self):
        if self.top == -1:
            return True
        return False


stack = MyStack(10)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_full())
