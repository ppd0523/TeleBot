import os.path

def save(path, value, overwrite=True):
    if os.path.isfile(path) and (overwrite is False):
        return False
    else:
        with open(path, 'w') as file:
            file.write(str(value))
        return True

def load(path):
    """
    return :
        None 파일이 없을 때
        '' 내용이 없을 때
        문자열 값이 있을 때
    """
    if os.path.isfile(path):
        with open(path, 'r') as file:
            return file.readline()
    else:
        return None