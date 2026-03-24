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
    s1_1 = Task(
        task_id = "s1_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "s1", "sourceType" : "Seed", "alias" : ""}
    )
    p1__Reformat_1 = Task(task_id = "p1__Reformat_1", component = "Model", modelName = "p1__Reformat_1")
    Pipeline_1 = Task(
        task_id = "Pipeline_1", 
        component = "Pipeline", 
        maxTriggers = 10000, 
        triggerCondition = "Always", 
        enableMaxTriggers = False, 
        pipelineName = "p1", 
        parameters = {}
    )
    input_csv = Task(
        task_id = "input_csv", 
        component = "OrchestrationTarget", 
        kind = "DatabricksVolumeTarget", 
        connector = Connection(kind = "databricks", id = "databricks_1"), 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "/hellow"}}]}
          }
        }, 
        format = {
          "properties": {
            "allowLazyQuotes": False, 
            "allowEmptyColumnNames": True, 
            "separator": ",", 
            "nullValue": "", 
            "encoding": "UTF-8", 
            "header": True
          }, 
          "kind": "csv", 
          "category": "file"
        }, 
        isNew = False
    )
    Pipeline_1 = Task(
        task_id = "Pipeline_1", 
        component = "Dataset", 
        label = "Pipeline_1", 
        table = {"name" : "{{ prophecy_tmp_source('p1', 'Pipeline_1') }}", "sourceType" : "UnreferencedSource"}
    )
    OrchestrationTarget_1 = Task(
        task_id = "OrchestrationTarget_1", 
        component = "OrchestrationTarget", 
        kind = "OnedriveTarget", 
        connector = Connection(kind = "onedrive"), 
        properties = {}, 
        format = {
          "properties": {
            "allowLazyQuotes": False, 
            "allowEmptyColumnNames": True, 
            "separator": ",", 
            "nullValue": "", 
            "encoding": "UTF-8", 
            "header": True
          }, 
          "kind": "csv", 
          "category": "file"
        }, 
        isNew = True
    )
    catalog_tags = Task(
        task_id = "catalog_tags", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {
          "name": "catalog_tags", 
          "sourceType": "Table", 
          "sourceName": "raghav.information_schema", 
          "alias": "", 
          "additionalProperties": None
        }
    )
    p1__Except_1 = Task(task_id = "p1__Except_1", component = "Model", modelName = "p1__Except_1")
    s1_2 = Task(
        task_id = "s1_2", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "s1", "sourceType" : "Seed", "alias" : ""}
    )
    Pipeline_1.out0 >> Pipeline_1.input_port_r7THacaE
    s1.out >> p1__Reformat_1.in_0
    Pipeline_1.output_port_TnTL9Xzv >> p1__Except_1.in_0
