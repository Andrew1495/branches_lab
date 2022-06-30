class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        rows = self.matrix_string.split("\n")
        for number in rows:
            int(number)
        return rows
            

    def column(self, index):
        pass
