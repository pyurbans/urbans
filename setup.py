import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='urbans',
     version='0.0.1',
     author="Truong-Phat Nguyen",
     author_email="me@patrickphat.com",
     description="URBANS: Universal Rule-based Machine Translation NLP Toolkit",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/urbans/urbans",
     packages=setuptools.find_packages(exclude=['docs', 'tests', 'experiments']),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>3.6',
     install_requires =[
         'nltk<4',
         ],
     extras_require={
         'dev': [
             'pytest',
             'coverage',
             ],
     }
 )
