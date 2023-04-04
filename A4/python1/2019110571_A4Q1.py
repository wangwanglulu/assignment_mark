class MyTxt():

    def __init__(self, path):
        self.path = path
        with open(self.path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.lines = lines

    def get_wdnum(self):
        count = 0
        for i in self.lines:
            i = i.strip()
            i_list = i.split(' ')
            a = len(i_list)
            count += a
        return count

    def record_num(self, file_name):
        num = self.get_wdnum()
        path = f'./{file_name}'
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(num))


a = MyTxt('./Harry_Potter.txt')
a.get_wdnum()
a.record_num('Count_Words.txt')
