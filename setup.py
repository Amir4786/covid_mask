import setuptools

with open("README.md", "r", encoding= "utf8") as f:
    long_description = f.read()

__version__= "0.0.3"

REPO_NAME= "covid_mask"
AUTHOR_USER_NAME= "Amir4786"
SRC_REPO= "covid_md"
AUTHOR_EMAIL= "er.a.khan47@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "Covid Mask Detection Project.",
    long_description= long_description,
    long_description_content= "text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where= "src")
)