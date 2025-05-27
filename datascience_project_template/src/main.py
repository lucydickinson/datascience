#  ------ IMPORT LIBRARIES ------  #
#  import functions/classes from your own modules, in addition to standard or third party packages
from dataset import load_data
from features import feature_engineer
import typer

#  ...

#  ------ CLI config ------  #
app = typer.Typer()


#  ------ MAIN FUNCTION ------  #
@app.command()
def main(arg1, arg2):
    """Docstring summary of main function.

    Args:
        arg1 (_type_): _description_
        arg2 (_type_): _description_

    Returns:
        _type_: _description_
    """

    #  ADD CODE HERE FOR MAIN EXECUTION OF ALL MODULES  #


#  ------ MAIN PROGRAMME EXECUTION ------  #
if __name__ == "__main__":
    main()  # this function will be executed when running main.py
