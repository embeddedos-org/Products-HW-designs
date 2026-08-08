# eEdgeAI CAD Design

> EmbeddedOS edge AI hardware portfolio — inference accelerators, vision and speech front ends, sensor fusion and SLAM compute, all running the eOS embedded stack.

## Product Lines

| Product | Category | Key Standard | Status |
|---|---|---|---|
| edge_ai_accelerators | General-purpose edge inference compute | CE / FCC Part 15B | Design |
| tinyml_platforms | Always-on microcontroller-class inference | CE / FCC Part 15B | Design |
| npu_subsystems | FPGA-based custom NPU fabric | CE / FCC Part 15B | Design |
| vision_processing | Multi-camera vision pipeline and ISP | IEC 62471 / CE | Design |
| speech_processing | Far-field voice capture and keyword spotting | EN 301 489-1 / CE | Design |
| sensor_fusion | Multi-modal perception fusion | ISO 26262 ASIL-B | Design |
| slam_compute | Simultaneous localisation and mapping | CE / FCC Part 15B | Design |
| inference_servers | Rack and cabinet edge inference aggregation | IEC 62368-1 / EN 55032 Class A | Design |

## Directory Structure

```
eEdgeAI_CAD_Design/
├── README.md
├── edge_ai_accelerators/
├── tinyml_platforms/
├── npu_subsystems/
├── vision_processing/
├── speech_processing/
├── sensor_fusion/
├── slam_compute/
├── inference_servers/
├── docs/
│   ├── business_plan.md
│   └── regulatory_path.md
└── ebuild_simulation/
    └── README.md
```

Each product directory carries a datasheet, a costed bill of materials, a
runnable power simulation, and trees for CAD and PCB artefacts. The data is
generated from `tools/catalog/` and checked by `tools/validate_products.py`.
