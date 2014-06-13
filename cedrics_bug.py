Last login: Fri May 23 09:25:16 on ttys000
Cedric ~ $ python
Python 2.7.5 (v2.7.5:ab05e7dd2788+, May 15 2013, 18:43:04) 
[GCC 4.0.1 (Apple Inc. build 5493)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import StringIO
>>> import sys
>>> sys.stdout = mystdout = StringIO.StringIO()
>>> print "apples and oranges"
>>> sys.stdout = sys.__stdout__
>>> mystdout.getvalue()
'apples and oranges\n'
>>> exit(1)
Cedric ~ $ python
Python 2.7.5 (v2.7.5:ab05e7dd2788+, May 15 2013, 18:43:04) 
[GCC 4.0.1 (Apple Inc. build 5493)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import StringIO
>>> import sys
>>> sys.stdout = mystdout = StringIO.StringIO()
>>> print "apples and oranges"
>>> mystdout.getvalue()
>>> mystdout.close()
>>> mystdout.getvalue()
Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
        File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/http://StringIO.py", line 269, in getvalue
            _complain_ifclosed(self.closed)
              File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/http://StringIO.py", line 40, in _complain_ifclosed
                  raise ValueError, "I/O operation on closed file"
              ValueError: I/O operation on closed file
              >>> sys.stdout = mystdout = StringIO.StringIO()
              >>> mystdout.getvalue()
              >>> print "apples and oranges"
              >>> mystdout.getvalue()
              >>>
