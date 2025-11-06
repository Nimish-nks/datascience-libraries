from setuptools import find_packages,setup
from typing import List

# you don't want HYPEN_E_DOT in your requirements
HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    """This function will return list of requirements

    Args:
        file_path (str): your requirements.txt path

    Returns:
        List[str]: returns list
    """

    requirements=[]
    with open(file_path) as file_obj:
        # read line wise
        requirements=file_obj.readlines()
        # replace \n
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)




setup(
name='ml_project',
version='0.0.1',
author='Nimish',
author_email='nkssrk007@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)