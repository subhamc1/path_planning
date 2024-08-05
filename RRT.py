from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')
from matplotlib.patches import Circle

from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap


class gen_image:
    def generate_image(start_x,start_y,end_x,end_y,num):
        plt.clf()
        dimensions = (500, 500)
        start = (int(start_x), int(start_y))
        goal = (int(end_x), int(end_y))
        obsdim = 20
        obsnum = int(num)
        iteration = 0

        fig = plt.figure(num='RRT Path Planning', figsize=(10, 10))
        plt.xlim(0, 500)
        plt.ylim(0, 500)
        map = RRTMap(start, goal, dimensions, obsdim, obsnum)
        graph = RRTGraph(start, goal, dimensions, obsdim, obsnum)


        obstacles = graph.makeobs()
        map.drawMap(obstacles)

        while (not graph.path_to_goal()):
            if iteration % 10 == 0:
                X, Y, Parent = graph.bias(goal)
                Circle1 = Circle((X[-1], Y[-1]), map.nodeRad + 2, facecolor='gray', fill = 0)
                fig.gca().add_patch(Circle1)
                plt.plot((X[-1], X[Parent[-1]]), (Y[-1], Y[Parent[-1]]), 'blue')
            else:
                X, Y, Parent = graph.expand()
                Circle1 = Circle((X[-1], Y[-1]), map.nodeRad + 2, facecolor='gray', fill=0)
                fig.gca().add_patch(Circle1)
                plt.plot((X[-1], X[Parent[-1]]), (Y[-1], Y[Parent[-1]]), 'blue')

            # if iteration % 5 == 0:
            #     fig.canvas.draw()
            iteration += 1

        map.drawPath(graph.getPathCoords())

        plt.savefig('./static/solution.png')



