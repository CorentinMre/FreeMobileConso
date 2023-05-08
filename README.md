<br>
<p align="center"><img width="400" alt="Logo" src="https://raw.githubusercontent.com/CorentinMre/FreeMobileConso/main/images/logoV2.png"></a></p>

<br/>


<h2 style="font-family: sans-serif; font-weight: normal;" align="center">An API for get<strong> Free mobile </strong>Consommation</h2>


<br/>


[![pypi version](https://img.shields.io/pypi/v/FreeMobileConso.svg)](https://pypi.org/project/FreeMobileConso/)
[![python version](https://img.shields.io/pypi/pyversions/FreeMobileConso.svg)](https://pypi.org/project/FreeMobileConso/)
[![license](https://img.shields.io/pypi/l/FreeMobileConso.svg)](https://pypi.org/project/FreeMobileConso/)

## Description
A python API for get your consommation of your Free mobile account


## Dependencies

- requests
- bs4

## Usage


- `pip3 install FreeMobileConso`

Here is an example script:

```python

import FreeMobileConso


client = FreeMobileConso.Client(
                        "<identifiant>",
                        "<password>"
                        )


conso = client.getConso()


print(conso)

```


## LICENSE

Copyright (c) 2022 CorentinMre

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.