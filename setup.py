from setuptools import find_packages,setup
setup(
    name='ragproject',
    version='0.0.1',
    author='mantu kumar',
    author_email='kumar290081998@gmail.com',
    install_requires=["openai","langchain","PyPDF2","streamlit","python-dotenv"],
    packages=find_packages()
)