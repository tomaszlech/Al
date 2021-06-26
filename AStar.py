import numpy
from AStarState import AStarState

class AStar:
    def returnPath(self, currentNode, grid):
        path = []
        noRows, noColumns = numpy.shape(grid)
        result = [[-1 for i in range(noColumns)] for j in range(noRows)]
        current = currentNode
        while current is not None:
            path.append(current.position)
            current = current.parent
        path = path[::-1]
        startValue = 0
        for i in range(len(path)):
            result[path[i][0]][path[i][1]] = startValue
            startValue+=1
        return result
######################################################### w current jest koszt do przebycia
    def search(self, start, end, grid, cost, flaga): #start to kordy wózka, end miejsce podjęcia paczki
        noRows, noColumns = numpy.shape(grid)
        startNode = AStarState(None, tuple(start))
        endNode = AStarState(None, tuple(end))
        startNode.g = 0
        startNode.h = 0
        startNode.f = 0
        endNode.g = 0
        endNode.h = 0
        endNode.f = 0
        toVisit = []
        visited = []
        toVisit.append(startNode)
        iterations = 0
        max = (len(grid) // 2) ** 10
        moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while len(toVisit)>0:
            iterations=iterations+1
            current = toVisit[0]
            currentIndeks = 0
            for indeks, item in enumerate(toVisit):
                if item.g<current.g:
                    current = item
                    currentIndeks = indeks
            if iterations>max and flaga == 0: #podprojekt genetyczne
                return current.g
            if iterations>max:
                return self.returnPath(current, grid)
            visited.append(current)
            toVisit.pop(currentIndeks)
            if current==endNode and flaga == 0:
                return current.g
            if current==endNode:
                return self.returnPath(current, grid)       #zwracanie wagi przejscia
            children = []
            for new in moves:
                positions = (current.position[0]+new[0], current.position[1]+new[1])

                if (positions[0] > (noRows - 1) or
                    positions[0] < 0 or
                    positions[1] > (noColumns - 1) or
                    positions[1] < 0):
                    continue
                """ podprojekt genetyczne"""
                if grid[positions[0]][positions[1]] == 2 and flaga == 0:
                    children.append(AStarState(current, positions))
                    continue

                if grid[positions[0]][positions[1]]!=0:
                    continue

                children.append(AStarState(current, positions))
            for child in children:

                if len([visitedChild for visitedChild in visited if visitedChild==child])>0:
                    continue

                if child.position[0]<=(len(grid)-4) and child.position[0]>=3 and child.position[1]>=4 and child.position[1]<=(len(grid[0])-1):
                    child.g = current.g + (10 * cost)
                else:
                    child.g = current.g + cost
                child.h = (((child.position[0]-endNode.position[0]) ** 2) + ((child.position[1]-endNode.position[1]) ** 2))
                child.f = child  .g + child.h

                if len([i for i in toVisit if child==i and child.g>i.g])>0:
                    continue

                toVisit.append(child)




