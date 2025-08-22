Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    s1 = Task(
        task_id = "s1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "s1", "sourceType" : "Seed", "alias" : ""}
    )
    p1__DataCleansing_1 = Task(task_id = "p1__DataCleansing_1", component = "Model", modelName = "p1__DataCleansing_1")
    p1__Aggregate_1 = Task(task_id = "p1__Aggregate_1", component = "Model", modelName = "p1__Aggregate_1")
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3"), 
        isNew = True, 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          separator = ",", 
          nullValue = "", 
          encoding = "UTF-8", 
          header = True
        ), 
        fileOperationProperties = {"fileLoadingType" : "filepath", "includeFileNameColumn" : True}
    )
    OrchestrationSource_0 = Task(
        task_id = "OrchestrationSource_0", 
        component = "Dataset", 
        label = "OrchestrationSource_0", 
        table = {"name" : "{{ prophecy_tmp_source('p1', 'OrchestrationSource_0') }}", "sourceType" : "UnreferencedSource"}
    )
    OrchestrationSource_0.out >> OrchestrationSource_0.input_port_1
    OrchestrationSource_0.output_port_1 >> p1__Aggregate_1.in_0
