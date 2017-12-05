from . import Board_Elements


class Board_CL(object):
    def __init__(self):
        self._BOARD_DIC = Board_Elements.Board_Dic
        self._BOARD_ELEM = Board_Elements.Board_Elem

    @property
    def board_elem(self):
        return self._BOARD_ELEM

    @board_elem.setter
    def board_elem(self, value):
        print("elem setter run.")
        self._BOARD_ELEM = value
        Board_CL.Board_Elem = self._BOARD_ELEM

    @board_elem.deleter
    def board_elem(self):
        print("elem deleter run.")
        del self._BOARD_ELEM

    def append(self, value):
        self.board_elem = self.board_elem + [value]
        return self.board_elem

    @property
    def board_dic(self):
        return self._BOARD_DIC

    @board_dic.setter
    def board_dic(self, value):
        self._BOARD_DIC = value

    @board_dic.deleter
    def board_dic(self):
        print("dict_deleter run.")
        del self._BOARD_DIC

    def __getitem__(self, key):
        print("getitem run.")
        if isinstance(key, (int, str)):
            return self._BOARD_ELEM[key]
        if isinstance(key, tuple):
            if len(key) == 1:
                return self._BOARD_ELEM[key[0]]
            if len(key) == 2:
                x, y = key
                print(key)
                return self._BOARD_ELEM[x][y]
            if len(key) == 3:
                print(key)
                x, y, z = key
                return self._BOARD_ELEM[x][y][z]
            if len(key) == 4:
                print(key)
                x, y, z, xx = key
                return self._BOARD_ELEM[x][y][z][xx]
            if len(key) == 5:
                print(key)
                x, y, z, xx, xy = key
                return self._BOARD_ELEM[x][y][z][xx][xy]
            if len(key) == 6:
                print(key)
                x, y, z, xx, xy, xz = key
                return self._BOARD_ELEM[x][y][z][xx][xy][xz]
            if len(key) == 7:
                print(key)
                x, y, z, xx, xy, xz, yx = key
                return self._BOARD_ELEM[x][y][z][xx][xy][xz][yx]
            if len(key) == 8:
                print(key)
                x, y, z, xx, xy, xz, yx, yy = key
                return self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy]
            if len(key) == 9:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz = key
                return self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy][yz]
            if len(key) == 10:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx = key
                return self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy][yz][zx]
            if len(key) == 11:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx, zy = key
                return self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy][yz][zx][zy]
            if len(key) == 12:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx, zy, zz = key
                return self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy][yz][zx][zy][zz]
        else:
            print("Error: key must be tuple or int, but is", type(key))

    def __setitem__(self, key, value):
        print("setitem run.")
        if isinstance(key, (int, str)):
            self._BOARD_ELEM[key] = value
        if isinstance(key, tuple):
            if len(key) == 1:
                self._BOARD_ELEM[key[0]] = value
            if len(key) == 2:
                x, y = key
                print(key)
                self._BOARD_ELEM[x][y] = value
            if len(key) == 3:
                print(key)
                x, y, z = key
                self._BOARD_ELEM[x][y][z] = value
            if len(key) == 4:
                print(key)
                x, y, z, xx = key
                self._BOARD_ELEM[x][y][z][xx] = value
            if len(key) == 5:
                print(key)
                x, y, z, xx, xy = key
                self._BOARD_ELEM[x][y][z][xx][xy] = value
            if len(key) == 6:
                print(key)
                x, y, z, xx, xy, xz = key
                self._BOARD_ELEM[x][y][z][xx][xy][xz] = value
            if len(key) == 7:
                print(key)
                x, y, z, xx, xy, xz, yx = key
                self._BOARD_ELEM[x][y][z][xx][xy][xz][yx] = value
            if len(key) == 8:
                print(key)
                x, y, z, xx, xy, xz, yx, yy = key
                self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy] = value
            if len(key) == 9:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz = key
                self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy][yz] = value
            if len(key) == 10:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx = key
                self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy][yz][zx] = value
            if len(key) == 11:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx, zy = key
                self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy][yz][zx][zy] = value
            if len(key) == 12:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx, zy, zz = key
                self._BOARD_ELEM[x][y][z][xx][xy][xz][yx][yy][yz][zx][zy][zz] = value
        else:
            print("Error: key must be tuple or int, but is", type(key))
        Board_Elements.Board_Elem = self._BOARD_ELEM
