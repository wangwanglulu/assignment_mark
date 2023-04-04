def input_ratio(r):
    def scale_factor(a):
        answer = []
        for n in range(5):
            answer.append(a*r**n)
        answer = tuple(answer)
        return answer
    return scale_factor

gs3 = input_ratio(3)
print(gs3(4))
