"""this module supplies methods for operation with matrixes.

Module suppliees methods for manipulation with matrixes, conversion of file to
matrix and vector of right sides and for check that iinput file is properly
formated
"""
from copy import deepcopy

"""This method calcualtes teterminant of matrix.

 determinantCalculation(). For example,

>>> determinantCalculationII(3)
1
"""


def determinantCalculationII(AAT):
    """Functon determinantCalculation calculates determinant of given matrix.

    Args:
        - matrixarray - array representing matrix that should be calculated

    Returns:
        - determinant of given matrix, a number.
    """
    return 1


"""This method calcualtes teterminant of matrix.

 determinantCalculation(). For example,

>>> determinantCalculation([1, 1, 1, 1, 1, 1, 1, 1, 1])
1
"""


def determinantCalculation(matrixarray):
    """Functon determinantCalculation calculates determinant of given matrix.

    Args:
        - matrixarray - array representing matrix that should be calculated

    Returns:
        - determinant of given matrix, a number.
    """
    # we need copy of array, not reference.
    matrixArray = deepcopy(matrixarray)
    # matrix is stored as list of 9 elementst, first rows,
    # then columns beginning at te zero
    startIndexesP = [0, 3, 6]
    startIndexesM = [2, 5, 8]

    # part of determinants
    plusSide = 0
    minusSide = 0

    # calculate positive side of determinantn
    for start in startIndexesP:
        # set current index to start  index and inner multiply to 1
        currentIndex = start
        innerMultiply = 1
        # do-while replacement
        while True:
            if currentIndex > 8:
                # remov 9 as there are 9 elements in array beginning at zero
                innerMultiply = innerMultiply * matrixArray[currentIndex - 9]
            else:
                innerMultiply = innerMultiply * matrixArray[currentIndex]
            currentIndex = currentIndex + 4

            # when current index is same as
            if currentIndex - 8 == start:
                break
        plusSide = plusSide + innerMultiply

    # iterate and calculate minus side of the determinant
    for start in startIndexesM:
        currentIndex = start
        innerMultiply = 1

        while True:
            if currentIndex > 8:
                # remov 9 as there are 9 elements in array beginning at zero
                innerMultiply = innerMultiply * matrixArray[currentIndex - 9]
            else:
                innerMultiply = innerMultiply * matrixArray[currentIndex]
            currentIndex = currentIndex + 2
            if currentIndex - 4 == start:
                break
        minusSide = minusSide + innerMultiply

    return plusSide - minusSide


"""This method replaces specified certain column in 3x3 matrix.

 replaceWithRightSides - replaces column  in matrix with vector of right sides

>>> replaceWithRightSides([1, 1, 1, 1, 1, 1, 1, 1, 1], [4,5,6], 0)
[4, 1 , 1, 5, 1, 1, 6, 1, 1]
"""


def replaceWithRightSides(matrixarray, vector, column):
    """Functon replaceWithRightSides replaces with vector of right sides.

    Args:
        - matrixarray - array representing matrix that should be calculated
        - vector  - array of three values representing vecotr of right sides.
        - column - column to be replace, have to be in interval <0;2>

    Returns:
        - output - determinant of given matrix, a number.
    """
    # just in case that somebody uses index greater than 2
    column = column % 3
    workingArray = deepcopy(matrixarray)
    workingArray[column] = deepcopy(vector[0])
    workingArray[column + 3] = deepcopy(vector[1])
    workingArray[column + 6] = deepcopy(vector[2])

    return workingArray


"""This method converts input from fiel to matrix.

 ConvertToMatrixAndVector - converts input from file to matrix an vector of
 right sides

>>> convertToMatrixAndVector(["1 1 1 1", "2 2 2 2", "3 3 3 3"], matrix, vector)
1
"""


def convertToMatrixAndVector(fileContent, matrix, vector):
    """Functon convertToMatrixAndVector checks and converts content.

    Functon convertToMatrixAndVector checks and converts content of file to
    matrix and vector of right sides.

    Args:
        - fileConetn - array of lines
        - matrix  - array representing matrix
        - vector - array, vector of right sides

    Returns:
        - output - 0 on failure, 1 on sucess.
    """
    if len(fileContent) < 3:
        print("File format problem: too few lines")
        return (0)

    if len(fileContent) > 3:
        print("File format problem: too many lines")
        return 0

    # now convert array to vector and matrix.
    for line in fileContent:
        column = 0
        # trim new line from line and spit it by delimieter, delimiter is space
        lineArray = line.rstrip("\n").split(" ")
        if len(lineArray) != 4:
            print("Invalid number of cloumns in file. File must contain 4 colu\
            mns, 3 for matrix and 1 for vector of right sides")
            return 0

        for element in lineArray:
            try:
                elementValue = float(element)
            except ValueError:
                print("Input Error! "+element+" can't be converted to string")
                return 0

            # first three columns are of
            if column == 3:
                vector.append(elementValue)
            else:
                matrix.append(elementValue)
            # culumn counter increment
            column += 1

    return 1
