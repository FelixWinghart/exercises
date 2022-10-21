from abc import abstractmethod, ABC
from pydoc import doc
from sre_constants import FAILURE
from typing import Tuple
from numpy import empty

from pyparsing import null_debug_action

from pdm4ar.exercises.ex02.structures import AdjacencyList, X, Path, OpenedNodes


class GraphSearch(ABC):
    @abstractmethod
    def search(self, graph: AdjacencyList, start: X, goal: X) -> Tuple[Path, OpenedNodes]:
        """
        :param graph: The given graph as an adjacency list
        :param start: The initial state (i.e. a node)
        :param goal: The goal state (i.e. a node)
        :return: The path from start to goal as a Sequence of states, None if a path does not exist
        """
        pass


class DepthFirst(GraphSearch):
    def search(self, graph: AdjacencyList, start: X, goal: X) -> Tuple[Path, OpenedNodes]:
        # todo implement here your solution
        q = [start]                 #Queue with the starting state (ToDo)
        v = []                      #Visited set
        path = []
        #parent[start] = None

        while q:       #While there is an element in the ToDo list, do:
            s = q.pop(0)            #Our current state s is at the first element of the ToDo list
            v.append(s)             #Add current state to visited
            if goal not in path:
                path.append(s)          #Add current state to the path
            if s == goal:
                return [path, v]
            u = 0
            #if graph[s] in (v + q):
            #    index = v.index(q[0])
            #    path -= v[index:]
            #else:
            for i in sorted(graph[s]):
                #if i == goal:
                    #return [path + [i], v + [i]]
                
                #if i in (q)

                if i not in (v + q):
                    q.insert(u, i)
                    u += 1
                    if i == goal:
                        if i not in path:
                            path.append(i)
                #if i in v:
                #    index = path.index(i) + 1
                #    del path[index:]
        return [[], v]



class BreadthFirst(GraphSearch):
    def search(self, graph: AdjacencyList, start: X, goal: X) -> Tuple[Path, OpenedNodes]:
        # todo implement here your solution
        q = [start]             #Queue with the starting state (ToDo)
        v = []                  #Visited set
        path = []

        while q:       #While Q is not empty
            s = q.pop(0)            #Remove the first from the ToDo list and add it to S
            v.append(s)             #Set the first on ToDo list as visited
            if goal not in path:
                path.append(s)          #Add current state to the path
            if s == goal:
                return [path, v]
            for i in sorted(graph[s]):
                #if i == goal:
                    #return [path + [i], v + [i]]
                if i not in (v + q):
                    q.append(i)
                    if i == goal:
                        if i not in path:
                            path.append(i)
        return [[], v]


class IterativeDeepening(GraphSearch):
    def search(self, graph: AdjacencyList, start: X, goal: X) -> Tuple[Path, OpenedNodes]:
        # todo implement here your solution
        q = [start]            #Queue with the starting state (ToDo)
        v = []            #Visited set
        path = []
        #d = 1                   #Iterator
        #m = 1

        while q:
            s = q.pop(0)
            v.append(s)
            if goal not in path:
                path.append(s)
            if s == goal:
                return [path, v]
            #p = len(graph[s])

            u = 0
            for i in sorted(graph[s]):
                #if m <= d:
                    if i not in (v + q):
                        q.append(i)
                        u += 1
                        if i == goal:
                            if i not in path:
                                path.append(i)
        return [[], v]
