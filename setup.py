from setuptools import setup

setup(name='kollari',
      version='0.1',
      description='A tool for publishing and operating a scholarly journal',
      scripts=['scripts/kollari'],
      url='http://github.com/ryneches/kollari',
      author='Russell Neches',
      author_email='ryneches@ucdavis.edu',
      license='BSD',
      packages=['kollari'],
      package_data = {'kollari' : ['templates/article.html', 'templates/article.tex'] },
      include_package_data=True,
      zip_safe=False)
