from copy import deepcopy


"""This method calcualtes teterminant of matrix.

 determinantCalculation(). For example,

>>> determinantCalculation([1, 1, 1, 1, 1, 1, 1, 1, 1])
1
"""

def determinantCalculation(matrixarray):
    """Functon determinantCalculation calculates determinant of given matrix.

    Args:
        matrixarray - array representing matrix that should be calculated

    Returns:
        determinant of given matrix, a number.
    """


	#we need copy of array, not reference.
    matrixArray = deepcopy(matrixarray)
    #matrix is stored as list of 9 elementst, first rows, then columns beginning at te zero
    startIndexesP = [0, 3, 6]
    startIndexesM = [2, 5, 8]

    #part of determinants
    plusSide = 0
    minusSide = 0

    #calculate positive side of determinantn
    for start in startIndexesP:
        #set current index to start  index and inner multiply to 1
        currentIndex = start
        innerMultiply = 1
        #do-while replacement
        while True:
            if currentIndex > 8:
                #remov 9 as there are 9 elements in array beginning at tha zero
                innerMultiply = innerMultiply * matrixArray[currentIndex -9]
            else:
                innerMultiply = innerMultiply * matrixArray[currentIndex]
            currentIndex = currentIndex + 4

            #when current index is same as
            if currentIndex - 8 == start:
                break
        plusSide = plusSide + innerMultiply

    #iterate and calculate minus side of the determinant
    for start in startIndexesM:
        currentIndex = start
        innerMultiply = 1

        while True:
            if currentIndex > 8:
                #remov 9 as there are 9 elements in array beginning at tha zero
                innerMultiply = innerMultiply * matrixArray[currentIndex - 9]
            else:
                innerMultiply = innerMultiply * matrixArray[currentIndex]
            currentIndex = currentIndex + 2
            if currentIndex - 4 == start:
                break
        minusSide = minusSide + innerMultiply
    print(plusSide)
    print(minusSide)
    return plusSide - minusSide



"""This method replaces specified certain column in 3x3 matrix.

 replaceWithRightSides - replaces column  in matrix with vector of right sides

>>> replaceWithRightSides([1, 1, 1, 1, 1, 1, 1, 1, 1], [4,5,6], 0)
[4, 1 , 1, 5, 1, 1, 6, 1, 1]
"""

def replaceWithRightSides(matrixarray, vector, column):
    """Functon replaceWithRightSides replaces with vector of right sides.

    Args:
        matrixarray - array representing matrix that should be calculated
        vector  - array of three values representing vecotr of right sides.
        column - column to be replace, have to be in interval <0;2>

    Returns:
        determinant of given matrix, a number.
    """
    column = column % 3
    workingArray = deepcopy(matrixarray)
    workingArray[column] = deepcopy(vector[0])
    workingArray[column + 3] =  deepcopy(vector[1])
    workingArray[column + 6] = deepcopy(vector[2])

    return workingArray
