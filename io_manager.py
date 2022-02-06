class IoManager():
    def __init__(self, path):
        self.path = path
        self.lines = []
        self.dt = {}

    def read(self):
        try:
            with open(self.path) as file_c:
                for line in file_c:
                    self.lines.append(line.strip())
            self.lines.pop(0)
        except Exception as e:
            print(e)
            exit(0)

    def write(self, output_lines):
        fo = open(self.path, "w")
        try:
            fo.writelines(output_lines)
        except Exception as e:
            print(e)
            fo.close()
            exit(0)
        fo.close()

    def getDict(self):
        for line in self.lines:
            l = line.strip().split(',')
            self.dt[l[0]] = l[1]
        return self.dt