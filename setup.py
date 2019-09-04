from distutils.core import setup

setup(
  name = 'sorting',         # How you named your package folder (MyLib)
  packages = ['sorting'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Package for visualizing sorting algorithms',   # Give a short description about your library
  author = 'Martin Moldsvor',                   # Type in your name
  author_email = 'martin@moldsvor.com',      # Type in your E-Mail
  url = 'https://github.com/mmoldsvor/sortingproject/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mmoldsvor/sortingproject/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['Sorting', 'Algorithm', 'Visualization'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development',    'License :: MIT License',   # Again, pick a license    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.7',
  ],
)