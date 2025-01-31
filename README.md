# Noise Tolerant Threshold Cryptography

## Prerequirements
 - A mosek license is required. Obtain a trial license [here](https://www.mosek.com/license/request/trial/)

## How-to

 - `codegen.py` creates the source code for our lp problem and prints it to stdout.
 - Pipe this output into a file and run it as a python file.
 - Edit `codegen.py` to change the values of `n`, `m`, `l`, `point`, `limit` as required.

```
python codegen.py > code.py
```

 ```
 python code.py
 ```
