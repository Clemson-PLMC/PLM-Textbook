from datetime import datetime, timedelta

from Gantt import Gantt, Task
from Gantt_Plotter import Gantt_Plotter

# Make tasks
tasks = list()
tasks.append(Task(1, "Assign tasks", timedelta(days=1)))
tasks.append(Task(2, "Design geometry", timedelta(days=21), [1]))
tasks.append(Task(3, "Establish manufacturing process", timedelta(days=3), [1]))
tasks.append(Task(4, "Identify new manufacturer", timedelta(days=10), [3]))
tasks.append(Task(5, "Source material sample", timedelta(days=12), [4]))
tasks.append(Task(6, "Prepare prototype frame", timedelta(days=8), [5]))
tasks.append(Task(7, "Perform suspension tests", timedelta(days=2), [6]))
tasks.append(Task(8, "Perform rideability tests", timedelta(days=3), [6]))
tasks.append(Task(9, "Perform durability tests", timedelta(days=3), [6]))
tasks.append(Task(10, "Perform peformance simulation", timedelta(days=2), [2]))
tasks.append(Task(11, "Approve design", timedelta(days=2), [7, 8, 9, 10]))
tasks.append(Task(12, "Propose to vendors", timedelta(days=28), [2]))
tasks.append(Task(13, "Verify manufacturing test run", timedelta(days=2), [11]))
tasks.append(Task(14, "Submit contract to manufacturer", timedelta(days=10), [13]))
tasks.append(Task(15, "Establish QA procedures", timedelta(days=9), [2]))
tasks.append(Task(16, "Verify manufacturing run", timedelta(days=1), [14, 15]))
tasks.append(Task(17, "Deliver to vendor", timedelta(days=1), [12, 16]))

# Form Gantt chart and plot
gantt = Gantt(tasks, datetime(year=2000, month=4, day=1, hour=8, minute=0))
plotter = Gantt_Plotter(gantt, title="Producing Bicycle Frame V2", xtick_format= ("%b %d", "date"))