from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
configuration = {"schema" : {"type" : "record", "fields" : []}}
metainfo = PipelineGraphMetadata(
    label = "p3",
    version = 1,
    configuration = configuration,
    schedule = None,
    sensor_schedule = None,
)

with PipelineGraph(id = "p3", metainfo = metainfo) as graph:
    p3__join_1 = PipelineProcess(
        name = "p3__Join_1",
        metadata = PipelineNodeMetadata(phase = 0),
        properties = GemProperties.ModelTransformSpecProperties(modelName = "p3__Join_1"),
        ports = Ports(inputs = [], outputs = [Port(name = "out_0")], is_custom_output_schema = False)
    )

