
from distutils.core import setup
setup(
  name = 'ImageConversion',         # How you named your package folder (MyLib)
  packages = ['IvNode'],   # Chose the same as "name"
  version = '1.8.0',      # Start with a small number and increase it with every change you make
  license='MIT',
  description = 'ImagingControls',
  author = 'IMG - Imagined',
  author_email = 'ING.email@domain.com',
  url = 'https://www.imgonline.com.ua/eng/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['MultiPurposeImagingLibrary'],
  install_requires=[
          'validators',
          'beautifulsoup4',
          'pynput',
          'pyautogui',
          'keyboard',
          'requests',
          ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: ANY',
    'Topic :: Software Development :',
    'License :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)