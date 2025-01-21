class Path():

    def __init__(self):
        self.width = 6 # 최대 좌표
        self.height = 6

        self.hey = 0
    

    def calculatePath(self, x: int, y: int, target: tuple, possiblePath = [], usedPath = []):

        count = 0

        if x == target[0] and y == target[1]:
            self.hey += 1
            print(self.hey)
            return 1

        if len(possiblePath) == 0:
            possiblePath = self.getPossiblePath(x, y, usedPath)

        if len(possiblePath) == 0:
            return 0
        
        # print(str(x), str(y), str(len(usedPath)))
        
        for p in possiblePath:

            recentUsedPath = []
            for u in usedPath:
                recentUsedPath.append(u)
            
            recentUsedPath.append((x, y))

            count += self.calculatePath(p[0], p[1], target, self.getPossiblePath(p[0], p[1], recentUsedPath), recentUsedPath)
        
        return count

    def getPossiblePath(self, x: int, y: int, usedPath = []):

        p = []

        if x != 0 and not (x - 1, y) in usedPath: 
            p.append((x - 1, y))
        # 우
        if x != self.width and not (x + 1, y) in usedPath:
            p.append((x + 1, y))
        
        # 상
        if y != 0 and not (x, y - 1) in usedPath:
            p.append((x, y - 1))
        
        # 하
        if y != self.height and not (x, y + 1) in usedPath:
            p.append((x, y + 1))

        return p





if __name__ == '__main__':
    c = Path()

    print(c.calculatePath(0, 0, (c.width, c.height)))