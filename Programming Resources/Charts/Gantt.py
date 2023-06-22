from datetime import datetime, timedelta

class Task:
    def __init__(self, id: int, name: str, duration = timedelta(days=1), parents: list = list()):
        self.id = id
        if type(duration) == float:
            self.duration = timedelta(days = duration)
        else: self.duration = duration
        self.name = name
        self.duration = duration
        self.parents = parents

    def toString(self)-> str:
        return "Task: " + self.name + " (" + str(self.id) + ")"


class Gantt:
    def __init__(self, tasks: list=list(), start_date: datetime= datetime.now()):
        self.start_date = start_date
        self.tasks = tasks
        self.chart_tasks = dict()
        self.sort()

    def addTask(self, task: Task):
        self.tasks.append(task)

    def sort(self):
        self.chart_tasks.clear()
        q = list(self.tasks)
        roots = self.findRoots(q)
        for r in roots:
            self.addChildren(r, q)
        if len(q) != 0:
            message = "The following tasks are not part of the main sequence:\n"
            for t in q:
                message += "\t" + t.toString() + "\n" 
            raise Exception(message)

    def findChildren(self, t: Task, q: list):
        children = list()
        for a in q:
            for p in a.parents:
                if p == t.id: children.append(a)
        return children

    def addChildren(self, t: Task, q: list):
        if self.parentsInChart(t):
            self.chart_tasks.update({t: self.getTaskStartDate(t)})
            q.remove(t)
            children = self.findChildren(t, q)
            for c in children:
                self.addChildren(c, q)

    def getTaskStartDate(self, t: Task)-> datetime:
        if len(t.parents) == 0: return self.start_date
        parents = self.findTasksByIds(t.parents)
        latest = self.chart_tasks[parents[0]] + parents[0].duration
        for p in parents:
            check = self.chart_tasks[p] + p.duration
            if check > latest: latest = check
        return latest

    def findTasksByIds(self, l: list)-> list:
        out = list()
        for id in l:
            foundFlag = False
            for t in self.tasks:
                if t.id == id: 
                    out.append(t)
                    foundFlag = True
                    continue
            if not foundFlag:
                msg = "Parent id " + str(id) + " not found"
                raise Exception(msg)
        return out

    def parentsInChart(self, t: Task)-> bool:
        parents = self.findTasksByIds(t.parents)
        for p in parents:
            if p in self.chart_tasks: continue
            else: return False
        return True
        
    def findRoots(self, to_add: list)-> list:
        roots = list()
        for t in to_add:
            if len(t.parents) == 0: 
                roots.append(t)
        return roots

    def toString(self)-> str:
        out = str()
        for t in self.chart_tasks.keys():
            out += (t.toString() + "; " + self.chart_tasks[t].strftime("%H:%M:%S") + "\n")
        return out
        

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
    print(gantt.toString())
    

if __name__ == "__main__":
    example()
