#  ------ IMPORT LIBRARIES ------  #
from module_A import ClassA
from module_B import functionA
from module_C import ClassB


#  ------ MAIN FUNCTION ------  #
def main(arg1, arg2):
    """Main entry point of the program.

    This function coordinates the overall execution
    of the application by utilizing the functionality
    provided by the imported modules."""

    #  ADD CODE HERE FOR PRIMARY PROGRAMME EXECUTION USING IMPORTED MODULES  #
    obj1 = ClassA(arg1)
    obj2 = functionA(obj1)
    # ... etc ...


#  ------ MAIN PROGRAMME EXECUTION ------  #
if __name__ == "__main__":
    main()  # this function will be executed when running main.py
