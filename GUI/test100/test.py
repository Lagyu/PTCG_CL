

list100 = [[["test" for i in range(2)] for j in range(3)]for k in range(10)]


class SomeList(object):
    def __init__(self):
        global list100
        self._SomeList = list100

    @property
    def somelist(self):
        print("property run.")
        return self._SomeList

    @somelist.setter
    def somelist(self, value):
        global list100
        print("setter run.")
        self._SomeList = value
        list100 = self._SomeList

    def __getitem__(self, key):
        print("getitem run.")
        if isinstance(key, (int, str)):
            return self._SomeList[key]
        if isinstance(key, tuple):
            if len(key) == 1:
                return self._SomeList[key[0]]
            if len(key) == 2:
                x, y = key
                print(key)
                return self._SomeList[x][y]
            if len(key) == 3:
                print(key)
                x, y, z = key
                return self._SomeList[x][y][z]
            if len(key) == 4:
                print(key)
                x, y, z, xx = key
                return self._SomeList[x][y][z][xx]
            if len(key) == 5:
                print(key)
                x, y, z, xx, xy = key
                return self._SomeList[x][y][z][xx][xy]
            if len(key) == 6:
                print(key)
                x, y, z, xx, xy, xz = key
                return self._SomeList[x][y][z][xx][xy][xz]
            if len(key) == 7:
                print(key)
                x, y, z, xx, xy, xz, yx = key
                return self._SomeList[x][y][z][xx][xy][xz][yx]
            if len(key) == 8:
                print(key)
                x, y, z, xx, xy, xz, yx, yy = key
                return self._SomeList[x][y][z][xx][xy][xz][yx][yy]
            if len(key) == 9:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz = key
                return self._SomeList[x][y][z][xx][xy][xz][yx][yy][yz]
            if len(key) == 10:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx = key
                return self._SomeList[x][y][z][xx][xy][xz][yx][yy][yz][zx]
            if len(key) == 11:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx, zy = key
                return self._SomeList[x][y][z][xx][xy][xz][yx][yy][yz][zx][zy]
            if len(key) == 12:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx, zy, zz = key
                return self._SomeList[x][y][z][xx][xy][xz][yx][yy][yz][zx][zy][zz]
        else:
            print("Error: key must be tuple or int, but is", type(key))

    def __setitem__(self, key, value):
        print("setitem run.")
        if isinstance(key, (int, str)):
            self._SomeList[key] = value
        if isinstance(key, tuple):
            if len(key) == 1:
                self._SomeList[key[0]] = value
            if len(key) == 2:
                x, y = key
                print(key)
                self._SomeList[x][y] = value
            if len(key) == 3:
                print(key)
                x, y, z = key
                self._SomeList[x][y][z] = value
            if len(key) == 4:
                print(key)
                x, y, z, xx = key
                self._SomeList[x][y][z][xx] = value
            if len(key) == 5:
                print(key)
                x, y, z, xx, xy = key
                self._SomeList[x][y][z][xx][xy] = value
            if len(key) == 6:
                print(key)
                x, y, z, xx, xy, xz = key
                self._SomeList[x][y][z][xx][xy][xz] = value
            if len(key) == 7:
                print(key)
                x, y, z, xx, xy, xz, yx = key
                self._SomeList[x][y][z][xx][xy][xz][yx] = value
            if len(key) == 8:
                print(key)
                x, y, z, xx, xy, xz, yx, yy = key
                self._SomeList[x][y][z][xx][xy][xz][yx][yy] = value
            if len(key) == 9:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz = key
                self._SomeList[x][y][z][xx][xy][xz][yx][yy][yz] = value
            if len(key) == 10:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx = key
                self._SomeList[x][y][z][xx][xy][xz][yx][yy][yz][zx] = value
            if len(key) == 11:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx, zy = key
                self._SomeList[x][y][z][xx][xy][xz][yx][yy][yz][zx][zy] = value
            if len(key) == 12:
                print(key)
                x, y, z, xx, xy, xz, yx, yy, yz, zx, zy, zz = key
                self._SomeList[x][y][z][xx][xy][xz][yx][yy][yz][zx][zy][zz] = value
        else:
            print("Error: key must be tuple or int, but is", type(key))
        global list100
        list100 = self._SomeList

print(list100)
SomeList()[8,1,1] = "Changed"  # setter doesn't run.
print(list100)