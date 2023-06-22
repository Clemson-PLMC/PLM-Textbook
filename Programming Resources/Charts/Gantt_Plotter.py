import matplotlib.pyplot as plt
from numpy import arange
from datetime import datetime, timedelta

from Gantt import Gantt, Task

class Gantt_Plotter:
    def __init__(self, gantt: Gantt, **kwargs):
        self.gantt = gantt
        self.tasks = list(gantt.chart_tasks.keys())
        self.times = gantt.chart_tasks
        self.min_time = min(self.times.values())
        self.max_time = max([self.times[t] + t.duration for t in self.tasks])
        self.fig, self.ax = plt.subplots()

        defaultKwargs = { "title": "Gantt Chart", "inches_between_lines": 0.75, 
            "xtick_format": "pass", "bar_height": 0.8, "num_gridlines": 5, "ylabels": [t.id for t in self.tasks]}
        kwargs = {**defaultKwargs, **kwargs}
        self.ax.set_title(kwargs['title'])
        self.inches_between_gridlines = kwargs['inches_between_lines']
        self.bar_height = kwargs['bar_height']
        self.num_gridlines = kwargs['num_gridlines']
        self.ylabels = kwargs['ylabels']
        if kwargs["xtick_format"] == "pass": self.strf = self.set_xlabel_format()
        else:  self.strf = kwargs["xtick_format"]

        self.plotBars()

    def plotBars(self):
        self.formatPlot()
        for t in self.tasks:
            start = self.times[t]
            length = t.duration
            self.ax.broken_barh([(start, length)], (self.tasks.index(t)-self.bar_height/2, self.bar_height), facecolors='blue')
        plt.show()

    def formatPlot(self):
        self.ax.grid(True, axis="x")
        self.ax.set_xlim(self.min_time, self.max_time)
        self.ax.set_ylim(-1, len(self.tasks))
        xticks = [self.min_time + i * ((self.max_time - self.min_time) / self.num_gridlines) for i in range(self.num_gridlines + 1)]
        xlbls = [i.strftime(self.strf[0]) for i in xticks]
        self.ax.set_xticks(xticks, labels=xlbls)
        self.ax.set_yticks(arange(len(self.tasks)), labels=self.ylabels)
        self.ax.set_xlabel("Time (" + self.strf[1] + ")") 
        self.ax.set_ylabel("Task")  

    def set_xlabel_format(self):
        project_length = self.max_time - self.min_time
        if project_length < timedelta(seconds=1): return ("%f", "milliseconds")
        if project_length < timedelta(minutes=1): return ("%S", "seconds")
        if project_length < timedelta(hours=1): return ("%M", "minutes")
        if project_length < timedelta(days=1): return ("%H", "hours")
        if project_length < timedelta(months=1): return ("%d", "days")
        if project_length < timedelta(years=1): return ("%b", "months")
        return ("y", "years")


def example():
    tasks = list()
    tasks.append(Task(1, "Choose sandwich", timedelta(minutes=1)))
    tasks.append(Task(2, "Clean counter", timedelta(minutes=5)))
    tasks.append(Task(3, "Find ingredients", timedelta(minutes=3), [1]))
    tasks.append(Task(4, "Layout ingredients", timedelta(minutes=1), [2, 3]))
    tasks.append(Task(5, "Spread sauces", timedelta(minutes=1), [4]))
    tasks.append(Task(6, "Layer ingredients", timedelta(minutes=2), [5]))
    tasks.append(Task(7, "Gather eaters", timedelta(minutes=8), [2]))
    tasks.append(Task(8, "Give sandwich", timedelta(minutes=1), [7, 6]))
    tasks.append(Task(9, "Return ingredients", timedelta(minutes=2), [6]))
    tasks.append(Task(10, "Clean up", timedelta(minutes=5), [8, 9]))
    gantt = Gantt(tasks, datetime(year=2023, month=6, day=22, hour=0, minute=0))
    plotter = Gantt_Plotter(gantt, title="Making a Sandwich", xtick_format= ("%M:%S", "minutes"))

if __name__ == "__main__":
    example()