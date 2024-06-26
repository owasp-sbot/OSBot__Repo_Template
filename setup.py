import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("osbot_xyz/version", "r") as file_version:
    version = file_version.read().strip()

setuptools.setup(
    version                       = version                 ,
    name                          = "osbot_xyz"              ,
    author                        = "Dinis Cruz"            ,
    author_email                  = "dinis.cruz@owasp.org"  ,
    description                   = "OSBot - XYZ"            ,
    long_description              = long_description        ,
    long_description_content_type = "text/markdown"         ,
    url                           = "https://github.com/owasp-sbot/OSBot-Xyz",
    packages                      = setuptools.find_packages(),
    classifiers                   = [ "Programming Language :: Python :: 3"   ,
                                      "License :: OSI Approved :: MIT License",
                                      "Operating System :: OS Independent"   ])