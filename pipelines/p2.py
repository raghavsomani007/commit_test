Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    s1 = Task(
        task_id = "s1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "s1", "sourceType" : "Seed", "alias" : ""}
    )
    Table_2 = Task(task_id = "Table_2", component = "Dataset", writeOptions = {"writeMode" : "overwrite"})
    p2__SQLStatement_0 = Task(task_id = "p2__SQLStatement_0", component = "Model", modelName = "p2__SQLStatement_0")
    Table_1 = Task(task_id = "Table_1", component = "Dataset", writeOptions = {"writeMode" : "overwrite"})
