class Matrix:
    def __init__(self, row = 2, col = 2):
        self.row_count = row
        self.col_count = col
        self.mat = self.assign_matrix(self.row_count,self.col_count)

    @staticmethod
    def assign_matrix( row, col):
        mat = [[0 for i in range(col)] for j in range(row)]
        return mat

    def setter(self, *argv):
        try:
            for i,j in enumerate(argv[0]):
                if(j.__len__() != self.mat[i].__len__()):
                    raise IndexError
            ls = argv[0]    
            self.mat = ls
        except: 
            print("Set Matric values : ")
            for i in range(self.row_count):
                for j in range(self.col_count):
                    self.mat[i][j] = int(input(f'mat[{i}][{j}]'))
        
        self.__repr__()

    def __add__(self, other):
        try:
            if(self.row_count != other.row_count or self.col_count != other.col_count):
                raise IndexError

            result = Matrix(self.row_count, self.col_count)
            for row in range(self.row_count):
                for col in range(self.col_count):
                    result.mat[row][col] = self.mat[row][col] + other.mat[row][col]
            return result
        except IndexError as ie:
            print("number of row and column of both matrix is not equal")

        return None

    def __mul__(self, other):
        try:
            if(self.col_count != other.row_count):
                raise IndexError
            else:
                result = Matrix(self.row_count, other.col_count)
                for row in range(self.row_count):
                    for col in range(other.col_count):
                        for k in range(self.col_count):
                            result.mat[row][col] = result.mat[row][col] + (self.mat[row][k] * other.mat[k][col])
                
                return result
        except:
            print("Matrix Multiplication not possible")
        
        return None

    def __sub__(self, other):
        try:
            if(self.row_count != other.row_count or self.col_count != other.col_count):
                raise IndexError

            result = Matrix(self.row_count, self.col_count)
            for row in range(self.row_count):
                for col in range(self.col_count):
                    result.mat[row][col] = self.mat[row][col] - other.mat[row][col]
            return result
        except IndexError as ie:
            print("number of row and column of both matrix is not equal")

        return None

    def __repr__(self):
        mat_str = ""
        for i in self.mat:
            mat_str = mat_str + str(i) + "\n"
        
        return "Matrix is : \n" + mat_str