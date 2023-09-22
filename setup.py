from setuptools import setup, find_packages, find_namespace_packages
setup(
    name = 'causalai',
    version = '2.0',
    packages=find_namespace_packages(include="*"),
    install_requires=["numpy>=1.22.2",
                    "matplotlib>=3.7.1",
                    "scikit-learn>=1.1.2", # "scikit-learn==0.24.2",
                    "scipy>=1.4.1",
                    "ray>=1.12.0",
                    "networkx>=2.4",
                    "lingam==1.5.5",
                    "flask>=2.2.2",
                    "flask_cors>=3.0.0",
                    "ges",
                    "ccit==0.4"
                    ]
)