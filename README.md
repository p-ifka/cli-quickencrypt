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

``` shell
python main.py en text 'test'
```

``` shell
python main.py de text 'gAAAAABlutje55bx5YeGUONwVUmbYcjhbT1uCMiCHkN1Rhzq88FSxGtPP2MHNR9eo7--ap3yv4vgeQ0Bf2nhBZ3U81HbyC9CAA==''
```



