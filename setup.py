import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='rumbamt',  
     version='0.1',
     scripts=['rubamt'] ,
     author="Patrick Phat",
     author_email="me@patrickphat.com",
     description="Context-free grammar rule-based machine translation package",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/patrickphat/rubamt",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )