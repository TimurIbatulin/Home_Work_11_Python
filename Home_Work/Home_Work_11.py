# Задача 3. Создайте класс Матрица. 
# Добавьте методы для: - вывода на печать, 
# - сравнения, 
# - сложения, 
# - *умножения матриц


def sum_matrix(matrix_1: list, matrix_2: list):
    answer_matrix = []
    insait_string = []
    if len(matrix_1) == len(matrix_2):
        for i in range (len(matrix_2)):
            if len(matrix_1[i]) == len(matrix_2[i]):
                for i_2 in range(len(matrix_2[i])):
                    insait_string.append(matrix_1[i][i_2] + matrix_2[i][i_2])
                    # answer_matrix[i][i_2] = 
            
            else:
                return False
            answer_matrix.append(insait_string)
            insait_string = []
        
    else:
        return False       
    return answer_matrix

def mul_matrix(matrix_1: list, matrix_2: list):
    temporarily_list = []
    ans_list = []
    temp = 0
    temp_1 = 0
    
    if len(matrix_2) == len(matrix_1[0]):
        print(f'{len(matrix_1) = }')
        for i in range(len(matrix_1)):
            count = 0
            for _ in range(len(matrix_1)):
                for k in range(len(matrix_1[0])):
                    temp = matrix_1[i][k] * matrix_2[k][count]
                    temp_1 += temp
                temporarily_list.append(temp_1)
                count += 1
                temp_1 = 0
                temp = 0
            ans_list.append(temporarily_list)
            temporarily_list = []
    return ans_list




class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix
    
    def __eq__(self, other):
        return self == other
    
    def __add__(self, other):
        return Matrix(sum_matrix(self.matrix, other.matrix))
    
    def __mul__(self, other):
        return Matrix(mul_matrix(self.matrix, other.matrix))
    
    def __repr__(self):
        return f'{self.matrix}'


if __name__ == '__main__':
    z_1 = [[2, 1], [-3, 0], [4, -1]]
    z_2 = [[5, -1, 6],[-3, 0, 7]]

    m_1 = Matrix(z_1)
    m_2 = Matrix(z_2)
    
    m_3 = m_1 + m_2

    m_4 = m_1 * m_2
    print(m_3)

    print(m_4)

    

    