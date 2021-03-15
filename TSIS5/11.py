def size_of_text(fname):
    import os
    ans = os.stat(fname)
    return ans.st_size
print('File size in bytes of a plain file:',size_of_text('text.txt'))