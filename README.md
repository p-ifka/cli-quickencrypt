# CLI-QUICKENCRYPT
Simple python script to encrypt/decrypt text (string or text file) through a terminal 
## Dependencies 
* Python (obviously)
* Cryptography (https://pypi.org/project/cryptography/)
## Usage
Usage: quickencrypt [mode] [input type] [file/text]

**[mode]**: 'encrypt' (en) or 'decrypt' (de)

**[input type]**: 'file' ('-f') or 'text' ('-t')

**[File]**: /path/to/file

**[text]**: 'text here'

ex:
''' python main.py en text 'test' '''
''' python main.py de text 'gAAAAABlutdAmEj1Q90NL3MQ3sa-44tB93ru60irx3IBti4-BLT_BmeiuR4BC3XV6SeC9kpRnffXy4gApW1qI4i9_nwfC7Lw6w==' '''
