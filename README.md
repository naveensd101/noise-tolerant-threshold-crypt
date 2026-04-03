# Noise Tolerant Threshold Cryptography

## Optional
 - A mosek license can be obtained [here](https://www.mosek.com/license/request/trial/) to solve for larger values of `n` and `k`

## How-to

 - `eqgen.py` generates equations to be solved by the lp solver in `eqn.txt`.
 - Edit `eqgen.py` to change the values of `n`, `m`, `l`, `point`, `limit` as required.
 - `code.py` will read `eqn.txt` and solve the lp.

```
python eqgen.py
```

 ```
 python code.py
 ```
