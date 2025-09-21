Config = {"arrstr" : array("'hello'", "'yellow'")}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Config = Config, Schedule = Schedule, SensorSchedule = SensorSchedule):
    s1 = Task(
        task_id = "s1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "s1", "sourceType" : "Seed", "alias" : ""}
    )
    p1__Reformat_1 = Task(task_id = "p1__Reformat_1", component = "Model", modelName = "p1__Reformat_1")
    p1__Except_1 = Task(task_id = "p1__Except_1", component = "Model", modelName = "p1__Except_1")
    s1.out >> p1__Reformat_1.in_0
