from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This Function will rerturn list of requirements
    '''
    
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    
    return requirements



# Metadata information of Entire project
setup(
name='mlproject_07032023',
version='0.0.1',
author='Mohammed Ismail',
author_email='ismail46h.shaikh@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
    
)