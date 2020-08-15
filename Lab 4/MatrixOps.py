# Author:		Logan Hammond; lhammond12@student.umuc.edu
# Source File:  MatrixOps.py
# Description:  Allows user to input two 3x3 matrices and perform specific 
#               operations on them. 
# IDE:			AWS Cloud9

import numpy as np

class MatrixOps():
    """Allows users to input matrices and perform numpy functions on them. 

    Attributes:
        mat_A: list that will be made into numpy matrix from user input. 
        mat_B: list that will be made into numpy matrix from user input. 
        result_mat: list that will be into numpy matrix after numpy operations 
                    are applied to mat_A and mat_B. 
    """

    mat_A = []
    mat_B = []
    result_mat = []

    def playGame(self):
        """Starts game. 
        """

        self.mat_A = self.createMat()
        self.mat_B = self.createMat()
        self.getOp()


    def createMat(self):
        """Allows user to create numpy matrix from string input. 
        
        Returns:
            A: numpy array made from user string input. 
        """

        while True: 
            try: 
                print("\n\tEnter elements of 3x3 matrix left to right, row by" \
                " row, seperated by commas.")
                elements = []
                elements_str = input()
                # TODO determine how to allow input of multi-digit elements. 
                for ele in elements_str:
                    if not ele is "," and not ele is " ":
                        elements.append(int(ele))
                A = np.asarray(elements).reshape(3,3)
                return A
            except ValueError:
                print("Invalid input. Please try again.")


    def getOp(self):
        """Displays operation menu. 

        Displays operation menu to user and validates user input. When valid
        input is given function sends a string representation of the choice 
        to applyOp(). Menu repeats until valid input is given. 
        """

        # Display operation menu. Loop until valid input received. 
        choice_str = ""
        while True:
            print("\n\tSelect a matrix operation from the list below...")
            print("\n\ta. Addition")
            print("\tb. Subtraction")
            print("\tc. Dot product")
            print("\td. Multiplication by element")
            choice_str = input()
            
            # TODO determine most correct whitespace usage
            if choice_str is not "a" and \
               choice_str is not "b" and \
               choice_str is not "c" and \
               choice_str is not "d":
                print("\n\tInvalid input. Please try again.")
            else:
                self.applyOp(choice_str)
                break


    def applyOp(self, op):
        """Applies given operation to mat_A and mat_B. 

        Applies given operation too mat_A and mat_B. Prints result_mat after 
        resultant matrix is computed. Calculates row and column mean of 
        resultant matrix and displays these to user. 
        
        Args:
            op (string): letter representing operation to be applied. 
        """

        # Apply operations to matrices. 
        op_str = ""
        if op is "a":
            op_str = "addition"
            self.result_mat = np.add(self.mat_A, self.mat_B) 
        elif op is "b":
            op_str = "subtraction"
            self.result_mat = np.subtract(self.mat_A, self.mat_B)
        elif op is "c":
            op_str = "dot product"
            # TODO determine is np.dot() is more efficient that np.matmul(). 
            self.result_mat = np.matmul(self.mat_A, self.mat_B) 
        elif op is "d":
            op_str = "multiplication by element"
            self.result_mat = np.multiply(self.mat_A, self.mat_B)

        # Display resultant matrix and its' transpose. 
        print("\n\tYou selected {}. The result is: \n{}".format(op_str, 
        self.result_mat))
        print("\n\tThe transpose is: \n{}".format(np.transpose(
        self.result_mat)))
        print("\n\tThe row and column mean values of the result is:")
        
        # Calculate row and column mean of resultant matrix. 
        r1_mean = round((self.result_mat[0][0] + self.result_mat[1][0] 
        + self.result_mat[2][0]) / 3, 2)
        r2_mean = round((self.result_mat[0][1] + self.result_mat[1][1] 
        + self.result_mat[2][1]) / 3, 2)
        r3_mean = round((self.result_mat[0][2] + self.result_mat[1][2] 
        + self.result_mat[2][2]) / 3, 2)
        c1_mean = round((self.result_mat[0][0] + self.result_mat[0][1] 
        + self.result_mat[0][2]) / 3, 2)
        c2_mean = round((self.result_mat[1][0] + self.result_mat[1][1] 
        + self.result_mat[1][2]) / 3, 2)
        c3_mean = round((self.result_mat[2][0] + self.result_mat[2][1] 
        + self.result_mat[2][2]) / 3, 2)
        
        # Display row and column mean of resultant matrix. 
        print("\n\tRow:\t{}, {}, {}".format(r1_mean, r2_mean, r3_mean))
        print("\tColumn:\t{}, {}, {}".format(c1_mean, c2_mean, c3_mean))

def main():
    """Welcomes user to program and prompts user to begin playing game. 
    """
    
    # Initialize class and welcome user. 
    mops = MatrixOps()
    print("******Welcome to the Python Matrix Application******")

    # Prompt user to begin playing game. Loops until valid input received. 
    while True:
        choice_str = input("\n\tDo you want to play the matrix game? " \
        "(Y/N): ")
        
        if choice_str is "Y":
            mops.playGame()
        elif choice_str is "N":
            print("\n\tThanks for playing the matrix game!")
            break
        else:
            print("\n\tInvalid input. Please try again.")

if __name__ == "__main__":
    main()
